import asyncio
from sqlalchemy import select
from app.core.database import AsyncSessionLocal
from app.models.organization import Organization, OrganizationMember
from app.models.identity import User

async def check():
    async with AsyncSessionLocal() as db:
        user = (await db.execute(select(User).limit(1))).scalar_one_or_none()
        print("User:", user.id)
        
        members = (await db.execute(select(OrganizationMember).where(OrganizationMember.user_id == user.id))).scalars().all()
        print("Memberships:", len(members))
        for m in members:
            org = (await db.execute(select(Organization).where(Organization.id == m.organization_id))).scalar_one()
            print(f"Org: {org.name} - Role: {m.role} - Status: {m.status}")

if __name__ == "__main__":
    asyncio.run(check())
