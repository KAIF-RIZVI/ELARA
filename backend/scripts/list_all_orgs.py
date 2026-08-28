import asyncio
from sqlalchemy import select
from app.core.database import AsyncSessionLocal
from app.models.organization import Organization, OrganizationMember
from app.models.identity import User

async def check():
    async with AsyncSessionLocal() as db:
        user = (await db.execute(select(User).limit(1))).scalar_one_or_none()
        print("User:", user.id)
        
        all_orgs = (await db.execute(select(Organization))).scalars().all()
        print(f"Total organizations in DB: {len(all_orgs)}")
        for org in all_orgs:
            print(f"- {org.name} (id: {org.id}, owner_id: {org.owner_id})")

        all_memberships = (await db.execute(select(OrganizationMember))).scalars().all()
        print(f"\nTotal memberships in DB: {len(all_memberships)}")
        for m in all_memberships:
            print(f"- user: {m.user_id}, org: {m.organization_id}, role: {m.role}, status: {m.status}")

if __name__ == "__main__":
    asyncio.run(check())
