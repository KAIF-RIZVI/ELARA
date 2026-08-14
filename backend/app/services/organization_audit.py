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

organization_audit_service = OrganizationAuditService()
