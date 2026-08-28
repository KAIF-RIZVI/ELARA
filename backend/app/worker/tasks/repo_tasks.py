import asyncio
import os
import shutil
import uuid
import logging
from app.worker.celery_app import celery_app
from app.core.database import AsyncSessionLocal as SessionLocal
from app.services.repository_processor import repository_processor
from app.services.repository_indexing import repository_indexing_service
from app.models.project import JobStatus

logger = logging.getLogger(__name__)

def _run_async(coro):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)

@celery_app.task(name="index_repository_job")
def index_repository_job(job_id_str: str, organization_id_str: str):
    """
    Background task to securely process and index a repository.
    Enforces Layer 1 Cleanup (try/finally).
    """
    job_id = uuid.UUID(job_id_str)
    organization_id = uuid.UUID(organization_id_str)
    workspace_dir = f"/tmp/elara/indexing/{job_id}/"
    
    logger.info(f"Starting ephemeral indexing job {job_id} for organization {organization_id}")
    
    async def _execute():
        async with SessionLocal() as db:
            try:
                await repository_processor.process_job(db, job_id, organization_id)
            except Exception as e:
                import traceback
                logger.error(f"Job {job_id} failed with error: {e}")
                logger.error(traceback.format_exc())
                # Ensure status is FAILED if it bubbled up without being caught
                job = await repository_indexing_service.get_job(db, job_id, organization_id)
                if job and job.status not in [JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED]:
                    await repository_indexing_service.update_job_status(db, job_id, JobStatus.FAILED, error="Unhandled worker exception", error_code="WORKER_CRASH")

    try:
        _run_async(_execute())
    finally:
        # Layer 1 Cleanup Guarantee: Delete the ephemeral workspace
        if os.path.exists(workspace_dir):
            try:
                shutil.rmtree(workspace_dir)
                logger.info(f"Successfully cleaned up ephemeral workspace: {workspace_dir}")
            except Exception as cleanup_err:
                logger.error(f"Failed to clean up workspace {workspace_dir}: {cleanup_err}")

    return {"status": "FINISHED", "job_id": str(job_id)}

@celery_app.task(name="sync_repository_task")
def sync_repository_task(repository_id: str, workspace_id: str = None, organization_id: str = None):
    """
    Deprecated compatibility wrapper for existing frontend workflows.
    In a real scenario, this delegates to the new endpoint logic.
    """
    pass