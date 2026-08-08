import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.dashboard import dashboard_repo

class DashboardService:
    async def get_stats(self, db: AsyncSession, workspace_id: uuid.UUID) -> dict:
        repos_count = await dashboard_repo.get_active_repositories_count(db, workspace_id)
        bugs_count = await dashboard_repo.get_open_bugs_count(db, workspace_id)
        auto_resolved = await dashboard_repo.get_auto_resolved_bugs_count(db, workspace_id)
        team_size = await dashboard_repo.get_team_size(db, workspace_id)
        
        total_jobs, failed_jobs = await dashboard_repo.get_system_health_metrics(db, workspace_id)
        health_percentage = "100%"
        if total_jobs > 0:
            success_rate = ((total_jobs - failed_jobs) / total_jobs) * 100
            health_percentage = f"{success_rate:.1f}%"
        
        return {
            "active_repositories": repos_count,
            "open_bugs": bugs_count,
            "auto_resolved": auto_resolved,
            "team_size": team_size,
            "system_health": health_percentage
        }

    async def get_activity(self, db: AsyncSession, workspace_id: uuid.UUID) -> list[dict]:
        logs = await dashboard_repo.get_recent_activity(db, workspace_id)
        return [
            {
                "id": str(log.id),
                "action": log.action,
                "target": log.target,
                "status": log.status,
                "time": log.created_at.isoformat() + "Z" if log.created_at else None
            } for log in logs
        ]

dashboard_service = DashboardService()