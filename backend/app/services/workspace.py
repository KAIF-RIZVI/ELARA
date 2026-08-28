import uuid
from typing import Any
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.base_service import BaseService
from app.models.workspace import Workspace, WorkspaceStatus
from app.repositories.workspace import RepositoryWorkspace, workspace as workspace_repo

class WorkspaceService(BaseService[Workspace, RepositoryWorkspace]):
    async def create_workspace(self, db: AsyncSession, *, name: str, slug: str, user_id: uuid.UUID, organization_id: uuid.UUID, settings: dict[str, Any] | None = None) -> Workspace:
        from app.models.organization import OrganizationMember
        from sqlalchemy import select
        
        # Verify user belongs to the specified organization
        stmt = select(OrganizationMember).where(
            OrganizationMember.organization_id == organization_id,
            OrganizationMember.user_id == user_id
        )
        result = await db.execute(stmt)
        org_member = result.scalar_one_or_none()
        if not org_member:
            raise ValueError("User does not belong to the specified organization or organization does not exist.")

        # Check if slug exists
        existing = await self.repository.get_by_slug(db, slug)
        if existing:
            raise ValueError(f"Workspace with slug {slug} already exists.")
        
        workspace = Workspace(
            name=name,
            slug=slug,
            organization_id=organization_id,
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
