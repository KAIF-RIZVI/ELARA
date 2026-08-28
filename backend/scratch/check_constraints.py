import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

async def main():
    engine = create_async_engine("postgresql+asyncpg://postgres:Kaifrizvi%400708@localhost:5432/elara")
    async with engine.connect() as conn:
        result = await conn.execute(text("""
            SELECT conname
            FROM pg_constraint
            WHERE conrelid = 'idempotency_keys'::regclass
            AND contype = 'u';
        """))
        constraints = result.fetchall()
        print("Unique Constraints:", constraints)

asyncio.run(main())
