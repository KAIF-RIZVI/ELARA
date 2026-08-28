import asyncio
import sys
import os
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.core.config import get_settings
from app.models.project import RepoIndexJob
from app.worker.tasks.repo_tasks import index_repository_job

async def main():
    settings = get_settings()
    engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI)
    
    async with engine.connect() as conn:
        res = await conn.execute(select(RepoIndexJob).where(RepoIndexJob.status == "QUEUED"))
        jobs = res.fetchall()
        for job in jobs:
            print(f"Re-queueing job {job.id} for repo {job.repository_id}")
            index_repository_job.delay(str(job.id), str(job.organization_id))

if __name__ == "__main__":
    asyncio.run(main())
