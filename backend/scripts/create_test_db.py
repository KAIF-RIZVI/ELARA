import asyncio
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv(".env")

async def main():
    user = os.environ.get("POSTGRES_USER", "postgres")
    password = os.environ.get("POSTGRES_PASSWORD", "YOUR_PASSWORD")
    host = os.environ.get("POSTGRES_HOST", "localhost")
    port = os.environ.get("POSTGRES_PORT", "5432")
    
    conn = await asyncpg.connect(user=user, password=password, host=host, port=port, database="postgres")
    
    # Check if database exists
    exists = await conn.fetchval("SELECT 1 FROM pg_database WHERE datname='elara_test'")
    if not exists:
        print("Creating elara_test database...")
        await conn.execute("CREATE DATABASE elara_test")
    else:
        print("elara_test already exists")
    
    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())
