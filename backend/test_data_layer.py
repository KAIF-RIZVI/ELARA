import asyncio
import uuid
import unittest
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy import select
from app.core.base_model import Base
from app.models.workspace import Workspace, WorkspaceStatus
from app.models.organization import Organization, OrganizationMember, OrganizationRole
from app.models.identity import User, WorkspaceAPIKey, MemberRole
from app.models.bug import Bug, BugSource
from app.services.workspace import workspace_service
from app.schemas.workspace import WorkspaceCreate

class TestDataLayer(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
        self.TestingSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def asyncTearDown(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    async def test_legacy_workspaces_untouched(self):
        # Legacy workspace created before the migration has no organization_id
        async with self.TestingSessionLocal() as db:
            legacy_ws = Workspace(
                name="Legacy WS",
                slug="legacy-ws",
                organization_id=None,
                status=WorkspaceStatus.ACTIVE
            )
            db.add(legacy_ws)
            await db.commit()
            
            # Verify it persists perfectly without an org_id
            result = await db.execute(select(Workspace).where(Workspace.slug == "legacy-ws"))
            fetched_ws = result.scalar_one()
            self.assertIsNone(fetched_ws.organization_id)
            self.assertEqual(fetched_ws.name, "Legacy WS")

    async def test_new_workspace_requires_organization(self):
        async with self.TestingSessionLocal() as db:
            user = User(email="test@test.com", full_name="Test")
            db.add(user)
            await db.commit()
            
            # Test 1: Service layer requires organization_id
            # We attempt to pass an invalid org
            bad_org_id = uuid.uuid4()
            
            with self.assertRaisesRegex(ValueError, "User does not belong to the specified organization"):
                await workspace_service.create_workspace(
                    db,
                    name="New WS",
                    slug="new-ws",
                    user_id=user.id,
                    organization_id=bad_org_id
                )

    async def test_workspace_organization_membership(self):
        async with self.TestingSessionLocal() as db:
            user = User(email="test2@test.com", full_name="Test2")
            org1 = Organization(name="Org 1", slug="org-1")
            org2 = Organization(name="Org 2", slug="org-2")
            db.add_all([user, org1, org2])
            await db.commit()
            
            # User belongs only to Org 1
            org1_member = OrganizationMember(
                organization_id=org1.id,
                user_id=user.id,
                role=OrganizationRole.MEMBER
            )
            db.add(org1_member)
            await db.commit()
            
            # Succeeds creating in Org 1
            ws = await workspace_service.create_workspace(
                db,
                name="WS 1",
                slug="ws-1",
                user_id=user.id,
                organization_id=org1.id
            )
            self.assertEqual(ws.organization_id, org1.id)
            
            # Fails creating in Org 2 (doesn't belong)
            with self.assertRaisesRegex(ValueError, "User does not belong to the specified organization"):
                await workspace_service.create_workspace(
                    db,
                    name="WS 2",
                    slug="ws-2",
                    user_id=user.id,
                    organization_id=org2.id
                )

    async def test_bug_creation_requires_valid_ownership(self):
        async with self.TestingSessionLocal() as db:
            # DB constraints (organization_id and workspace_id are NOT NULL)
            bug = Bug(
                title="Test Bug",
                description="Fails because org and ws are missing",
                source=BugSource.MANUAL
            )
            db.add(bug)
            
            import sqlalchemy.exc
            with self.assertRaises(sqlalchemy.exc.IntegrityError):
                await db.commit()
                
    async def test_workspace_api_keys_cross_boundary(self):
        async with self.TestingSessionLocal() as db:
            # DB constraints for workspace API key requires BOTH org and ws
            key = WorkspaceAPIKey(
                key_hash="hash",
                name="Test Key",
                prefix="test_"
            )
            db.add(key)
            import sqlalchemy.exc
            with self.assertRaises(sqlalchemy.exc.IntegrityError):
                await db.commit()

if __name__ == '__main__':
    unittest.main()
