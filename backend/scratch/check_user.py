import asyncio
from sqlalchemy import select
from app.core.database import AsyncSessionLocal
from app.models.identity import User

async def main():
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(User))
        users = result.scalars().all()
        for u in users:
            print(f"Email: {u.email} | Name: {u.full_name} | Avatar: {u.avatar_url}")

if __name__ == "__main__":
    asyncio.run(main())
