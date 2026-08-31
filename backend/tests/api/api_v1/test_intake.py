import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.workspace import Workspace
from app.models.organization import Organization
from app.models.identity import APIKey, User
from app.models.bug import Bug, BugSource
import uuid

@pytest_asyncio.fixture
async def api_key_setup(auth_client: AsyncClient, test_workspace: Workspace):
    # Generate a key using the authorized internal endpoint
    resp = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/api-keys",
        json={"name": "Test Intake Key"}
    )
    assert resp.status_code == 200
    return resp.json()["raw_key"], resp.json()["id"]

@pytest.mark.asyncio
async def test_valid_api_key_creates_bug(async_client: AsyncClient, api_key_setup):
    raw_key, _ = api_key_setup
    payload = {
        "title": "Intake Bug",
        "description": "Created from API",
        "priority": "P2",
        "severity": "HIGH",
    }
    resp = await async_client.post(
        "/api/v1/intake/bugs",
        json=payload,
        headers={"X-API-Key": raw_key}
    )
    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == "Intake Bug"
    
@pytest.mark.asyncio
async def test_invalid_api_key_rejected(async_client: AsyncClient):
    resp = await async_client.post(
        "/api/v1/intake/bugs",
        json={"title": "test", "description": "test"},
        headers={"X-API-Key": "elara_live_invalidkey123"}
    )
    assert resp.status_code == 401

@pytest.mark.asyncio
async def test_revoked_api_key_rejected(async_client: AsyncClient, auth_client: AsyncClient, test_workspace: Workspace, api_key_setup):
    raw_key, key_id = api_key_setup
    
    # Revoke the key
    del_resp = await auth_client.delete(f"/api/v1/workspaces/{test_workspace.id}/api-keys/{key_id}")
    assert del_resp.status_code == 200
    
    # Attempt intake
    resp = await async_client.post(
        "/api/v1/intake/bugs",
        json={"title": "test", "description": "test"},
        headers={"X-API-Key": raw_key}
    )
    assert resp.status_code == 401

@pytest.mark.asyncio
async def test_api_key_resolves_correct_tenant(async_client: AsyncClient, db: AsyncSession, api_key_setup, test_workspace: Workspace):
    raw_key, _ = api_key_setup
    resp = await async_client.post(
        "/api/v1/intake/bugs",
        json={"title": "Tenant Bug", "description": "test"},
        headers={"X-API-Key": raw_key}
    )
    assert resp.status_code == 201
    bug_id = resp.json()["id"]
    
    # Verify in db
    result = await db.execute(select(Bug).where(Bug.id == bug_id))
    bug = result.scalar_one()
    assert bug.workspace_id == test_workspace.id
    assert bug.organization_id == test_workspace.organization_id
    assert bug.source == BugSource.API

@pytest.mark.asyncio
async def test_cross_tenant_injection_impossible(async_client: AsyncClient, db: AsyncSession, api_key_setup, test_workspace: Workspace):
    raw_key, _ = api_key_setup
    fake_org_id = str(uuid.uuid4())
    fake_workspace_id = str(uuid.uuid4())
    
    # Attempt to forge payload with malicious IDs
    # Pydantic BugIntakeCreate simply ignores these fields because they aren't in the schema
    payload = {
        "title": "Malicious Bug",
        "description": "test",
        "organization_id": fake_org_id,
        "workspace_id": fake_workspace_id
    }
    
    resp = await async_client.post(
        "/api/v1/intake/bugs",
        json=payload,
        headers={"X-API-Key": raw_key}
    )
    assert resp.status_code == 201
    bug_id = resp.json()["id"]
    
    result = await db.execute(select(Bug).where(Bug.id == bug_id))
    bug = result.scalar_one()
    
    # Assert DB ignores the forgery and binds strictly to the API key's owner
    assert str(bug.organization_id) != fake_org_id
    assert str(bug.workspace_id) != fake_workspace_id
    assert bug.workspace_id == test_workspace.id

