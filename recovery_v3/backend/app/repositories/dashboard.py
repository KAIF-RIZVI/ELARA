import uuid
from sqlalchemy import select, func, desc
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Repository, Bug, WorkspaceMember, ActivityLog, RepoIndexJob

class DashboardRepository:
    async def get_active_repositories_count(self, db: AsyncSession, workspace_id: uuid.UUID) -> int:
        stmt = select(func.count()).select_from(Repository).where(Repository.workspace_id == workspace_id)
        result = await db.execute(stmt)
        return result.scalar() or 0

    async def get_open_bugs_count(self, db: AsyncSession, workspace_id: uuid.UUID) -> int:
        stmt = select(func.count()).select_from(Bug).where(Bug.workspace_id == workspace_id, Bug.status == "OPEN")
        result = await db.execute(stmt)
        return result.scalar() or 0

    async def get_auto_resolved_bugs_count(self, db: AsyncSession, workspace_id: uuid.UUID) -> int:
        stmt = select(func.count()).select_from(Bug).where(Bug.workspace_id == workspace_id, Bug.status == "CLOSED")
        result = await db.execute(stmt)
        return result.scalar() or 0

    async def get_team_size(self, db: AsyncSession, workspace_id: uuid.UUID) -> int:
        stmt = select(func.count()).select_from(WorkspaceMember).where(WorkspaceMember.workspace_id == workspace_id)
        result = await db.execute(stmt)
        return result.scalar() or 0

    async def get_system_health_metrics(self, db: AsyncSession, workspace_id: uuid.UUID) -> tuple[int, int]:
        # Returns (total_jobs, failed_jobs)
        stmt_total = select(func.count()).select_from(RepoIndexJob).join(Repository).where(Repository.workspace_id == workspace_id)
        stmt_failed = select(func.count()).select_from(RepoIndexJob).join(Repository).where(Repository.workspace_id == workspace_id, RepoIndexJob.status == "FAILED")
        
        total = await db.scalar(stmt_total) or 0
        failed = await db.scalar(stmt_failed) or 0
        return total, failed

    async def get_recent_activity(self, db: AsyncSession, workspace_id: uuid.UUID, limit: int = 5) -> list[ActivityLog]:
        stmt = select(ActivityLog).where(ActivityLog.workspace_id == workspace_id).order_by(desc(ActivityLog.created_at)).limit(limit)
        result = await db.execute(stmt)
        return list(result.scalars().all())

dashboard_repo = DashboardRepository()