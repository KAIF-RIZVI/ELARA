import uuid
import secrets
import hashlib
from typing import List, Optional
from datetime import datetime, timedelta, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.models.organization import (
    OrganizationInvitation, 
    OrganizationRole, 
    OrganizationInvitationStatus,
    OrganizationAuditLog,
    OrganizationMember,
    Organization
)
from app.models.identity import User
from app.services.email_service import email_service
from fastapi import HTTPException

class OrganizationInvitationService:
    async def create_invitation(
        self, 
        db: AsyncSession, 
        organization_id: uuid.UUID, 
        email: str, 
        role: OrganizationRole,
        invited_by: uuid.UUID
    ) -> OrganizationInvitation:
        # Check if already a member
        stmt = select(OrganizationMember).join(User).where(
            OrganizationMember.organization_id == organization_id,
            User.email == email
        )
        existing_member = (await db.execute(stmt)).scalar_one_or_none()
        if existing_member:
            raise HTTPException(status_code=400, detail="User is already a member of this organization")

        # Check for pending invitations
        stmt = select(OrganizationInvitation).where(
            OrganizationInvitation.organization_id == organization_id,
            OrganizationInvitation.email == email,
            OrganizationInvitation.status == OrganizationInvitationStatus.PENDING,
            OrganizationInvitation.expires_at > datetime.now(timezone.utc)
        )
        existing_invite = (await db.execute(stmt)).scalar_one_or_none()
        if existing_invite:
            raise HTTPException(status_code=400, detail="A pending invitation already exists for this email")

        # Generate secure token
        token = secrets.token_urlsafe(32)
        token_hash = hashlib.sha256(token.encode()).hexdigest()
        
        expires_at = datetime.now(timezone.utc) + timedelta(days=7)
        
        invitation = OrganizationInvitation(
            organization_id=organization_id,
            email=email,
            role=role,
            token_hash=token_hash,
            status=OrganizationInvitationStatus.PENDING,
            invited_by=invited_by,
            expires_at=expires_at
        )
        db.add(invitation)
        
        # Log Audit Event
        audit_log = OrganizationAuditLog(
            organization_id=organization_id,
            actor_id=invited_by,
            event_type="invitation.created",
            resource_type="invitation",
            resource_id=email,
            new_values={"role": role}
        )
        db.add(audit_log)
        
        await db.commit()
        await db.refresh(invitation)
        
        # Get Organization Name
        org = (await db.execute(select(Organization).where(Organization.id == organization_id))).scalar_one_or_none()
        org_name = org.name if org else "an organization"
        
        # Send Email
        try:
            await email_service.send_organization_invitation_email(email, org_name, token)
        except Exception as e:
            # We don't fail the transaction if email fails, it remains PENDING and can be resent
            print(f"Failed to send email to {email}: {e}")
            
        return invitation

    async def get_invitations(self, db: AsyncSession, organization_id: uuid.UUID) -> List[OrganizationInvitation]:
        stmt = select(OrganizationInvitation).where(
            OrganizationInvitation.organization_id == organization_id
        ).order_by(OrganizationInvitation.created_at.desc())
        result = await db.execute(stmt)
        return list(result.scalars().all())

    async def revoke_invitation(
        self, 
        db: AsyncSession, 
        organization_id: uuid.UUID, 
        invitation_id: uuid.UUID,
        actor_id: uuid.UUID
    ) -> bool:
        stmt = select(OrganizationInvitation).where(
            OrganizationInvitation.id == invitation_id,
            OrganizationInvitation.organization_id == organization_id
        )
        invitation = (await db.execute(stmt)).scalar_one_or_none()
        
        if not invitation:
            raise HTTPException(status_code=404, detail="Invitation not found")
            
        if invitation.status != OrganizationInvitationStatus.PENDING:
            raise HTTPException(status_code=400, detail="Can only revoke pending invitations")
            
        invitation.status = OrganizationInvitationStatus.REVOKED
        invitation.revoked_at = datetime.now(timezone.utc)
        
        audit_log = OrganizationAuditLog(
            organization_id=organization_id,
            actor_id=actor_id,
            event_type="invitation.revoked",
            resource_type="invitation",
            resource_id=invitation.email
        )
        db.add(audit_log)
        await db.commit()
        return True

    async def accept_invitation(self, db: AsyncSession, token: str, user_id: uuid.UUID) -> OrganizationMember:
        token_hash = hashlib.sha256(token.encode()).hexdigest()
        stmt = select(OrganizationInvitation).where(OrganizationInvitation.token_hash == token_hash)
        invitation = (await db.execute(stmt)).scalar_one_or_none()
        
        if not invitation:
            raise HTTPException(status_code=404, detail="Invalid invitation token")
            
        if invitation.status != OrganizationInvitationStatus.PENDING:
            raise HTTPException(status_code=400, detail="Invitation is no longer valid")
            
        if invitation.expires_at < datetime.now(timezone.utc):
            invitation.status = OrganizationInvitationStatus.EXPIRED
            await db.commit()
            raise HTTPException(status_code=400, detail="Invitation has expired")
            
        # Check user email matches (case-insensitive)
        user = (await db.execute(select(User).where(User.id == user_id))).scalar_one_or_none()
        if user.email.lower() != invitation.email.lower():
            raise HTTPException(status_code=400, detail="This invitation was sent to a different email address")
            
        # Accept invite
        invitation.status = OrganizationInvitationStatus.ACCEPTED
        invitation.accepted_at = datetime.now(timezone.utc)
        
        # Add member
        member = OrganizationMember(
            organization_id=invitation.organization_id,
            user_id=user_id,
            role=invitation.role,
            status="ACTIVE"
        )
        db.add(member)
        
        audit_log = OrganizationAuditLog(
            organization_id=invitation.organization_id,
            actor_id=user_id,
            event_type="invitation.accepted",
            resource_type="invitation",
            resource_id=invitation.email
        )
        db.add(audit_log)
        
        await db.commit()
        await db.refresh(member)
        return member

    async def reject_invitation(self, db: AsyncSession, token: str, user_id: uuid.UUID) -> bool:
        token_hash = hashlib.sha256(token.encode()).hexdigest()
        stmt = select(OrganizationInvitation).where(OrganizationInvitation.token_hash == token_hash)
        invitation = (await db.execute(stmt)).scalar_one_or_none()
        
        if not invitation:
            raise HTTPException(status_code=404, detail="Invalid invitation token")
            
        if invitation.status != OrganizationInvitationStatus.PENDING:
            raise HTTPException(status_code=400, detail="Invitation is no longer valid")
            
        user = (await db.execute(select(User).where(User.id == user_id))).scalar_one_or_none()
        if user.email != invitation.email:
            raise HTTPException(status_code=400, detail="This invitation was sent to a different email address")
            
        invitation.status = OrganizationInvitationStatus.DECLINED
        
        audit_log = OrganizationAuditLog(
            organization_id=invitation.organization_id,
            actor_id=user_id,
            event_type="invitation.declined",
            resource_type="invitation",
            resource_id=invitation.email
        )
        db.add(audit_log)
        await db.commit()
        return True

organization_invitation_service = OrganizationInvitationService()
