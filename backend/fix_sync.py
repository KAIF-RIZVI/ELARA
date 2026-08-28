import asyncio
import sys
import os
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import create_async_engine

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.core.config import get_settings
from app.models.project import Repository, SyncStatus

async def main():
    settings = get_settings()
    engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI)
    
    async with engine.connect() as conn:
        await conn.execute(update(Repository).where(Repository.full_name == "KAIF-RIZVI/NARI-PRODUCTION").values(sync_status=SyncStatus.COMPLETED))
        await conn.commit()
        print("Updated NARI-PRODUCTION sync_status to COMPLETED.")

if __name__ == "__main__":
    asyncio.run(main())
