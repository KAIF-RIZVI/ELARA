import asyncio
import sys
import os
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.core.config import get_settings
from app.models.identity import Organization

async def main():
    settings = get_settings()
    engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI)
    
    async with engine.connect() as conn:
        res = await conn.execute(select(Organization.id, Organization.name))
        orgs = res.fetchall()
        for o in orgs:
            print(f"Org: {o.id}, Name: {o.name}")

if __name__ == "__main__":
    asyncio.run(main())
