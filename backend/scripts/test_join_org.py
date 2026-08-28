import asyncio
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.database import AsyncSessionLocal
from app.models.organization import Organization, OrganizationMember
from app.models.identity import User
from app.core.security import create_access_token
import httpx
from sqlalchemy import select

async def check_db():
    print("Testing create_join_request via HTTP API...")
    try:
        async with AsyncSessionLocal() as db:
            org = await db.execute(select(Organization).limit(1))
            org = org.scalar_one_or_none()
            if not org:
                print("No org found.")
                return
            
            user = await db.execute(select(User).limit(1))
            user = user.scalar_one_or_none()
            if not user:
                print("No user found.")
                return
                
            org.discoverable = True
            org.join_policy = "OPEN"
            await db.execute(OrganizationMember.__table__.delete().where(
                OrganizationMember.organization_id == org.id,
                OrganizationMember.user_id == user.id
            ))
            from app.models.organization import OrganizationJoinRequest
            await db.execute(OrganizationJoinRequest.__table__.delete().where(
                OrganizationJoinRequest.organization_id == org.id,
                OrganizationJoinRequest.user_id == user.id
            ))
            await db.commit()
            
            import uuid
            access_token = create_access_token(user.id, session_id=uuid.uuid4())
            
            # Hit API
            async with httpx.AsyncClient() as client:
                res = await client.post(
                    f"http://localhost:8000/api/v1/organizations/{org.id}/join-request",
                    json={"message": "Let me in please via API"},
                    headers={"Authorization": f"Bearer {access_token}"}
                )
                print("Status:", res.status_code)
                print("Response:", res.text)
                
    except Exception as e:
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(check_db())
