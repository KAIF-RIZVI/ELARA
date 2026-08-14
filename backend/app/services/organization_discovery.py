import uuid
from typing import List, Dict, Any, Optional
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, func, or_, and_
from app.models.organization import (
    Organization,
    OrganizationMember,
    OrganizationJoinRequest,
    OrganizationAuditLog,
    JoinPolicy,
    JoinRequestStatus,
    OrganizationRole
)
from app.models.identity import User
from app.models.notification import NotificationType, NotificationPriority
from app.services.notification_service import notification_service
from fastapi import HTTPException

class OrganizationDiscoveryService:
    async def search_organizations(
        self, 
        db: AsyncSession, 
        user_id: uuid.UUID,
        query: Optional[str] = None, 
        limit: int = 50, 
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        # Subquery for member count
        member_count_subq = (
            select(func.count(OrganizationMember.id))
            .where(OrganizationMember.organization_id == Organization.id)
            .where(OrganizationMember.status == "ACTIVE")
            .scalar_subquery()
            .correlate(Organization)
        )

        # Subquery to get owner's name
        owner_name_subq = (
            select(User.full_name)
            .where(User.id == Organization.owner_id)
            .scalar_subquery()
            .correlate(Organization)
        )

        # Subquery to check if current user is member
        is_member_subq = (
            select(func.count(OrganizationMember.id) > 0)
            .where(OrganizationMember.organization_id == Organization.id)
            .where(OrganizationMember.user_id == user_id)
            .scalar_subquery()
            .correlate(Organization)
        )

        # Subquery to check if current user has pending request
        has_pending_subq = (
            select(func.count(OrganizationJoinRequest.id) > 0)
            .where(OrganizationJoinRequest.organization_id == Organization.id)
            .where(OrganizationJoinRequest.user_id == user_id)
            .where(OrganizationJoinRequest.status == JoinRequestStatus.PENDING)
            .scalar_subquery()
            .correlate(Organization)
        )

        stmt = select(
            Organization,
            member_count_subq.label("member_count"),
            owner_name_subq.label("owner_name"),
            is_member_subq.label("is_member"),
            has_pending_subq.label("has_pending")
        ).where(
            Organization.discoverable == True
        )

        if query:
            try:
                org_id = uuid.UUID(query)
                stmt = stmt.where(Organization.id == org_id)
            except ValueError:
                # If query is not a valid UUID, return empty result
                stmt = stmt.where(False)

        stmt = stmt.limit(limit).offset(offset).order_by(Organization.name)
        result = await db.execute(stmt)

        orgs = []
        for org, member_count, owner_name, is_member, has_pending in result.all():
            user_relation = "NONE"
            if is_member:
                user_relation = "MEMBER"
            elif has_pending:
                user_relation = "PENDING_REQUEST"
                
            orgs.append({
                "id": org.id,
                "name": org.name,
                "slug": org.slug,
                "logo_url": org.logo_url,
                "tagline": org.tagline,
                "member_count": member_count,
                "join_policy": org.join_policy,
                "owner_name": owner_name,
                "user_relation": user_relation
            })
            
        return orgs

    async def get_join_requests(self, db: AsyncSession, organization_id: uuid.UUID) -> List[Dict[str, Any]]:
        stmt = select(
            OrganizationJoinRequest,
            User.full_name.label("user_name"),
            User.email.label("user_email"),
            User.avatar_url.label("user_avatar")
        ).join(
            User, OrganizationJoinRequest.user_id == User.id
        ).where(
            OrganizationJoinRequest.organization_id == organization_id,
            OrganizationJoinRequest.status == JoinRequestStatus.PENDING
        ).order_by(OrganizationJoinRequest.created_at.desc())
        
        result = await db.execute(stmt)
        
        requests = []
        for req, user_name, user_email, user_avatar in result.all():
            req_dict = req.__dict__.copy()
            req_dict.pop('_sa_instance_state', None)
            req_dict['user_name'] = user_name
            req_dict['user_email'] = user_email
            req_dict['user_avatar'] = user_avatar
            requests.append(req_dict)
            
        return requests

    async def create_join_request(
        self,
        db: AsyncSession,
        organization_id: uuid.UUID,
        user_id: uuid.UUID,
        message: Optional[str]
    ) -> OrganizationJoinRequest:
        # Check org exists and discoverable
        org = (await db.execute(select(Organization).where(Organization.id == organization_id))).scalar_one_or_none()
        if not org or not org.discoverable or org.join_policy == JoinPolicy.CLOSED:
            raise HTTPException(status_code=400, detail="Organization is not open for join requests")
            
        # Check if already member
        existing_member = (await db.execute(select(OrganizationMember).where(
            OrganizationMember.organization_id == organization_id,
            OrganizationMember.user_id == user_id
        ))).scalar_one_or_none()
        if existing_member:
            raise HTTPException(status_code=400, detail="You are already a member of this organization")
            
        # Check for existing pending request
        existing_req = (await db.execute(select(OrganizationJoinRequest).where(
            OrganizationJoinRequest.organization_id == organization_id,
            OrganizationJoinRequest.user_id == user_id,
            OrganizationJoinRequest.status == JoinRequestStatus.PENDING
        ))).scalar_one_or_none()
        if existing_req:
            raise HTTPException(status_code=400, detail="You already have a pending join request")
            
        req = OrganizationJoinRequest(
            organization_id=organization_id,
            user_id=user_id,
            message=message,
            status=JoinRequestStatus.PENDING
        )
        db.add(req)
        
        # Log Audit Event
        audit_log = OrganizationAuditLog(
            organization_id=organization_id,
            actor_id=user_id,
            event_type="join_request.created",
            resource_type="join_request",
            resource_id=str(user_id)
        )
        db.add(audit_log)
        
        # Notify admins
        admins_result = await db.execute(select(OrganizationMember.user_id).where(
            OrganizationMember.organization_id == organization_id,
            OrganizationMember.role.in_([OrganizationRole.OWNER, OrganizationRole.ADMIN]),
            OrganizationMember.status == "ACTIVE"
        ))
        admin_ids = [row[0] for row in admins_result.all()]
        applicant = (await db.execute(select(User).where(User.id == user_id))).scalar_one()

        await notification_service.create_bulk_notifications(
            db=db,
            recipient_user_ids=admin_ids,
            type=NotificationType.JOIN_REQUEST,
            title="Join Request",
            message=f"{applicant.full_name} requested to join {org.name}",
            priority=NotificationPriority.INFO,
            organization_id=organization_id,
            action_url=f"/organizations/{org.slug}/team",
            action_label="View Request"
        )
        
        await db.commit()
        await db.refresh(req)
        return req

    async def cancel_join_request(
        self,
        db: AsyncSession,
        organization_id: uuid.UUID,
        user_id: uuid.UUID
    ) -> bool:
        req = (await db.execute(select(OrganizationJoinRequest).where(
            OrganizationJoinRequest.organization_id == organization_id,
            OrganizationJoinRequest.user_id == user_id,
            OrganizationJoinRequest.status == JoinRequestStatus.PENDING
        ))).scalar_one_or_none()
        
        if not req:
            raise HTTPException(status_code=404, detail="Pending join request not found")
            
        req.status = JoinRequestStatus.CANCELLED
        
        audit_log = OrganizationAuditLog(
            organization_id=organization_id,
            actor_id=user_id,
            event_type="join_request.cancelled",
            resource_type="join_request",
            resource_id=str(req.id)
        )
        db.add(audit_log)
        await db.commit()
        return True

    async def approve_join_request(
        self,
        db: AsyncSession,
        organization_id: uuid.UUID,
        request_id: uuid.UUID,
        actor_id: uuid.UUID
    ) -> OrganizationMember:
        req = (await db.execute(select(OrganizationJoinRequest).where(
            OrganizationJoinRequest.id == request_id,
            OrganizationJoinRequest.organization_id == organization_id
        ))).scalar_one_or_none()
        
        if not req:
            raise HTTPException(status_code=404, detail="Join request not found")
            
        if req.status != JoinRequestStatus.PENDING:
            raise HTTPException(status_code=400, detail="Only pending requests can be approved")
            
        req.status = JoinRequestStatus.APPROVED
        req.reviewed_at = datetime.now(timezone.utc)
        req.reviewed_by = actor_id
        
        # Add as member (default role VIEWER or DEVELOPER, depending on your RBAC, assuming DEVELOPER here)
        member = OrganizationMember(
            organization_id=organization_id,
            user_id=req.user_id,
            role=OrganizationRole.DEVELOPER,
            status="ACTIVE"
        )
        db.add(member)
        
        audit_log = OrganizationAuditLog(
            organization_id=organization_id,
            actor_id=actor_id,
            event_type="join_request.approved",
            resource_type="join_request",
            resource_id=str(req.id)
        )
        db.add(audit_log)
        
        org = (await db.execute(select(Organization).where(Organization.id == organization_id))).scalar_one()
        await notification_service.create_notification(
            db=db,
            recipient_user_id=req.user_id,
            type=NotificationType.JOIN_APPROVED,
            title="Join Request Approved",
            message=f"Your request to join {org.name} has been approved.",
            priority=NotificationPriority.SUCCESS,
            organization_id=organization_id,
            action_url=f"/organizations/{org.slug}",
            action_label="View Organization"
        )
        
        await db.commit()
        await db.refresh(member)
        return member

    async def reject_join_request(
        self,
        db: AsyncSession,
        organization_id: uuid.UUID,
        request_id: uuid.UUID,
        actor_id: uuid.UUID
    ) -> bool:
        req = (await db.execute(select(OrganizationJoinRequest).where(
            OrganizationJoinRequest.id == request_id,
            OrganizationJoinRequest.organization_id == organization_id
        ))).scalar_one_or_none()
        
        if not req:
            raise HTTPException(status_code=404, detail="Join request not found")
            
        if req.status != JoinRequestStatus.PENDING:
            raise HTTPException(status_code=400, detail="Only pending requests can be rejected")
            
        req.status = JoinRequestStatus.REJECTED
        req.reviewed_at = datetime.now(timezone.utc)
        req.reviewed_by = actor_id
        
        audit_log = OrganizationAuditLog(
            organization_id=organization_id,
            actor_id=actor_id,
            event_type="join_request.rejected",
            resource_type="join_request",
            resource_id=str(req.id)
        )
        db.add(audit_log)
        
        org = (await db.execute(select(Organization).where(Organization.id == organization_id))).scalar_one()
        await notification_service.create_notification(
            db=db,
            recipient_user_id=req.user_id,
            type=NotificationType.JOIN_REJECTED,
            title="Join Request Declined",
            message=f"Your request to join {org.name} has been declined.",
            priority=NotificationPriority.INFO,
            organization_id=organization_id
        )
        
        await db.commit()
        return True

organization_discovery_service = OrganizationDiscoveryService()
