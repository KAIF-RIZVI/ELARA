import uuid
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.orm import joinedload
from app.models.organization import OrganizationMember, OrganizationRole, OrganizationAuditLog
from app.models.identity import User
from fastapi import HTTPException

class OrganizationMemberService:
    async def get_members(self, db: AsyncSession, organization_id: uuid.UUID) -> List[OrganizationMember]:
        stmt = select(OrganizationMember, User).join(
            User, OrganizationMember.user_id == User.id
        ).where(
            OrganizationMember.organization_id == organization_id
        ).order_by(OrganizationMember.created_at.desc())
        
        result = await db.execute(stmt)
        rows = result.all()
        
        # Hydrate the model with user info for response
        members = []
        for member, user in rows:
            member.full_name = user.full_name
            member.email = user.email
            member.avatar_url = user.avatar_url
            members.append(member)
            
        return members

    async def get_member(self, db: AsyncSession, organization_id: uuid.UUID, user_id: uuid.UUID) -> Optional[OrganizationMember]:
        stmt = select(OrganizationMember).where(
            OrganizationMember.organization_id == organization_id,
            OrganizationMember.user_id == user_id
        )
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    async def update_member_role(
        self, 
        db: AsyncSession, 
        organization_id: uuid.UUID, 
        user_id: uuid.UUID, 
        new_role: OrganizationRole,
        actor_id: uuid.UUID
    ) -> OrganizationMember:
        member = await self.get_member(db, organization_id, user_id)
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")
            
        old_role = member.role
        member.role = new_role
        
        # Log Audit Event
        audit_log = OrganizationAuditLog(
            organization_id=organization_id,
            actor_id=actor_id,
            event_type="member.role_updated",
            resource_type="member",
            resource_id=str(user_id),
            old_values={"role": old_role},
            new_values={"role": new_role}
        )
        db.add(audit_log)
        await db.commit()
        await db.refresh(member)
        return member

    async def remove_member(
        self, 
        db: AsyncSession, 
        organization_id: uuid.UUID, 
        user_id: uuid.UUID,
        actor_id: uuid.UUID
    ) -> bool:
        member = await self.get_member(db, organization_id, user_id)
        if not member:
            raise HTTPException(status_code=404, detail="Member not found")
            
        if member.role == OrganizationRole.OWNER:
            raise HTTPException(status_code=400, detail="Cannot remove the owner of the organization")
            
        await db.delete(member)
        
        audit_log = OrganizationAuditLog(
            organization_id=organization_id,
            actor_id=actor_id,
            event_type="member.removed",
            resource_type="member",
            resource_id=str(user_id)
        )
        db.add(audit_log)
        await db.commit()
        return True

organization_member_service = OrganizationMemberService()
