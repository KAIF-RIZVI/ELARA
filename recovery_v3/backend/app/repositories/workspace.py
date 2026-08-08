import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.base_repository import BaseRepository
from app.models.workspace import Workspace

class RepositoryWorkspace(BaseRepository[Workspace]):
    async def get_by_slug(self, db: AsyncSession, slug: str) -> Workspace | None:
        result = await db.execute(select(Workspace).where(Workspace.slug == slug))
        return result.scalars().first()

workspace = RepositoryWorkspace(Workspace)
