import asyncio
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.database import AsyncSessionLocal
from app.models.project import Project, Repository, RepoIndexJob
from app.models.organization import Organization
from sqlalchemy import select

async def check_db():
    print("Checking Database ORM configuration and connectivity...")
    try:
        async with AsyncSessionLocal() as db:
            orgs = await db.execute(select(Organization).limit(1))
            print("Organizations queried successfully.")
            
            repos = await db.execute(select(Repository).limit(1))
            print("Repositories queried successfully.")
            
            jobs = await db.execute(select(RepoIndexJob).limit(1))
            print("RepoIndexJobs queried successfully.")
            
            print("✅ Database verification passed.")
    except Exception as e:
        print(f"❌ Database verification failed: {e}")

if __name__ == "__main__":
    asyncio.run(check_db())
