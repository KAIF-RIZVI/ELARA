import asyncio
import asyncpg
from app.core.config import get_settings

async def verify_schema():
    settings = get_settings()
    dsn = settings.SQLALCHEMY_DATABASE_URI.replace("+asyncpg", "")
    
    conn = await asyncpg.connect(dsn)
    try:
        # Get all tables in the public schema
        tables = await conn.fetch('''
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name;
        ''')
        
        print("--- DATABASE TABLES ---")
        for table in tables:
            print(f"- {table['table_name']}")
            
            # Print a few key columns to verify completeness
            if table['table_name'] in ('users', 'workspaces', 'subscriptions'):
                columns = await conn.fetch(f'''
                    SELECT column_name, data_type
                    FROM information_schema.columns
                    WHERE table_name = '{table['table_name']}'
                ''')
                cols = [c['column_name'] for c in columns]
                print(f"  Columns: {', '.join(cols[:5])} ... ({len(cols)} total)")
        
        print("\n--- ALEMBIC VERSION ---")
        version = await conn.fetchval('SELECT version_num FROM alembic_version')
        print(f"Current Head: {version}")
        
    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(verify_schema())
