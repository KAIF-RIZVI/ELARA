import asyncio
import sys
import os
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.core.config import get_settings
from app.models.integrations import GitHubIntegration

async def main():
    settings = get_settings()
    engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI)
    
    async with engine.connect() as conn:
        res = await conn.execute(select(GitHubIntegration.id, GitHubIntegration.organization_id, GitHubIntegration.status, GitHubIntegration.github_installation_id))
        ints = res.fetchall()
        for i in ints:
            print(f"Integration: {i.id}, Org: {i.organization_id}, Status: {i.status}, Install_ID: {i.github_installation_id}")

if __name__ == "__main__":
    asyncio.run(main())
