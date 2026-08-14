import asyncio
from sqlalchemy import select
from app.core.database import AsyncSessionLocal
from app.models.identity import User
from app.models.organization import OrganizationMember

async def check():
    async with AsyncSessionLocal() as session:
        users = await session.execute(select(User))
        for u in users.scalars().all():
            print(f"User: {u.email}, {u.full_name}, {u.id}")
            mems = await session.execute(select(OrganizationMember).where(OrganizationMember.user_id == u.id))
            for m in mems.scalars().all():
                print(f"  OrgMember: Org {m.organization_id}, Role {m.role}")

if __name__ == "__main__":
    asyncio.run(check())
