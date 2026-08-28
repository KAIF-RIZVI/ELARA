import uuid
from typing import Optional
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_
from fastapi import HTTPException, status
from app.models.project import RepoIndexJob, JobStatus, Repository
from app.core.config import get_settings

settings = get_settings()

class RepositoryIndexingService:
    async def get_job(self, db: AsyncSession, job_id: uuid.UUID, organization_id: uuid.UUID) -> Optional[RepoIndexJob]:
        stmt = select(RepoIndexJob).where(
            and_(
                RepoIndexJob.id == job_id,
                RepoIndexJob.organization_id == organization_id
            )
        )
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    async def get_active_job_for_repository(self, db: AsyncSession, repository_id: uuid.UUID) -> Optional[RepoIndexJob]:
        active_states = [
            JobStatus.QUEUED, JobStatus.CLONING, JobStatus.PARSING, 
            JobStatus.ANALYZING, JobStatus.EMBEDDING, JobStatus.STORING
        ]
        stmt = select(RepoIndexJob).where(
            and_(
                RepoIndexJob.repository_id == repository_id,
                RepoIndexJob.status.in_(active_states)
            )
        )
        result = await db.execute(stmt)
        return result.scalar_one_or_none()

    async def create_indexing_job(self, db: AsyncSession, organization_id: uuid.UUID, repository_id: uuid.UUID) -> RepoIndexJob:
        # 1. Verify Repository Ownership
        stmt = select(Repository).where(
            and_(Repository.id == repository_id, Repository.organization_id == organization_id)
        )
        result = await db.execute(stmt)
        repo = result.scalar_one_or_none()
        if not repo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Repository not found or not owned by this organization.")

        # 2. Prevent Duplicate Jobs
        existing_job = await self.get_active_job_for_repository(db, repository_id)
        if existing_job:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="An active indexing job already exists for this repository.")

        # 3. Check Organization Concurrency
        active_states = [JobStatus.QUEUED, JobStatus.CLONING, JobStatus.PARSING, JobStatus.ANALYZING, JobStatus.EMBEDDING, JobStatus.STORING]
        org_jobs_stmt = select(RepoIndexJob).where(
            and_(RepoIndexJob.organization_id == organization_id, RepoIndexJob.status.in_(active_states))
        )
        org_jobs_result = await db.execute(org_jobs_stmt)
        active_org_jobs = len(org_jobs_result.scalars().all())
        
        max_org_jobs = getattr(settings, "INDEXING_MAX_CONCURRENT_PER_ORG", 1)
        if active_org_jobs >= max_org_jobs:
            raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail=f"Organization has reached its concurrent indexing limit ({max_org_jobs}).")

        # 4. Create Job
        job = RepoIndexJob(
            repository_id=repository_id,
            organization_id=organization_id,
            status=JobStatus.QUEUED,
            commit_sha="PENDING",
            model_version=getattr(settings, "CODE_EMBEDDING_MODEL", "microsoft/graphcodebert-base")
        )
        db.add(job)
        await db.commit()
        await db.refresh(job)
        return job

    async def update_job_status(self, db: AsyncSession, job_id: uuid.UUID, new_status: JobStatus, error: str = None, error_code: str = None) -> Optional[RepoIndexJob]:
        stmt = select(RepoIndexJob).where(RepoIndexJob.id == job_id)
        result = await db.execute(stmt)
        job = result.scalar_one_or_none()
        if not job:
            return None

        # Basic State Machine Validation
        valid_transitions = {
            JobStatus.QUEUED: [JobStatus.CLONING, JobStatus.FAILED, JobStatus.CANCELLED],
            JobStatus.CLONING: [JobStatus.PARSING, JobStatus.FAILED, JobStatus.CANCELLED],
            JobStatus.PARSING: [JobStatus.ANALYZING, JobStatus.FAILED, JobStatus.CANCELLED],
            JobStatus.ANALYZING: [JobStatus.EMBEDDING, JobStatus.FAILED, JobStatus.CANCELLED],
            JobStatus.EMBEDDING: [JobStatus.STORING, JobStatus.FAILED, JobStatus.CANCELLED],
            JobStatus.STORING: [JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED],
            JobStatus.COMPLETED: [],
            JobStatus.FAILED: [],
            JobStatus.CANCELLED: []
        }

        if new_status not in valid_transitions.get(job.status, []):
            pass # Soft enforcement to handle race conditions where job is cancelled during transition.

        job.status = new_status
        if new_status == JobStatus.CLONING:
            job.started_at = datetime.now(timezone.utc)
        elif new_status == JobStatus.COMPLETED:
            job.completed_at = datetime.now(timezone.utc)
            if job.started_at:
                job.duration_ms = int((job.completed_at - job.started_at).total_seconds() * 1000)
        elif new_status == JobStatus.FAILED:
            job.failed_at = datetime.now(timezone.utc)
            job.error = error
            job.error_code = error_code
            if job.started_at:
                job.duration_ms = int((job.failed_at - job.started_at).total_seconds() * 1000)

        await db.commit()
        await db.refresh(job)
        return job

    async def cancel_job(self, db: AsyncSession, job_id: uuid.UUID, organization_id: uuid.UUID) -> RepoIndexJob:
        job = await self.get_job(db, job_id, organization_id)
        if not job:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found.")

        if job.status in [JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Job cannot be cancelled in its current state.")

        job.status = JobStatus.CANCELLED
        await db.commit()
        await db.refresh(job)
        return job

repository_indexing_service = RepositoryIndexingService()
