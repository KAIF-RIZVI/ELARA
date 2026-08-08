from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, func
import uuid
from app.api.deps import SessionDep, CurrentUser, RequireRole
from app.schemas.workspace import WorkspaceCreate, WorkspaceResponse, WorkspaceUpdate, WorkspaceOverview
from app.services.workspace import workspace_service
from app.models import WorkspaceMember, MemberRole, WorkspaceStatus, Project, Repository, AIWallet

router = APIRouter()

@router.post("", response_model=WorkspaceResponse)
async def create_workspace(db: SessionDep, current_user: CurrentUser, workspace_in: WorkspaceCreate):
    try:
        workspace = await workspace_service.create_workspace(
            db, 
            name=workspace_in.name, 
            slug=workspace_in.slug, 
            user_id=current_user.id,
            settings=workspace_in.settings
        )
        return workspace
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=list[WorkspaceResponse])
async def list_workspaces(db: SessionDep, current_user: CurrentUser):
    # Fetch workspaces where the user is a member
    stmt = select(WorkspaceMember.workspace_id).where(WorkspaceMember.user_id == current_user.id)
    result = await db.execute(stmt)
    workspace_ids = [row[0] for row in result.all()]

    if not workspace_ids:
        return []

    workspaces = await workspace_service.get_multi(db)
    return [w for w in workspaces if w.id in workspace_ids]

@router.get("/{workspace_id}", response_model=WorkspaceOverview)
async def get_workspace_overview(
    workspace_id: uuid.UUID,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    workspace = await workspace_service.get(db, id=workspace_id)
    if not workspace:
        raise HTTPException(status_code=404, detail="Workspace not found")

    # Fetch stats
    members_count = await db.scalar(select(func.count(WorkspaceMember.id)).where(WorkspaceMember.workspace_id == workspace_id))
    projects_count = await db.scalar(select(func.count(Project.id)).where(Project.workspace_id == workspace_id))
    repositories_count = await db.scalar(select(func.count(Repository.id)).where(Repository.workspace_id == workspace_id))
    
    wallet = await db.scalar(select(AIWallet).where(AIWallet.workspace_id == workspace_id))
    ai_credits = wallet.balance_units if wallet else 0

    return WorkspaceOverview(
        **workspace.__dict__,
        members_count=members_count or 0,
        projects_count=projects_count or 0,
        repositories_count=repositories_count or 0,
        ai_credits_remaining=ai_credits
    )

@router.put("/{workspace_id}", response_model=WorkspaceResponse)
async def update_workspace(
    workspace_id: uuid.UUID,
    workspace_in: WorkspaceUpdate,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    workspace = await workspace_service.get(db, id=workspace_id)
    if not workspace:
        raise HTTPException(status_code=404, detail="Workspace not found")
        
    workspace = await workspace_service.update(db, db_obj=workspace, obj_in=workspace_in)
    return workspace

@router.delete("/{workspace_id}", response_model=dict)
async def archive_workspace(
    workspace_id: uuid.UUID,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.OWNER))
):
    workspace = await workspace_service.get(db, id=workspace_id)
    if not workspace:
        raise HTTPException(status_code=404, detail="Workspace not found")
        
    workspace = await workspace_service.update(db, db_obj=workspace, obj_in={"status": WorkspaceStatus.SUSPENDED})
    return {"message": "Workspace archived successfully"}
