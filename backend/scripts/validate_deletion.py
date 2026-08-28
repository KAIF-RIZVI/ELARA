import asyncio
from app.core.database import AsyncSessionLocal
from app.models.organization import Organization, OrganizationStatus, OrganizationRole, OrganizationMember
from app.models.user import User
from app.ai.vector_store import vector_store
from sqlalchemy import select
import uuid
import sys

async def validate():
    async with AsyncSessionLocal() as db:
        # 1. Create a dummy organization and user
        user_id = uuid.uuid4()
        org_id = uuid.uuid4()
        
        user = User(id=user_id, email=f"test_{user_id}@example.com", full_name="Test User", hashed_password="pw")
        db.add(user)
        
        org = Organization(id=org_id, name="Test Deletion Org", slug=f"test-del-{org_id}")
        db.add(org)
        
        member = OrganizationMember(organization_id=org_id, user_id=user_id, role=OrganizationRole.OWNER)
        db.add(member)
        
        await db.commit()
        
        print(f"Created org: {org.id}")
        
        # Insert dummy vectors
        vector_store.upsert_vectors(str(org_id), str(uuid.uuid4()), [
            {"id": str(uuid.uuid4()), "vector": [0.1]*768, "payload": {"organization_id": str(org_id), "chunk_id": "test"}}
        ])
        print("Inserted dummy vectors.")
        
        # Test transition to DELETING
        org = await db.scalar(select(Organization).where(Organization.id == org_id))
        org.status = OrganizationStatus.DELETING
        await db.commit()
        print("Transitioned to DELETING.")
        
        # Run Qdrant deletion
        vector_store.delete_organization_vectors(str(org_id))
        print("Deleted Qdrant vectors.")
        
        # Postgres deletion
        await db.delete(org)
        await db.commit()
        print("Deleted Postgres organization.")
        
        org_check = await db.scalar(select(Organization).where(Organization.id == org_id))
        if org_check:
            print("ERROR: Postgres org still exists!")
            sys.exit(1)
        else:
            print("SUCCESS: Postgres org deleted successfully.")

if __name__ == "__main__":
    asyncio.run(validate())
