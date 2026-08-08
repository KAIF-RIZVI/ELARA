import uuid
from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.base_service import BaseService
from app.models.workspace import Workspace, WorkspaceStatus
from app.repositories.workspace import RepositoryWorkspace, workspace as workspace_repo

class WorkspaceService(BaseService[Workspace, RepositoryWorkspace]):
    async def create_workspace(self, db: AsyncSession, *, name: str, slug: str, user_id: uuid.UUID, settings: dict[str, Any] | None = None) -> Workspace:
        # Check if slug exists
        existing = await self.repository.get_by_slug(db, slug)
        if existing:
            raise ValueError(f"Workspace with slug {slug} already exists.")
        
        workspace = Workspace(
            name=name,
            slug=slug,
            status=WorkspaceStatus.ACTIVE,
            settings=settings or {}
        )
        db.add(workspace)
        await db.flush() # get workspace id
        
        from app.models.identity import WorkspaceMember, MemberRole, MemberStatus
        member = WorkspaceMember(
            workspace_id=workspace.id,
            user_id=user_id,
            role=MemberRole.OWNER,
            status=MemberStatus.ACTIVE
        )
        db.add(member)
        await db.commit()
        await db.refresh(workspace)
        return workspace

workspace_service = WorkspaceService(repository=workspace_repo)
