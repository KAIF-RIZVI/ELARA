from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.base_service import BaseService
from app.models.project import Repository, SyncStatus
from app.repositories.repository import RepositoryRepo, repository_repo
from app.services.activity import activity_service
import uuid

class RepositoryService(BaseService[Repository, RepositoryRepo]):
    async def get_by_workspace(self, db: AsyncSession, workspace_id: uuid.UUID) -> list[Repository]:
        stmt = select(Repository).where(Repository.workspace_id == workspace_id)
        result = await db.execute(stmt)
        return list(result.scalars().all())
        
    async def connect_repository(
        self, db: AsyncSession, *, workspace_id: uuid.UUID, provider: str, full_name: str, external_id: str, default_branch: str, user_id: uuid.UUID
    ) -> Repository:
        # Check if already exists in workspace
        stmt = select(Repository).where(
            Repository.workspace_id == workspace_id,
            Repository.full_name == full_name
        )
        existing = await db.scalar(stmt)
        if existing:
            raise ValueError(f"Repository {full_name} is already connected to this workspace.")
            
        obj_in = {
            "workspace_id": workspace_id,
            "provider": provider,
            "full_name": full_name,
            "external_id": external_id,
            "default_branch": default_branch,
            "sync_status": SyncStatus.PENDING,
            "project_id": None
        }
        
        repo = await self.create(db, obj_in=obj_in)
        
        # Log activity
        await activity_service.log_activity(
            db=db,
            workspace_id=workspace_id,
            action="Repository Connected",
            target=full_name,
            status="success",
            user_id=user_id
        )
        
        return repo
        
    async def disconnect_repository(self, db: AsyncSession, *, repository_id: uuid.UUID, workspace_id: uuid.UUID, user_id: uuid.UUID) -> None:
        repo = await self.get(db, repository_id)
        if not repo or repo.workspace_id != workspace_id:
            raise ValueError("Repository not found in workspace")
            
        full_name = repo.full_name
        
        await self.remove(db, id=repository_id)
        
        # Log activity
        await activity_service.log_activity(
            db=db,
            workspace_id=workspace_id,
            action="Repository Disconnected",
            target=full_name,
            status="warning",
            user_id=user_id
        )

repository_service = RepositoryService(repository=repository_repo)