from fastapi import APIRouter, status, HTTPException, Depends
from app.api.deps import CurrentUser, SessionDep, RequireRole
from app.models.identity import MemberRole, WorkspaceMember
from app.worker.tasks.repo_tasks import sync_repository_task
from app.schemas.repository import RepositoryCreate, RepositoryResponse
from app.services.repository import repository_service
import uuid

router = APIRouter()

@router.get("/", response_model=list[RepositoryResponse])
async def list_repositories(
    workspace_id: uuid.UUID, 
    db: SessionDep, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    return await repository_service.get_by_workspace(db, workspace_id)

@router.post("/", response_model=RepositoryResponse)
async def connect_repository(
    repo_in: RepositoryCreate,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    try:
        return await repository_service.connect_repository(
            db,
            workspace_id=repo_in.workspace_id,
            provider=repo_in.provider,
            full_name=repo_in.full_name,
            external_id=repo_in.external_id,
            default_branch=repo_in.default_branch,
            user_id=member.user_id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{repository_id}", status_code=status.HTTP_204_NO_CONTENT)
async def disconnect_repository(
    repository_id: uuid.UUID,
    workspace_id: uuid.UUID,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    try:
        await repository_service.disconnect_repository(
            db,
            repository_id=repository_id,
            workspace_id=workspace_id,
            user_id=member.user_id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{repository_id}/sync", status_code=status.HTTP_202_ACCEPTED)
async def sync_repository(
    repository_id: uuid.UUID,
    workspace_id: uuid.UUID,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    """
    Triggers an async Celery task to fetch the repository and index it for AI embeddings.
    """
    sync_repository_task.delay(str(repository_id), str(workspace_id))
    return {"message": "Repository sync initiated in the background"}