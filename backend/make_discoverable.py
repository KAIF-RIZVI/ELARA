import asyncio
from app.core.database import AsyncSessionLocal
from sqlalchemy import update
from app.models.organization import Organization, JoinPolicy

async def main():
    async with AsyncSessionLocal() as db:
        await db.execute(update(Organization).values(discoverable=True, join_policy=JoinPolicy.REQUEST_TO_JOIN))
        await db.commit()
        print('Successfully updated all organizations to be discoverable and open to join requests.')

if __name__ == "__main__":
    asyncio.run(main())
