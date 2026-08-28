import asyncio
import sys
import os
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.core.config import get_settings
from app.models.project import RepoIndexJob, Repository

async def main():
    settings = get_settings()
    engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI)
    
    async with engine.connect() as conn:
        res = await conn.execute(select(RepoIndexJob.id, RepoIndexJob.repository_id, RepoIndexJob.status, RepoIndexJob.error_message))
        jobs = res.fetchall()
        for job in jobs:
            print(f"Job: {job.id}, Repo: {job.repository_id}, Status: {job.status}, Error: {job.error_message}")
            
        res = await conn.execute(select(Repository.id, Repository.name, Repository.index_status))
        repos = res.fetchall()
        for repo in repos:
            print(f"Repo: {repo.name}, Status: {repo.index_status}")

if __name__ == "__main__":
    asyncio.run(main())
