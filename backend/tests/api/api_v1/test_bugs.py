import uuid
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.identity import WorkspaceMember, MemberRole
from app.models.workspace import Workspace
from app.models.organization import Organization
from app.models.bug import Bug, BugState, BugPriority

@pytest.mark.asyncio
async def test_create_bug_authorized(auth_client: AsyncClient, test_workspace: Workspace, test_user):
    response = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs",
        json={"title": "Test Bug", "description": "This is a bug"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Bug"
    assert data["state"] == "OPEN"
    assert data["organization_id"] == str(test_workspace.organization_id)
    assert data["workspace_id"] == str(test_workspace.id)

@pytest.mark.asyncio
async def test_unauthenticated_rejected(async_client: AsyncClient, test_workspace: Workspace):
    response = await async_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs",
        json={"title": "Test Bug"}
    )
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_cross_org_rejected(auth_client: AsyncClient, other_workspace: Workspace):
    # test_user accessing other_workspace (where they are not a member)
    response = await auth_client.post(
        f"/api/v1/workspaces/{other_workspace.id}/bugs",
        json={"title": "Test Bug"}
    )
    assert response.status_code == 403

@pytest.mark.asyncio
async def test_cross_workspace_rejected(auth_client: AsyncClient, other_workspace: Workspace):
    # User belongs to org but not other_workspace
    response = await auth_client.get(f"/api/v1/workspaces/{other_workspace.id}/bugs")
    assert response.status_code == 403

@pytest.mark.asyncio
async def test_client_cannot_forge_tenant(auth_client: AsyncClient, test_workspace: Workspace, other_workspace: Workspace):
    response = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs",
        json={"title": "Forged Tenant Bug", "description": "forged", "organization_id": str(uuid.uuid4()), "workspace_id": str(other_workspace.id)}
    )
    assert response.status_code == 200
    data = response.json()
    # It must ignore the forged IDs and use the path/DB derived ones
    assert data["organization_id"] == str(test_workspace.organization_id)
    assert data["workspace_id"] == str(test_workspace.id)

@pytest.mark.asyncio
async def test_list_excludes_deleted(auth_client: AsyncClient, db: AsyncSession, test_workspace: Workspace, test_user):
    bug1 = Bug(title="Active Bug", description="active", priority=BugPriority.P2, organization_id=test_workspace.organization_id, workspace_id=test_workspace.id, reported_by=test_user.id)
    bug2 = Bug(title="Deleted Bug", description="deleted", priority=BugPriority.P2, organization_id=test_workspace.organization_id, workspace_id=test_workspace.id, reported_by=test_user.id, is_deleted=True)
    db.add_all([bug1, bug2])
    await db.commit()
    
    response = await auth_client.get(f"/api/v1/workspaces/{test_workspace.id}/bugs")
    assert response.status_code == 200
    data = response.json()
    titles = [b["title"] for b in data]
    assert "Active Bug" in titles
    assert "Deleted Bug" not in titles

@pytest.mark.asyncio
async def test_get_deleted_returns_404(auth_client: AsyncClient, db: AsyncSession, test_workspace: Workspace, test_user):
    bug = Bug(title="Deleted Bug", description="deleted", priority=BugPriority.P2, organization_id=test_workspace.organization_id, workspace_id=test_workspace.id, reported_by=test_user.id, is_deleted=True)
    db.add(bug)
    await db.commit()
    
    response = await auth_client.get(f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug.id}")
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_legacy_workspace_rejected(auth_client: AsyncClient, legacy_workspace: Workspace):
    response = await auth_client.post(
        f"/api/v1/workspaces/{legacy_workspace.id}/bugs",
        json={"title": "Test Bug", "description": "desc"}
    )
    assert response.status_code == 400
    assert "migrated to an organization" in response.json()["detail"]

