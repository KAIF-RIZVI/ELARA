import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.base_repository import BaseRepository
from app.models.developer import DeveloperProfile

class RepositoryDeveloperProfile(BaseRepository[DeveloperProfile]):
    async def get_by_user_id(self, db: AsyncSession, user_id: uuid.UUID) -> DeveloperProfile | None:
        result = await db.execute(select(DeveloperProfile).where(DeveloperProfile.user_id == user_id))
        return result.scalars().first()

profile_repo = RepositoryDeveloperProfile(DeveloperProfile)