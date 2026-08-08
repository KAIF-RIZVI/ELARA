import asyncio
import asyncpg
from app.core.config import get_settings

async def reset_db():
    settings = get_settings()
    uri = settings.SQLALCHEMY_DATABASE_URI.replace("+asyncpg", "")
    print(f"Connecting to {uri}")
    conn = await asyncpg.connect(uri)
    await conn.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")
    await conn.close()
    print("Database wiped clean!")

if __name__ == "__main__":
    asyncio.run(reset_db())