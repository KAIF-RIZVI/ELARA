import asyncio
import sys
import os
from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.core.config import get_settings
from app.models.identity import User

async def main():
    settings = get_settings()
    engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI)
    
    async with engine.connect() as conn:
        res = await conn.execute(select(User.email, User.avatar_url))
        users = res.fetchall()
        for u in users:
            print(f"User: {u.email}, Avatar: {u.avatar_url}")

if __name__ == "__main__":
    asyncio.run(main())
