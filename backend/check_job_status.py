import asyncio
from app.core.database import AsyncSessionLocal
from app.models.project import RepoIndexJob
from sqlalchemy import select

async def run():
    db = AsyncSessionLocal()
    jobs = await db.execute(select(RepoIndexJob))
    for j in jobs.scalars().all():
        print(f"Job {j.id}: {j.status}")
    await db.close()

asyncio.run(run())
