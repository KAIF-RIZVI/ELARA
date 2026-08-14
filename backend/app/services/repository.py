from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.base_service import BaseService
from app.models.project import Repository, SyncStatus
from app.repositories.repository import RepositoryRepo, repository_repo
from app.services.activity import activity_service
from app.schemas.repository import RepositoryCreate
from datetime import datetime, timezone
import uuid

class RepositoryService(BaseService[Repository, RepositoryRepo]):
    async def get_by_workspace(self, db: AsyncSession, workspace_id: uuid.UUID) -> list[Repository]:
        stmt = select(Repository).where(Repository.workspace_id == workspace_id)
        result = await db.execute(stmt)
        return list(result.scalars().all())

    async def get_by_organization(self, db: AsyncSession, organization_id: uuid.UUID) -> list[Repository]:
        stmt = select(Repository).where(Repository.organization_id == organization_id)
        result = await db.execute(stmt)
        return list(result.scalars().all())
        
    async def connect_repository(
        self, db: AsyncSession, *, repo_in: RepositoryCreate, user_id: uuid.UUID
    ) -> Repository:
        # Check if already exists in context
        stmt = select(Repository).where(Repository.full_name == repo_in.full_name)
        if repo_in.workspace_id:
            stmt = stmt.where(Repository.workspace_id == repo_in.workspace_id)
        elif repo_in.organization_id:
            stmt = stmt.where(Repository.organization_id == repo_in.organization_id)
            
        existing = await db.scalar(stmt)
        if existing:
            raise ValueError(f"Repository {repo_in.full_name} is already connected.")
            
        obj_in = repo_in.model_dump(exclude_unset=True)
        obj_in["sync_status"] = SyncStatus.PENDING
        obj_in["project_id"] = None
        
        repo = await self.create(db, obj_in=obj_in)
        
        # Log activity
        if repo_in.workspace_id:
            await activity_service.log_activity(
                db=db,
                workspace_id=repo_in.workspace_id,
                action="Repository Connected",
                target=repo_in.full_name,
                status="success",
                user_id=user_id
            )
        
        return repo
        
    def calculate_health_score(self, repo: Repository) -> int:
        score = 100
        
        # Deduct for failed syncs
        if repo.sync_status == SyncStatus.FAILED:
            score -= 30
            
        # Deduct for stale sync (older than 24 hours)
        if repo.last_synced_at:
            delta = datetime.now(timezone.utc) - repo.last_synced_at
            if delta.total_seconds() > 86400:
                score -= 20
        elif repo.sync_status != SyncStatus.PENDING:
            score -= 20
            
        # AI readiness
        if not repo.ai_ready:
            score -= 10
            
        # Index status
        if repo.index_status == "FAILED":
            score -= 20
        elif repo.index_status == "UNINDEXED":
            score -= 10
            
        return max(0, score)
        
    async def disconnect_repository(self, db: AsyncSession, *, repository_id: uuid.UUID, workspace_id: uuid.UUID | None, organization_id: uuid.UUID | None, user_id: uuid.UUID) -> None:
        repo = await self.get(db, repository_id)
        if not repo:
            raise ValueError("Repository not found")
            
        if workspace_id and repo.workspace_id != workspace_id:
            raise ValueError("Repository not found in workspace")
        if organization_id and repo.organization_id != organization_id:
            raise ValueError("Repository not found in organization")
            
        full_name = repo.full_name
        
        await self.remove(db, id=repository_id)
        
        # Log activity
        if workspace_id:
            await activity_service.log_activity(
                db=db,
                workspace_id=workspace_id,
                action="Repository Disconnected",
                target=full_name,
                status="warning",
                user_id=user_id
            )

repository_service = RepositoryService(repository=repository_repo)