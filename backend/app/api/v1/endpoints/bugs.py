from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep, CurrentUser
from app.schemas.bug import BugCreate, BugResponse
from app.services.bug import bug_service
import uuid

router = APIRouter()

@router.post("", response_model=BugResponse)
async def ingest_bug(db: SessionDep, current_user: CurrentUser, bug_in: BugCreate):
    try:
        bug = await bug_service.ingest_bug(
            db, 
            bug_in=bug_in,
            reported_by=current_user.id
        )
        # Here we will eventually trigger the Celery background task for AI Analysis (Phase 4)
        return bug
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{bug_id}", response_model=BugResponse)
async def get_bug(db: SessionDep, current_user: CurrentUser, bug_id: uuid.UUID):
    bug = await bug_service.get(db, id=bug_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
    return bug