@pytest.mark.asyncio
async def test_privileged_bug_fields_cannot_be_forged(async_client: AsyncClient, db: AsyncSession, api_key_setup):
    raw_key, _ = api_key_setup
    
    # Pydantic BugIntakeCreate simply ignores these fields because they aren't in the schema
    payload = {
        "title": "Privilege Bug",
        "description": "test",
        "state": "CLOSED",
        "is_deleted": True
    }
    
    resp = await async_client.post(
        "/api/v1/intake/bugs",
        json=payload,
        headers={"X-API-Key": raw_key}
    )
    assert resp.status_code == 201
    
    result = await db.execute(select(Bug).where(Bug.id == resp.json()["id"]))
    bug = result.scalar_one()
    
    # State should default to OPEN, is_deleted to False
    assert bug.state == "OPEN"
    assert not bug.is_deleted

@pytest.mark.asyncio
async def test_invalid_payload_rejected(async_client: AsyncClient, api_key_setup):
    raw_key, _ = api_key_setup
    resp = await async_client.post(
        "/api/v1/intake/bugs",
        json={"title": ""}, # Missing description, title too short
        headers={"X-API-Key": raw_key}
    )
    assert resp.status_code == 422

@pytest.mark.asyncio
async def test_api_key_last_used_at_updates(async_client: AsyncClient, db: AsyncSession, api_key_setup):
    raw_key, key_id = api_key_setup
    
    # Check initial last_used_at
    result = await db.execute(select(APIKey).where(APIKey.id == key_id))
    key_db = result.scalar_one()
    assert key_db.last_used_at is None
    
    # Use key
    resp = await async_client.post(
        "/api/v1/intake/bugs",
        json={"title": "Usage bug", "description": "test"},
        headers={"X-API-Key": raw_key}
    )
    assert resp.status_code == 201
    
    # Verify last_used_at is populated
    await db.refresh(key_db)
    assert key_db.last_used_at is not None

@pytest.mark.asyncio
async def test_raw_api_key_never_in_response(async_client: AsyncClient, api_key_setup):
    raw_key, _ = api_key_setup
    resp = await async_client.post(
        "/api/v1/intake/bugs",
        json={"title": "Leak bug", "description": "test"},
        headers={"X-API-Key": raw_key}
    )
    assert resp.status_code == 201
    text = resp.text
    assert raw_key not in text
    
@pytest.mark.asyncio
async def test_bug_visible_internally(async_client: AsyncClient, auth_client: AsyncClient, api_key_setup, test_workspace: Workspace):
    raw_key, _ = api_key_setup
    resp = await async_client.post(
        "/api/v1/intake/bugs",
        json={"title": "Internal Vis Bug", "description": "test"},
        headers={"X-API-Key": raw_key}
    )
    assert resp.status_code == 201
    bug_id = resp.json()["id"]
    
    # Now check via internal API
    list_resp = await auth_client.get(f"/api/v1/workspaces/{test_workspace.id}/bugs")
    assert list_resp.status_code == 200
    ids = [b["id"] for b in list_resp.json()]
    assert bug_id in ids
    
@pytest.mark.asyncio
async def test_idempotency_header_validation(async_client: AsyncClient, api_key_setup):
    raw_key, _ = api_key_setup
    
    # Valid length
    resp1 = await async_client.post(
        "/api/v1/intake/bugs",
        json={"title": "Idempotent Bug", "description": "test"},
        headers={
            "X-API-Key": raw_key,
            "Idempotency-Key": "some-safe-key-123"
        }
    )
    assert resp1.status_code == 201
    
    # Invalid length > 255
    resp2 = await async_client.post(
        "/api/v1/intake/bugs",
        json={"title": "Idempotent Bug 2", "description": "test"},
        headers={
            "X-API-Key": raw_key,
            "Idempotency-Key": "x" * 256
        }
    )
    assert resp2.status_code == 400
    assert "too long" in resp2.json()["detail"]

