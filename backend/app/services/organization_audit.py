import uuid
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.organization import OrganizationAuditLog
from app.models.identity import User

class OrganizationAuditService:
    async def get_audit_logs(self, db: AsyncSession, organization_id: uuid.UUID, limit: int = 50) -> List[OrganizationAuditLog]:
        # We join User to get the actor's name/email for display
        stmt = select(OrganizationAuditLog, User).outerjoin(
            User, OrganizationAuditLog.actor_id == User.id
        ).where(
            OrganizationAuditLog.organization_id == organization_id
        ).order_by(OrganizationAuditLog.created_at.desc()).limit(limit)
        
        result = await db.execute(stmt)
        rows = result.all()
        
        logs = []
        for log, user in rows:
            if user:
                log.actor_name = user.full_name
                log.actor_email = user.email
            logs.append(log)
            
        return logs
    async def log_action(
        self,
        db: AsyncSession,
        organization_id: uuid.UUID,
        event_type: str,
        resource_type: str,
        resource_id: str,
        actor_id: uuid.UUID | None = None,
        old_values: dict | None = None,
        new_values: dict | None = None,
        metadata_json: dict | None = None,
        ip_address: str | None = None,
        user_agent: str | None = None
    ) -> OrganizationAuditLog:
        log_entry = OrganizationAuditLog(
            organization_id=organization_id,
            actor_id=actor_id,
            event_type=event_type,
            resource_type=resource_type,
            resource_id=resource_id,
            old_values=old_values,
            new_values=new_values,
            metadata_json=metadata_json,
            ip_address=ip_address,
            user_agent=user_agent
        )
        db.add(log_entry)
        await db.commit()
        await db.refresh(log_entry)
        return log_entry

organization_audit_service = OrganizationAuditService()
