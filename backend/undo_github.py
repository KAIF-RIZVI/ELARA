import asyncio
from sqlalchemy import select, delete
from app.core.database import AsyncSessionLocal
from app.models.organization import Organization
from app.models.integrations import GitHubIntegration

async def undo():
    async with AsyncSessionLocal() as db:
        org = await db.scalar(select(Organization).where(Organization.slug == "meta"))
        if org:
            await db.execute(delete(GitHubIntegration).where(GitHubIntegration.organization_id == org.id))
            await db.commit()
            print("Undo successful")

if __name__ == "__main__":
    asyncio.run(undo())
