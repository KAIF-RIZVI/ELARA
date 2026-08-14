import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from app.core.database import AsyncSessionLocal
from app.services.organization_dashboard import organization_dashboard_service
from app.models.organization import Organization, OrganizationMember

async def test():
    async with AsyncSessionLocal() as session:
        orgs_result = await session.execute(select(Organization))
        orgs = orgs_result.scalars().all()
        for o in orgs:
            print(f"Org: {o.name} - {o.slug} - {o.id}")
        org = orgs[0] if orgs else None
        if not org:
            return
            
        mem_result = await session.execute(select(OrganizationMember).where(OrganizationMember.organization_id == org.id).limit(1))
        mem = mem_result.scalar_one_or_none()
        if not mem:
            print("No member")
            return
            
        print("Testing with org", org.id, "and user", mem.user_id)
        try:
            data = await organization_dashboard_service.get_dashboard_data(session, org.id, mem.user_id)
            print("SERVICE RETURNED SUCCESSFULLY")
            
            # validate using pydantic
            from app.schemas.dashboard import OrganizationDashboardResponse
            obj = OrganizationDashboardResponse(**data)
            print("PYDANTIC VALIDATION SUCCESS")
        except Exception as e:
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test())
