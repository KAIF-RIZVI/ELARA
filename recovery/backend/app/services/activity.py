import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.activity import activity_repo

class ActivityService:
    async def log_activity(self, db: AsyncSession, workspace_id: uuid.UUID, action: str, target: str, status: str = "success", user_id: uuid.UUID | None = None) -> None:
        """
        Log a system or user activity event.
        status should be one of: "success", "info", "warning", "error"
        """
        await activity_repo.create(db=db, workspace_id=workspace_id, action=action, target=target, status=status, user_id=user_id)

activity_service = ActivityService()