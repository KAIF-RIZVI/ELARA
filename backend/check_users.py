import asyncio
from app.db.session import async_session_maker
from app.repositories.user import user as user_repo

async def main():
    async with async_session_maker() as db:
        users = await user_repo.get_multi(db, skip=0, limit=100)
        print("Registered Emails:", [u.email for u in users])

if __name__ == "__main__":
    asyncio.run(main())