@pytest.mark.asyncio
async def test_valid_state_transition(auth_client: AsyncClient, db: AsyncSession, test_workspace: Workspace, test_user):
    bug = Bug(title="State Bug", description="desc", priority=BugPriority.P2, organization_id=test_workspace.organization_id, workspace_id=test_workspace.id, reported_by=test_user.id, state=BugState.OPEN)
    db.add(bug)
    await db.commit()
    
    response = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug.id}/status",
        json={"state": "IN_PROGRESS"}
    )
    assert response.status_code == 200
    assert response.json()["state"] == "IN_PROGRESS"

@pytest.mark.asyncio
async def test_invalid_state_transition(auth_client: AsyncClient, db: AsyncSession, test_workspace: Workspace, test_user):
    bug = Bug(title="State Bug", description="desc", priority=BugPriority.P2, organization_id=test_workspace.organization_id, workspace_id=test_workspace.id, reported_by=test_user.id, state=BugState.OPEN)
    db.add(bug)
    await db.commit()
    
    response = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug.id}/status",
        json={"state": "VERIFIED"}  # OPEN -> VERIFIED invalid
    )
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_priority_change(auth_client: AsyncClient, db: AsyncSession, test_workspace: Workspace, test_user):
    bug = Bug(title="Prio Bug", description="desc", priority=BugPriority.P2, organization_id=test_workspace.organization_id, workspace_id=test_workspace.id, reported_by=test_user.id)
    db.add(bug)
    await db.commit()
    
    response = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug.id}/priority",
        json={"priority": "P0"}
    )
    assert response.status_code == 200
    assert response.json()["priority"] == "P0"

@pytest.mark.asyncio
async def test_add_comment(auth_client: AsyncClient, db: AsyncSession, test_workspace: Workspace, test_user):
    bug = Bug(title="Comment Bug", description="desc", priority=BugPriority.P2, organization_id=test_workspace.organization_id, workspace_id=test_workspace.id, reported_by=test_user.id)
    db.add(bug)
    await db.commit()
    
    response = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug.id}/comments",
        json={"body": "Hello World"}
    )
    assert response.status_code == 200
    assert response.json()["body"] == "Hello World"

@pytest.mark.asyncio
async def test_soft_delete(auth_client: AsyncClient, db: AsyncSession, test_workspace: Workspace, test_user):
    bug = Bug(title="Delete Bug", description="desc", priority=BugPriority.P2, organization_id=test_workspace.organization_id, workspace_id=test_workspace.id, reported_by=test_user.id)
    db.add(bug)
    await db.commit()
    await db.refresh(bug)
    bug_id = bug.id
    
    response = await auth_client.delete(f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}")
    assert response.status_code == 200
    
    # Assert DB row still exists but is_deleted is true
    db_bug = await db.get(Bug, bug_id)
    assert db_bug is not None
    await db.refresh(db_bug)
    assert db_bug.is_deleted is True

@pytest.mark.asyncio
async def test_list_comments(auth_client: AsyncClient, db: AsyncSession, test_workspace: Workspace, test_user):
    bug = Bug(title="Comment Bug", description="desc", priority=BugPriority.P2, organization_id=test_workspace.organization_id, workspace_id=test_workspace.id, reported_by=test_user.id)
    db.add(bug)
    await db.commit()
    
    await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug.id}/comments",
        json={"body": "Hello World"}
    )
    
    response = await auth_client.get(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug.id}/comments"
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["body"] == "Hello World"

@pytest.mark.asyncio
async def test_get_bug_history(auth_client: AsyncClient, db: AsyncSession, test_workspace: Workspace, test_user):
    # Creating a bug should log BUG_CREATED
    response = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs",
        json={"title": "History Bug", "description": "This is a bug"}
    )
    bug_id = response.json()["id"]

    # Updating status should log STATUS_CHANGED
    await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}/status",
        json={"state": "IN_PROGRESS"}
    )
    
    # Adding comment should log BUG_COMMENTED
    await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}/comments",
        json={"body": "Hello"}
    )
    
    # Check history
    response = await auth_client.get(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}/history"
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 3
    
    actions = [item["action"] for item in data]
    assert "BUG_COMMENTED" in actions
    assert "STATUS_CHANGED" in actions
    assert "BUG_CREATED" in actions
    
    for item in data:
        assert item["bug_id"] == bug_id
