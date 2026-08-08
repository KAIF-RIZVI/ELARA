from fastapi import APIRouter, Depends
from app.api.deps import SessionDep, CurrentUser, RequireRole
from app.models.identity import MemberRole, WorkspaceMember
from app.services.dashboard import dashboard_service
import uuid

router = APIRouter()

@router.get("/{workspace_id}/stats")
async def get_dashboard_stats(
    workspace_id: uuid.UUID, 
    db: SessionDep, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    return await dashboard_service.get_stats(db, workspace_id)

@router.get("/{workspace_id}/activity")
async def get_dashboard_activity(
    workspace_id: uuid.UUID, 
    db: SessionDep, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    return await dashboard_service.get_activity(db, workspace_id)