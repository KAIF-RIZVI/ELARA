import asyncio
from app.core.database import AsyncSessionLocal
from app.models.organization import OrganizationAuditLog
from sqlalchemy import select

async def run():
    async with AsyncSessionLocal() as db:
        res = await db.execute(select(OrganizationAuditLog.event_type).distinct())
        print(res.scalars().all())

asyncio.run(run())