@pytest.mark.asyncio
async def test_idempotent_retry_returns_original_result(async_client: AsyncClient, api_key_setup):
    raw_key, _ = api_key_setup
    payload = {"title": "Idempotent Retry", "description": "test"}
    headers = {"X-API-Key": raw_key, "Idempotency-Key": "test-idem-key-1"}
    
    resp1 = await async_client.post("/api/v1/intake/bugs", json=payload, headers=headers)
    assert resp1.status_code == 201
    bug_id_1 = resp1.json()["id"]
    
    resp2 = await async_client.post("/api/v1/intake/bugs", json=payload, headers=headers)
    assert resp2.status_code == 200
    bug_id_2 = resp2.json()["id"]
    
    assert bug_id_1 == bug_id_2

@pytest.mark.asyncio
async def test_same_idempotency_key_different_payload_returns_409(async_client: AsyncClient, api_key_setup):
    raw_key, _ = api_key_setup
    
    headers = {"X-API-Key": raw_key, "Idempotency-Key": "test-idem-key-2"}
    
    resp1 = await async_client.post("/api/v1/intake/bugs", json={"title": "Bug A", "description": "test"}, headers=headers)
    assert resp1.status_code == 201
    
    resp2 = await async_client.post("/api/v1/intake/bugs", json={"title": "Bug B", "description": "test"}, headers=headers)
    assert resp2.status_code == 409

@pytest.mark.asyncio
async def test_same_idempotency_key_different_workspace_does_not_collide(async_client: AsyncClient, auth_client: AsyncClient, api_key_setup, other_workspace, test_other_user):
    raw_key1, _ = api_key_setup
    
    # Generate second key for other_workspace (acting as test_other_user)
    # Actually, we need an auth client for test_other_user, but we can just use async_client to call auth endpoint
    # Wait, creating an API key requires auth. Let's just create an API key in the DB.
    # To keep it simple, I will just login as test_other_user
    login_resp = await async_client.post("/api/v1/auth/login", data={"username": "other@example.com", "password": "password123"})
    token = login_resp.json()["access_token"]
    other_auth_client = AsyncClient(base_url=async_client.base_url, headers={"Authorization": f"Bearer {token}"})
    
    resp_key = await other_auth_client.post(
        f"/api/v1/workspaces/{other_workspace.id}/api-keys",
        json={"name": "Test Intake Key 2"}
    )
    assert resp_key.status_code == 200
    raw_key2 = resp_key.json()["raw_key"]
    
    idem_key = "shared-idem-key-123"
    payload = {"title": "Cross Workspace Idem Bug", "description": "test"}
    
    resp1 = await async_client.post("/api/v1/intake/bugs", json=payload, headers={"X-API-Key": raw_key1, "Idempotency-Key": idem_key})
    assert resp1.status_code == 201
    
    resp2 = await async_client.post("/api/v1/intake/bugs", json=payload, headers={"X-API-Key": raw_key2, "Idempotency-Key": idem_key})
    assert resp2.status_code == 201
    
    assert resp1.json()["id"] != resp2.json()["id"]

@pytest.mark.asyncio
async def test_concurrent_duplicate_submission(async_client: AsyncClient, api_key_setup):
    import asyncio
    raw_key, _ = api_key_setup
    
    payload = {"title": "Concurrent Bug", "description": "test"}
    headers = {"X-API-Key": raw_key, "Idempotency-Key": "concurrent-idem-key-1"}
    
    # Fire 5 concurrent requests
    tasks = [
        async_client.post("/api/v1/intake/bugs", json=payload, headers=headers)
        for _ in range(5)
    ]
    
    responses = await asyncio.gather(*tasks)
    
    # One should succeed (201), the rest should wait and return 200 OK
    successes_201 = [r for r in responses if r.status_code == 201]
    successes_200 = [r for r in responses if r.status_code == 200]
    
    assert len(successes_201) == 1
    assert len(successes_200) == 4
    
    # Ensure they all returned the exact same bug_id
    bug_ids = set(r.json()["id"] for r in responses)
    assert len(bug_ids) == 1

