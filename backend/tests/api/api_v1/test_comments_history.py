import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

@pytest.mark.asyncio
async def test_add_and_list_comments(
    auth_client: AsyncClient,
    test_user,
    test_workspace,
    db: AsyncSession
):
    # 1. Create a bug
    bug_resp = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs",
        json={"title": "Comment Test", "description": "Test body"}
    )
    assert bug_resp.status_code == 200
    bug_id = bug_resp.json()["id"]

    # 2. Add a comment
    comment_resp = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}/comments",
        json={"body": "This is a test comment"}
    )
    assert comment_resp.status_code == 200
    comment_data = comment_resp.json()
    assert comment_data["body"] == "This is a test comment"
    assert comment_data["bug_id"] == bug_id
    assert comment_data["author_id"] == str(test_user.id)

    # 3. List comments
    list_resp = await auth_client.get(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}/comments"
    )
    assert list_resp.status_code == 200
    comments = list_resp.json()
    assert len(comments) == 1
    assert comments[0]["id"] == comment_data["id"]

@pytest.mark.asyncio
async def test_get_bug_history(
    auth_client: AsyncClient,
    test_user,
    test_workspace
):
    # 1. Create a bug
    bug_resp = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs",
        json={"title": "History Test", "description": "History"}
    )
    assert bug_resp.status_code == 200
    bug_id = bug_resp.json()["id"]

    # 2. Add a comment to trigger BUG_COMMENTED event
    await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}/comments",
        json={"body": "History comment"}
    )

    # 3. Fetch history
    history_resp = await auth_client.get(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}/history"
    )
    assert history_resp.status_code == 200
    history = history_resp.json()
    
    # We expect at least BUG_CREATED and BUG_COMMENTED
    assert len(history) >= 2
    
    actions = [h["action"] for h in history]
    assert "BUG_CREATED" in actions
    assert "BUG_COMMENTED" in actions
    
    # Verify metadata_payload exists
    created_event = next(h for h in history if h["action"] == "BUG_CREATED")
    assert "metadata_payload" in created_event
    assert created_event["metadata_payload"]["state"] == "OPEN"

@pytest.mark.asyncio
async def test_cross_workspace_comments_rejected(
    auth_client: AsyncClient,
    test_workspace,
    db: AsyncSession
):
    # Create bug in test_workspace
    bug_resp = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs",
        json={"title": "Cross WS Test", "description": "Test body"}
    )
    bug_id = bug_resp.json()["id"]

    # Try to comment on it using a fake workspace ID
    fake_ws_id = str(uuid.uuid4())
    resp = await auth_client.post(
        f"/api/v1/workspaces/{fake_ws_id}/bugs/{bug_id}/comments",
        json={"body": "Hacker comment"}
    )
    # The member role dependency will fail first (403/404)
    assert resp.status_code in (404, 403, 401)

@pytest.mark.asyncio
async def test_deleted_bug_rejects_comments(
    auth_client: AsyncClient,
    test_workspace
):
    # Create bug
    bug_resp = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs",
        json={"title": "Delete Test", "description": "Test body"}
    )
    bug_id = bug_resp.json()["id"]

    # Delete bug
    del_resp = await auth_client.delete(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}"
    )
    assert del_resp.status_code == 200

    # Try to comment
    comment_resp = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}/comments",
        json={"body": "Comment on deleted"}
    )
    assert comment_resp.status_code in (404, 400)
