import asyncio
import asyncpg
from app.core.config import get_settings

async def wipe_db():
    settings = get_settings()
    # Replace +asyncpg from the connection string for asyncpg.connect
    dsn = settings.SQLALCHEMY_DATABASE_URI.replace("+asyncpg", "")
    
    conn = await asyncpg.connect(dsn)
    try:
        print("Dropping public schema...")
        await conn.execute("DROP SCHEMA public CASCADE;")
        print("Recreating public schema...")
        await conn.execute("CREATE SCHEMA public;")
        print("Database wiped successfully!")
    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(wipe_db())
