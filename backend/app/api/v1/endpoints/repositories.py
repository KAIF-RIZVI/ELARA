from fastapi import APIRouter, status, HTTPException, Depends
from typing import Optional
from app.api.deps import CurrentUser, SessionDep, RequireRole, RequireOrganizationRole
from app.models.identity import MemberRole, WorkspaceMember
from app.models.organization import OrganizationMember, OrganizationRole
from app.worker.tasks.repo_tasks import sync_repository_task
from app.schemas.repository import RepositoryCreate, RepositoryResponse
from app.services.repository import repository_service
import uuid

router = APIRouter()

@router.get("", response_model=list[RepositoryResponse])
async def list_repositories(
    db: SessionDep, 
    current_user: CurrentUser,
    workspace_id: Optional[uuid.UUID] = None,
    organization_id: Optional[uuid.UUID] = None
):
    if workspace_id:
        await RequireRole(MemberRole.DEVELOPER)(workspace_id, db, current_user)
        repos = await repository_service.get_by_workspace(db, workspace_id=workspace_id)
    elif organization_id:
        await RequireOrganizationRole(OrganizationRole.DEVELOPER)(organization_id, db, current_user)
        repos = await repository_service.get_by_organization(db, organization_id=organization_id)
    else:
        raise HTTPException(status_code=400, detail="Must provide either workspace_id or organization_id")
        
    result = []
    for repo in repos:
        repo_dict = RepositoryResponse.model_validate(repo).model_dump()
        repo_dict["health_score"] = repository_service.calculate_health_score(repo)
        result.append(repo_dict)
    return result

@router.post("", response_model=RepositoryResponse)
async def connect_repository(
    repo_in: RepositoryCreate,
    db: SessionDep,
    current_user: CurrentUser
):
    if repo_in.workspace_id:
        await RequireRole(MemberRole.ADMIN)(repo_in.workspace_id, db, current_user)
    elif repo_in.organization_id:
        await RequireOrganizationRole(OrganizationRole.PROJECT_MANAGER)(repo_in.organization_id, db, current_user)
    else:
        raise HTTPException(status_code=400, detail="Must provide either workspace_id or organization_id")

    try:
        repo = await repository_service.connect_repository(
            db,
            repo_in=repo_in,
            user_id=current_user.id
        )
        repo_dict = RepositoryResponse.model_validate(repo).model_dump()
        repo_dict["health_score"] = repository_service.calculate_health_score(repo)
        return repo_dict
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{repository_id}", response_model=RepositoryResponse)
async def get_repository(
    repository_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    workspace_id: Optional[uuid.UUID] = None,
    organization_id: Optional[uuid.UUID] = None
):
    if workspace_id:
        await RequireRole(MemberRole.DEVELOPER)(workspace_id, db, current_user)
    elif organization_id:
        await RequireOrganizationRole(OrganizationRole.DEVELOPER)(organization_id, db, current_user)
    else:
        raise HTTPException(status_code=400, detail="Must provide either workspace_id or organization_id")

    repo = await repository_service.get(db, repository_id)
    if not repo:
        raise HTTPException(status_code=404, detail="Repository not found")
        
    repo_dict = RepositoryResponse.model_validate(repo).model_dump()
    repo_dict["health_score"] = repository_service.calculate_health_score(repo)
    return repo_dict

@router.delete("/{repository_id}", status_code=status.HTTP_204_NO_CONTENT)
async def disconnect_repository(
    repository_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    workspace_id: Optional[uuid.UUID] = None,
    organization_id: Optional[uuid.UUID] = None
):
    if workspace_id:
        await RequireRole(MemberRole.ADMIN)(workspace_id, db, current_user)
    elif organization_id:
        await RequireOrganizationRole(OrganizationRole.PROJECT_MANAGER)(organization_id, db, current_user)
    else:
        raise HTTPException(status_code=400, detail="Must provide either workspace_id or organization_id")

    try:
        await repository_service.disconnect_repository(
            db,
            repository_id=repository_id,
            workspace_id=workspace_id,
            organization_id=organization_id,
            user_id=current_user.id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{repository_id}/sync", status_code=status.HTTP_202_ACCEPTED)
async def sync_repository(
    repository_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    workspace_id: Optional[uuid.UUID] = None,
    organization_id: Optional[uuid.UUID] = None
):
    """
    Triggers an async Celery task to fetch the repository and index it for AI embeddings.
    """
    if workspace_id:
        raise HTTPException(status_code=403, detail="Enterprise AI/Data pipelines are disabled for Personal Workspaces. Please use an Organization.")
        
    if not organization_id:
        raise HTTPException(status_code=400, detail="Organization ID is required")
        
    await RequireOrganizationRole(OrganizationRole.PROJECT_MANAGER)(organization_id, db, current_user)
    
    sync_repository_task.delay(str(repository_id), str(organization_id))
    return {"message": "Repository sync initiated in the background"}

@router.post("/{repository_id}/refresh", response_model=RepositoryResponse)
async def refresh_repository_metadata(
    repository_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    workspace_id: Optional[uuid.UUID] = None,
    organization_id: Optional[uuid.UUID] = None
):
    """
    Manually refreshes repository metadata from the provider.
    """
    if workspace_id:
        await RequireRole(MemberRole.ADMIN)(workspace_id, db, current_user)
    elif organization_id:
        await RequireOrganizationRole(OrganizationRole.PROJECT_MANAGER)(organization_id, db, current_user)
    else:
        raise HTTPException(status_code=400, detail="Must provide either workspace_id or organization_id")

    repo = await repository_service.get(db, repository_id)
    if not repo:
        raise HTTPException(status_code=404, detail="Repository not found")
        
    # In a real implementation, this would trigger an external API fetch
    # For now we'll just return the updated model
    repo_dict = RepositoryResponse.model_validate(repo).model_dump()
    repo_dict["health_score"] = repository_service.calculate_health_score(repo)
    return repo_dict