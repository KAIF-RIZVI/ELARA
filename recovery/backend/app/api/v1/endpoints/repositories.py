from fastapi import APIRouter, status
from app.api.deps import CurrentUser
from app.worker.tasks.repo_tasks import sync_repository_task
import uuid

router = APIRouter()

@router.post("/{repository_id}/sync", status_code=status.HTTP_202_ACCEPTED)
async def sync_repository(
    repository_id: uuid.UUID,
    workspace_id: uuid.UUID,
    current_user: CurrentUser
):
    """
    Triggers an async Celery task to fetch the repository and index it for AI embeddings.
    """
    # Dispatch Celery task
    sync_repository_task.delay(str(repository_id), str(workspace_id))
    return {"message": "Repository sync initiated in the background"}