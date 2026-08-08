import asyncio
from app.core.database import get_db
from app.repositories.user import user as user_repo

async def test():
    async for db in get_db():
        users = await user_repo.get_multi(db, limit=100)
        for u in users:
            print(f"User: {u.email} (Verified: {u.email_verified})")
        break

if __name__ == "__main__":
    asyncio.run(test())
