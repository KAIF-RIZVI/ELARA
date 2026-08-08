from fastapi import APIRouter
from app.api.deps import SessionDep, CurrentUser
from app.services.dashboard import dashboard_service
import uuid

router = APIRouter()

@router.get("/{workspace_id}/stats")
async def get_dashboard_stats(workspace_id: uuid.UUID, db: SessionDep, current_user: CurrentUser):
    # In a full setup, check if current_user is in workspace_id
    return await dashboard_service.get_stats(db, workspace_id)

@router.get("/{workspace_id}/activity")
async def get_dashboard_activity(workspace_id: uuid.UUID, db: SessionDep, current_user: CurrentUser):
    return await dashboard_service.get_activity(db, workspace_id)