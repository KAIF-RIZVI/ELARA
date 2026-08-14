import uuid
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.models.organization import OrganizationSettings, OrganizationAuditLog
from app.schemas.organization import OrganizationSettingsUpdate
from fastapi import HTTPException

class OrganizationSettingsService:
    async def get_settings(self, db: AsyncSession, organization_id: uuid.UUID) -> OrganizationSettings:
        stmt = select(OrganizationSettings).where(OrganizationSettings.organization_id == organization_id)
        settings = (await db.execute(stmt)).scalar_one_or_none()
        if not settings:
            raise HTTPException(status_code=404, detail="Settings not found")
        return settings

    async def update_settings(
        self, 
        db: AsyncSession, 
        organization_id: uuid.UUID, 
        settings_in: OrganizationSettingsUpdate,
        actor_id: uuid.UUID
    ) -> OrganizationSettings:
        settings = await self.get_settings(db, organization_id)
        
        update_data = settings_in.model_dump(exclude_unset=True)
        if not update_data:
            return settings
            
        old_values = {}
        new_values = {}
        for field, value in update_data.items():
            old_val = getattr(settings, field, None)
            if old_val != value:
                old_values[field] = old_val
                new_values[field] = value
                setattr(settings, field, value)
                
        if new_values:
            audit_log = OrganizationAuditLog(
                organization_id=organization_id,
                actor_id=actor_id,
                event_type="settings.updated",
                resource_type="settings",
                resource_id=str(settings.id),
                old_values=old_values,
                new_values=new_values
            )
            db.add(audit_log)
            await db.commit()
            await db.refresh(settings)
            
        return settings

organization_settings_service = OrganizationSettingsService()
