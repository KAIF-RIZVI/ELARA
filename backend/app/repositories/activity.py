import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.workspace import ActivityLog

class ActivityRepository:
    async def create(self, db: AsyncSession, *, workspace_id: uuid.UUID, action: str, target: str, status: str, user_id: uuid.UUID | None = None) -> ActivityLog:
        obj_in_data = {
            "workspace_id": workspace_id,
            "action": action,
            "target": target,
            "status": status,
            "user_id": user_id
        }
        db_obj = ActivityLog(**obj_in_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

activity_repo = ActivityRepository()