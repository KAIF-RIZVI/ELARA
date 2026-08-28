import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

async def main():
    engine = create_async_engine("postgresql+asyncpg://postgres:Kaifrizvi%400708@localhost:5432/elara")
    async with engine.connect() as conn:
        result = await conn.execute(text("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public' AND table_name = 'idempotency_keys';
        """))
        table = result.fetchone()
        if table:
            print("TABLE EXISTS")
        else:
            print("TABLE DOES NOT EXIST")

asyncio.run(main())
