import pytest
import uuid
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.organization import Organization, OrganizationMember, OrganizationRole
from app.models.workspace import Workspace
from app.models.bug import Bug

@pytest.mark.asyncio
async def test_org_member_can_list_bugs(auth_client: AsyncClient, test_workspace: Workspace, db: AsyncSession):
    # Create two bugs in the test workspace
    bug1 = Bug(
        organization_id=test_workspace.organization_id,
        workspace_id=test_workspace.id,
        title="Org Bug 1",
        description="Test",
        status="OPEN",
        severity="MEDIUM"
    )
    bug2 = Bug(
        organization_id=test_workspace.organization_id,
        workspace_id=test_workspace.id,
        title="Org Bug 2",
        description="Test",
        status="OPEN",
        severity="MEDIUM"
    )
    db.add_all([bug1, bug2])
    await db.commit()
    
    response = await auth_client.get(f"/api/v1/organizations/{test_workspace.organization_id}/bugs")
    assert response.status_code == 200
    data = response.json()
    
    assert len(data) >= 2
    titles = [b["title"] for b in data]
    assert "Org Bug 1" in titles
    assert "Org Bug 2" in titles
    
    # Verify workspace_id is included
    for b in data:
        assert "workspace_id" in b
        assert b["workspace_id"] is not None

@pytest.mark.asyncio
async def test_cross_org_leakage_prevented(auth_client: AsyncClient, test_workspace: Workspace, db: AsyncSession):
    # This user is authorized for test_workspace's organization.
    # Let's create a completely separate organization and bug.
    other_org = Organization(name="Other Org", slug=f"other-{uuid.uuid4().hex[:8]}")
    db.add(other_org)
    await db.commit()
    await db.refresh(other_org)
    
    other_ws = Workspace(organization_id=other_org.id, name="Other WS", slug=f"ws-{uuid.uuid4().hex[:8]}")
    db.add(other_ws)
    await db.commit()
    await db.refresh(other_ws)
    
    other_bug = Bug(
        organization_id=other_org.id,
        workspace_id=other_ws.id,
        title="Secret Bug",
        description="Test",
        status="OPEN",
        severity="MEDIUM"
    )
    db.add(other_bug)
    await db.commit()
    
    # 1. User should NOT see this bug when querying their own organization
    response = await auth_client.get(f"/api/v1/organizations/{test_workspace.organization_id}/bugs")
    assert response.status_code == 200
    data = response.json()
    titles = [b["title"] for b in data]
    assert "Secret Bug" not in titles
    
    # 2. User should get 403 when trying to query the other organization's bugs directly
    response2 = await auth_client.get(f"/api/v1/organizations/{other_org.id}/bugs")
    assert response2.status_code == 403

@pytest.mark.asyncio
async def test_soft_deleted_bugs_excluded(auth_client: AsyncClient, test_workspace: Workspace, db: AsyncSession):
    active_bug = Bug(
        organization_id=test_workspace.organization_id,
        workspace_id=test_workspace.id,
        title="Active Bug",
        description="Test",
        status="OPEN",
        severity="MEDIUM",
        is_deleted=False
    )
    deleted_bug = Bug(
        organization_id=test_workspace.organization_id,
        workspace_id=test_workspace.id,
        title="Deleted Bug",
        description="Test",
        status="OPEN",
        severity="MEDIUM",
        is_deleted=True
    )
    db.add_all([active_bug, deleted_bug])
    await db.commit()
    
    response = await auth_client.get(f"/api/v1/organizations/{test_workspace.organization_id}/bugs")
    assert response.status_code == 200
    data = response.json()
    titles = [b["title"] for b in data]
    assert "Active Bug" in titles
    assert "Deleted Bug" not in titles

@pytest.mark.asyncio
async def test_unauthenticated_receives_401(async_client: AsyncClient, test_workspace: Workspace):
    # Using async_client which does not have the authorization header attached
    response = await async_client.get(f"/api/v1/organizations/{test_workspace.organization_id}/bugs")
    assert response.status_code == 401
