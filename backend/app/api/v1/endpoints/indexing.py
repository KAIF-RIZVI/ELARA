from fastapi import APIRouter, Depends, HTTPException, status
import uuid
from typing import Optional

from app.api.deps import SessionDep, CurrentUser, RequireOrganizationRole
from app.models.organization import OrganizationRole
from app.services.repository_indexing import repository_indexing_service

router = APIRouter()

@router.get("/jobs/{job_id}")
async def get_indexing_job(
    job_id: uuid.UUID,
    organization_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser
):
    """
    Get the detailed status of a specific indexing job.
    """
    await RequireOrganizationRole(OrganizationRole.DEVELOPER)(organization_id, db, current_user)
    
    job = await repository_indexing_service.get_job(db, job_id, organization_id)
    if not job:
        raise HTTPException(status_code=404, detail="Indexing job not found")
        
    return {
        "id": str(job.id),
        "repository_id": str(job.repository_id),
        "status": job.status,
        "model_version": job.model_version,
        "files_indexed": job.files_indexed,
        "symbols_processed": job.symbols_processed,
        "vectors_generated": job.vectors_generated,
        "error": job.error,
        "error_code": job.error_code,
        "started_at": job.started_at,
        "finished_at": job.finished_at,
        "completed_at": job.completed_at,
        "failed_at": job.failed_at,
        "duration_ms": job.duration_ms
    }
