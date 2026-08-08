import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.base_service import BaseService
from app.models.bug import Bug, BugState
from app.repositories.bug import RepositoryBug, bug as bug_repo
from app.schemas.bug import BugCreate

class BugService(BaseService[Bug, RepositoryBug]):
    async def ingest_bug(self, db: AsyncSession, *, bug_in: BugCreate, reported_by: uuid.UUID, workspace_id: uuid.UUID) -> Bug:
        obj_in = bug_in.model_dump()
        obj_in["state"] = BugState.OPEN
        obj_in["reported_by"] = reported_by
        obj_in["workspace_id"] = workspace_id
        return await self.create(db, obj_in=obj_in)

bug_service = BugService(repository=bug_repo)
