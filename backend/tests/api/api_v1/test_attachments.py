import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
import uuid
import io

@pytest.mark.asyncio
async def test_attachment_upload_and_download(
    async_client: AsyncClient,
    db: AsyncSession,
    auth_client: AsyncClient,
    test_user,
    test_workspace
):
    # First create a bug
    bug_payload = {
        "title": "Attachment Test Bug",
        "description": "Bug for testing attachments"
    }
    
    resp = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs",
        json=bug_payload
    )
    assert resp.status_code == 200
    bug_id = resp.json()["id"]
    
    # Upload an attachment
    file_content = b"test attachment content"
    files = {
        "file": ("test.txt", io.BytesIO(file_content), "text/plain")
    }
    
    resp = await auth_client.post(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}/attachments",
        files=files
    )
    assert resp.status_code == 200
    attachment_data = resp.json()
    assert attachment_data["bug_id"] == bug_id
    assert attachment_data["mime_type"] == "text/plain"
    assert attachment_data["size_bytes"] == len(file_content)
    
    attachment_id = attachment_data["id"]
    
    # List attachments
    resp = await auth_client.get(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}/attachments"
    )
    assert resp.status_code == 200
    attachments = resp.json()
    assert len(attachments) == 1
    assert attachments[0]["id"] == attachment_id
    
    # Download attachment
    resp = await auth_client.get(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}/attachments/{attachment_id}/download"
    )
    assert resp.status_code == 200
    assert resp.content == file_content
    assert resp.headers["content-type"].startswith("text/plain")
    
    # Delete attachment
    resp = await auth_client.delete(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}/attachments/{attachment_id}"
    )
    # Admin role is required for deletion. test_user is admin in test_workspace (from conftest.py)
    assert resp.status_code == 200
    
    # List attachments again
    resp = await auth_client.get(
        f"/api/v1/workspaces/{test_workspace.id}/bugs/{bug_id}/attachments"
    )
    assert resp.status_code == 200
    assert len(resp.json()) == 0
