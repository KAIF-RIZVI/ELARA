from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.base_service import BaseService
from app.models.workspace import Workspace, WorkspaceStatus
from app.repositories.workspace import RepositoryWorkspace, workspace as workspace_repo

class WorkspaceService(BaseService[Workspace, RepositoryWorkspace]):
    async def create_workspace(self, db: AsyncSession, *, name: str, slug: str, settings: dict[str, Any] | None = None) -> Workspace:
        # Check if slug exists
        existing = await self.repository.get_by_slug(db, slug)
        if existing:
            raise ValueError(f"Workspace with slug {slug} already exists.")
        
        obj_in = {
            "name": name,
            "slug": slug,
            "status": WorkspaceStatus.ACTIVE,
            "settings": settings or {}
        }
        return await self.create(db, obj_in=obj_in)

workspace_service = WorkspaceService(repository=workspace_repo)
