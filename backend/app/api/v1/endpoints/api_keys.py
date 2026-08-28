import uuid
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from app.api.deps import SessionDep, CurrentUser, RequireRole
from app.schemas.api_key import APIKeyCreate, APIKeyResponse, APIKeyCreateResponse
from app.services.api_keys import api_key_service
from app.services.workspace import workspace_service
from app.models.identity import WorkspaceMember, MemberRole

router = APIRouter()

async def get_org_id_for_workspace(db: SessionDep, workspace_id: uuid.UUID) -> uuid.UUID:
    workspace = await workspace_service.get(db, id=workspace_id)
    if not workspace or not workspace.organization_id:
        raise HTTPException(status_code=400, detail="Invalid workspace context. Legacy workspaces must be migrated to an organization.")
    return workspace.organization_id

@router.post("", response_model=APIKeyCreateResponse)
async def create_api_key(
    workspace_id: uuid.UUID,
    key_in: APIKeyCreate,
    db: SessionDep,
    current_user: CurrentUser,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        api_key, raw_key = await api_key_service.create_workspace_key(
            db=db,
            organization_id=organization_id,
            workspace_id=workspace_id,
            name=key_in.name,
            user_id=current_user.id
        )
        
        # We merge the DB object and raw_key for the CreateResponse
        return {
            "id": api_key.id,
            "name": api_key.name,
            "prefix": api_key.prefix,
            "organization_id": api_key.organization_id,
            "workspace_id": api_key.workspace_id,
            "created_at": api_key.created_at,
            "last_used_at": api_key.last_used_at,
            "revoked_at": api_key.revoked_at,
            "created_by": api_key.created_by,
            "raw_key": raw_key
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=List[APIKeyResponse])
async def list_api_keys(
    workspace_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    await get_org_id_for_workspace(db, workspace_id)
    keys = await api_key_service.list_workspace_keys(db, workspace_id=workspace_id)
    return keys

@router.delete("/{key_id}", response_model=APIKeyResponse)
async def revoke_api_key(
    workspace_id: uuid.UUID,
    key_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    await get_org_id_for_workspace(db, workspace_id)
    try:
        api_key = await api_key_service.revoke_workspace_key(
            db=db,
            key_id=key_id,
            workspace_id=workspace_id,
            user_id=current_user.id
        )
        return api_key
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
