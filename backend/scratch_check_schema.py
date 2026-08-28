import asyncio
from sqlalchemy import text
from app.api.deps import get_db
from app.core.config import get_settings
from sqlalchemy.ext.asyncio import create_async_engine

settings = get_settings()
engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI, echo=False)

async def check_schema():
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT column_name, data_type, is_nullable FROM information_schema.columns WHERE table_name = 'activity_logs';"))
        columns = result.fetchall()
        for col in columns:
            print(col)

asyncio.run(check_schema())
