import os
import shutil
import logging
from datetime import datetime, timezone, timedelta
from app.worker.celery_app import celery_app
from app.core.database import AsyncSessionLocal as SessionLocal
from app.services.repository_indexing import repository_indexing_service
from app.models.project import JobStatus
import uuid

logger = logging.getLogger(__name__)

@celery_app.task(name="cleanup_stale_workspaces")
def cleanup_stale_workspaces():
    """
    Layer 3 Cleanup Mechanism.
    Scans /tmp/elara/indexing for stale workspaces and deletes them securely.
    """
    base_dir = "/tmp/elara/indexing/"
    if not os.path.exists(base_dir):
        return {"status": "NO_CLEANUP_NEEDED"}

    cleaned_count = 0
    for dirname in os.listdir(base_dir):
        workspace_path = os.path.join(base_dir, dirname)
        if not os.path.isdir(workspace_path):
            continue

        try:
            job_id = uuid.UUID(dirname)
        except ValueError:
            logger.warning(f"Found invalid directory in indexing workspace: {workspace_path}")
            continue

        # In a synchronous context (Celery beat), we need an async event loop for SQLAlchemy ops.
        # But for this simple cleanup, we can just use _run_async trick.
        from app.worker.tasks.repo_tasks import _run_async
        
        async def _check_and_clean():
            async with SessionLocal() as db:
                from sqlalchemy import select
                from app.models.project import RepoIndexJob
                job = await db.scalar(select(RepoIndexJob).where(RepoIndexJob.id == job_id))
                
                # If job doesn't exist, it's definitively orphaned
                if not job:
                    return True
                
                # If job is in a terminal state, the workspace is orphaned (Layer 1 failed to clean it)
                if job.status in [JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED]:
                    return True
                
                # If job is active but stale (started > 2 hours ago without finishing)
                # Note: Legitimate long jobs are kept if within the timeout. 
                if job.started_at:
                    if datetime.now(timezone.utc) - job.started_at > timedelta(hours=2):
                        # Force transition to FAILED due to timeout
                        await repository_indexing_service.update_job_status(
                            db, job_id, JobStatus.FAILED, error="Job timed out and was cleaned up by watchdog", error_code="TIMEOUT"
                        )
                        return True
                
                return False

        should_clean = _run_async(_check_and_clean())
        
        if should_clean:
            try:
                shutil.rmtree(workspace_path)
                logger.info(f"Watchdog cleaned stale workspace: {workspace_path}")
                cleaned_count += 1
            except Exception as e:
                logger.error(f"Watchdog failed to clean {workspace_path}: {e}")

    return {"status": "SUCCESS", "cleaned_count": cleaned_count}
