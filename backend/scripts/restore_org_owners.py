import asyncio
from sqlalchemy import select
from app.core.database import AsyncSessionLocal
from app.models.organization import Organization, OrganizationMember, OrganizationRole
from app.models.identity import User

async def restore():
    async with AsyncSessionLocal() as db:
        user = (await db.execute(select(User).limit(1))).scalar_one_or_none()
        print("User:", user.id)
        
        # Find all orgs owned by user
        stmt = select(Organization).where(Organization.owner_id == user.id)
        orgs = (await db.execute(stmt)).scalars().all()
        
        for org in orgs:
            # Check if user is a member
            stmt = select(OrganizationMember).where(
                OrganizationMember.organization_id == org.id,
                OrganizationMember.user_id == user.id
            )
            member = (await db.execute(stmt)).scalar_one_or_none()
            
            if not member:
                print(f"Restoring membership for {org.name}")
                new_member = OrganizationMember(
                    organization_id=org.id,
                    user_id=user.id,
                    role=OrganizationRole.OWNER,
                    status="ACTIVE"
                )
                db.add(new_member)
        
        await db.commit()
        print("Done.")

if __name__ == "__main__":
    asyncio.run(restore())
