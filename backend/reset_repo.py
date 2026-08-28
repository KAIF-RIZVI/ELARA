import asyncio
from app.core.database import AsyncSessionLocal
from app.models.project import Repository, SyncStatus
from sqlalchemy import select

async def reset_repo():
    async with AsyncSessionLocal() as session:
        repos = (await session.execute(select(Repository).where(Repository.full_name == 'KAIF-RIZVI/NARI-PRODUCTION'))).scalars().all()
        if repos:
            for repo in repos:
                print(f'Found repo: {repo.id}, status: {repo.sync_status}')
                if repo.sync_status == SyncStatus.SYNCING:
                    repo.sync_status = SyncStatus.PENDING
            await session.commit()
            print('Reset statuses to PENDING')
        else:
            print('Repo not found')

if __name__ == "__main__":
    asyncio.run(reset_repo())
