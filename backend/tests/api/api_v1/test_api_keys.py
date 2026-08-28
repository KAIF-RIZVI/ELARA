import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.workspace import Workspace, ActivityLog
from app.models.identity import WorkspaceAPIKey
from app.services.api_keys import api_key_service

@pytest.mark.asyncio
async def test_authorized_key_creation(auth_client: AsyncClient, db: AsyncSession, test_workspace: Workspace):
    response = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/api-keys",
        json={"name": "Test Key"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Key"
    assert "raw_key" in data
    assert data["raw_key"].startswith("elara_live_")
    assert "key_hash" not in data

@pytest.mark.asyncio
async def test_unauthorized_user_rejected(other_auth_client: AsyncClient, test_workspace: Workspace):
    # other_auth_client does not belong to test_workspace
    response = await other_auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/api-keys",
        json={"name": "Hacker Key"}
    )
    assert response.status_code in [403, 404]

@pytest.mark.asyncio
async def test_cross_workspace_rejected(other_auth_client: AsyncClient, test_workspace: Workspace):
    response = await other_auth_client.get(f"/api/v1/workspaces/{test_workspace.id}/api-keys")
    assert response.status_code in [403, 404]

@pytest.mark.asyncio
async def test_plaintext_returned_only_creation_not_in_get(auth_client: AsyncClient, db: AsyncSession, test_workspace: Workspace):
    create_resp = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/api-keys",
        json={"name": "Get Test"}
    )
    assert create_resp.status_code == 200
    assert "raw_key" in create_resp.json()

    get_resp = await auth_client.get(f"/api/v1/workspaces/{test_workspace.id}/api-keys")
    assert get_resp.status_code == 200
    keys = get_resp.json()
    assert len(keys) > 0
    for key in keys:
        assert "raw_key" not in key
        assert "key_hash" not in key

@pytest.mark.asyncio
async def test_valid_key_verification_updates_last_used(auth_client: AsyncClient, db: AsyncSession, test_workspace: Workspace):
    create_resp = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/api-keys",
        json={"name": "Verify Key"}
    )
    raw_key = create_resp.json()["raw_key"]

    api_key = await api_key_service.verify_and_get_workspace_for_key(db, raw_key=raw_key)
    assert api_key is not None
    assert api_key.workspace_id == test_workspace.id
    assert api_key.last_used_at is not None

@pytest.mark.asyncio
async def test_invalid_key_rejected(db: AsyncSession):
    api_key = await api_key_service.verify_and_get_workspace_for_key(db, raw_key="elara_live_invalid_key_here")
    assert api_key is None

@pytest.mark.asyncio
async def test_revocation_takes_effect_immediately(auth_client: AsyncClient, db: AsyncSession, test_workspace: Workspace):
    create_resp = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/api-keys",
        json={"name": "Revoke Key"}
    )
    data = create_resp.json()
    raw_key = data["raw_key"]
    key_id = data["id"]

    # Verify works initially
    assert await api_key_service.verify_and_get_workspace_for_key(db, raw_key=raw_key) is not None

    # Revoke
    revoke_resp = await auth_client.delete(f"/api/v1/workspaces/{test_workspace.id}/api-keys/{key_id}")
    assert revoke_resp.status_code == 200
    assert revoke_resp.json()["revoked_at"] is not None

    # Verify fails after revocation
    assert await api_key_service.verify_and_get_workspace_for_key(db, raw_key=raw_key) is None

@pytest.mark.asyncio
async def test_legacy_workspace_rejected(auth_client: AsyncClient, legacy_workspace: Workspace):
    response = await auth_client.post(
        f"/api/v1/workspaces/{legacy_workspace.id}/api-keys",
        json={"name": "Legacy Key"}
    )
    assert response.status_code == 400
    assert "migrated to an organization" in response.json()["detail"]

@pytest.mark.asyncio
async def test_plaintext_key_not_in_logs(auth_client: AsyncClient, db: AsyncSession, test_workspace: Workspace):
    create_resp = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/api-keys",
        json={"name": "Secret Log Key"}
    )
    raw_key = create_resp.json()["raw_key"]

    stmt = select(ActivityLog).where(ActivityLog.target == "Secret Log Key")
    logs = (await db.execute(stmt)).scalars().all()
    assert len(logs) > 0
    for log in logs:
        assert raw_key not in log.action
        assert raw_key not in log.target
