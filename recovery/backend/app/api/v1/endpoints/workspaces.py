from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep, CurrentUser
from app.schemas.workspace import WorkspaceCreate, WorkspaceResponse
from app.services.workspace import workspace_service

router = APIRouter()

@router.post("/", response_model=WorkspaceResponse)
async def create_workspace(db: SessionDep, current_user: CurrentUser, workspace_in: WorkspaceCreate):
    try:
        workspace = await workspace_service.create_workspace(
            db, 
            name=workspace_in.name, 
            slug=workspace_in.slug, 
            settings=workspace_in.settings
        )
        # TODO: Assign current_user as OWNER of this workspace in WorkspaceMembers
        return workspace
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[WorkspaceResponse])
async def list_workspaces(db: SessionDep, current_user: CurrentUser):
    # TODO: Fetch only workspaces where current_user is a member
    workspaces = await workspace_service.get_multi(db)
    return workspaces
