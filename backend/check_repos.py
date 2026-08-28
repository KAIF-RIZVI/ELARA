import asyncio
import sys
import os
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.core.config import get_settings
from app.models.project import Repository

async def main():
    settings = get_settings()
    engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI)
    
    async with engine.connect() as conn:
        res = await conn.execute(select(Repository.id, Repository.organization_id, Repository.workspace_id, Repository.full_name))
        repos = res.fetchall()
        for r in repos:
            print(f"Repo: {r.id}, Org: {r.organization_id}, Workspace: {r.workspace_id}, Name: {r.full_name}")

if __name__ == "__main__":
    asyncio.run(main())
