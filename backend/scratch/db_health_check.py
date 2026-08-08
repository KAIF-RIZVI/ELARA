import asyncio
from sqlalchemy import text
from app.core.database import engine

async def check_db_health():
    try:
        async with engine.connect() as conn:
            # 1. Connection check
            result = await conn.execute(text("SELECT 1"))
            print("Database Connection: SUCCESS")
            
            # 2. Check Alembic version
            try:
                version = await conn.execute(text("SELECT version_num FROM alembic_version"))
                print(f"Current Alembic Migration Version: {version.scalar()}")
            except Exception as e:
                print("Alembic Version Table: NOT FOUND or ERROR")
            
            # 3. List all tables
            tables_result = await conn.execute(
                text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
            )
            tables = [row[0] for row in tables_result]
            print("\n--- Tables Overview ---")
            
            for table in sorted(tables):
                count = await conn.execute(text(f"SELECT COUNT(*) FROM {table}"))
                print(f"Table: {table:<25} Rows: {count.scalar()}")

    except Exception as e:
        print(f"Database Connection: FAILED\n{e}")

if __name__ == "__main__":
    asyncio.run(check_db_health())
