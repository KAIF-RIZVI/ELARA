import asyncio
import httpx
from app.core.database import AsyncSessionLocal
from app.models.identity import User
from sqlalchemy import select
from app.core.security import create_access_token
import uuid

async def test_me():
    async with AsyncSessionLocal() as db:
        user = (await db.execute(select(User).limit(1))).scalar_one_or_none()
        if not user:
            print("No user")
            return
            
        token = create_access_token(user.id, session_id=uuid.uuid4())
        
    async with httpx.AsyncClient(base_url="http://localhost:8000/api/v1") as client:
        res = await client.get(
            "/organizations/me",
            headers={"Authorization": f"Bearer {token}"}
        )
        print("Status:", res.status_code)
        import json
        print(json.dumps(res.json(), indent=2))

if __name__ == "__main__":
    asyncio.run(test_me())
