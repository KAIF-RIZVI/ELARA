from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, func, or_, and_
import uuid
from app.api.deps import SessionDep, CurrentUser, RequireRole
from app.schemas.workspace import WorkspaceCreate, WorkspaceResponse, WorkspaceUpdate, WorkspaceOverview
from app.services.workspace import workspace_service
from app.models import WorkspaceMember, MemberRole, WorkspaceStatus, Project, Repository, AIWallet
from app.models.workspace import ActivityLog

router = APIRouter()

@router.get("/{workspace_id}/activity")
async def get_workspace_activity(
    workspace_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    stmt = select(ActivityLog).where(
        or_(
            ActivityLog.workspace_id == workspace_id,
            and_(ActivityLog.workspace_id.is_(None), ActivityLog.user_id == current_user.id)
        )
    ).order_by(ActivityLog.created_at.desc()).limit(15)
    result = await db.execute(stmt)
    logs = result.scalars().all()
    
    activities = []
    for log in logs:
        action_map = {
            "bug.created": "bug_created",
            "bug.assigned": "bug_assigned",
            "bug.fixed": "bug_closed",
            "repo.connected": "repository_connected",
            "repo.disconnected": "repository_disconnected",
            "project.created": "project_created",
            "member.joined": "member_joined",
            "profile.updated": "member_joined",
            "auth.login.success": "member_joined",
            "auth.register.success": "member_joined"
        }
        mapped_type = action_map.get(log.action, "bug_created")
        
        # Set dynamic title
        title = "Activity"
        actor = "System"
        description = log.target

        if log.action == "profile.updated":
            title = "Updated Profile"
            actor = current_user.email.split("@")[0].upper()
            description = "Updated developer profile details"
        elif log.action == "auth.login.success":
            title = "Logged in"
            actor = current_user.email.split("@")[0].upper()
            description = "Authenticated successfully"
        elif log.action == "auth.register.success":
            title = "Registered Account"
            actor = current_user.email.split("@")[0].upper()
            description = "Created a new account"

        activities.append({
            "id": log.id,
            "type": mapped_type,
            "actor": actor,
            "actor_avatar": None,
            "title": title,
            "description": description,
            "created_at": log.created_at.isoformat() if log.created_at else None
        })
    return activities

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
    repositories_count = await db.scalar(select(func.count(Repository.id)).where(Repository.workspace_id == workspace_id))
    
    wallet = await db.scalar(select(AIWallet).where(AIWallet.workspace_id == workspace_id))
    ai_credits = wallet.balance_units if wallet else 0

    return WorkspaceOverview(
        **workspace.__dict__,
        members_count=members_count or 0,
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
