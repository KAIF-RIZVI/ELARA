import asyncio
import sys
import os
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import create_async_engine

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.core.config import get_settings
from app.models.project import Repository, RepoIndexJob, JobStatus

import uuid

async def main():
    settings = get_settings()
    engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI)
    
    async with engine.connect() as conn:
        result = await conn.execute(select(Repository.id, Repository.organization_id).where(Repository.full_name.like("%NARI-PRODUCTION%")))
        row = result.fetchone()
        if not row:
            print("Repository NARI-PRODUCTION not found!")
            return
            
        repo_id = str(row[0])
        org_id = str(row[1])
        
        # Mark all existing jobs for this repo as cancelled
        await conn.execute(update(RepoIndexJob).where(RepoIndexJob.repository_id == repo_id).values(status=JobStatus.CANCELLED))
        
        print(f"Creating new job for repo {repo_id}")
        job_id = uuid.uuid4()
        await conn.execute(
            RepoIndexJob.__table__.insert().values(
                id=job_id,
                repository_id=repo_id,
                organization_id=org_id,
                status=JobStatus.QUEUED,
                commit_sha="PENDING",
                model_version="microsoft/graphcodebert-base",
                files_indexed=0,
                symbols_processed=0,
                vectors_generated=0
            )
        )
        await conn.commit()
        
        from app.worker.celery_app import celery_app
        celery_app.send_task("index_repository_job", kwargs={"job_id_str": str(job_id), "organization_id_str": str(org_id)})
        
        print("Done. Sent task to Celery.")

if __name__ == "__main__":
    asyncio.run(main())
