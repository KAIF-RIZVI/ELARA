import uuid
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from app.api.deps import SessionDep, CurrentUser, RequireOrganizationRole
from app.schemas.api_key import APIKeyCreate, APIKeyResponse, APIKeyCreateResponse
from app.services.api_keys import api_key_service
from app.models.organization import OrganizationMember, OrganizationRole as MemberRole

router = APIRouter()

@router.post("", response_model=APIKeyCreateResponse)
async def create_api_key(
    organization_id: uuid.UUID,
    key_in: APIKeyCreate,
    db: SessionDep,
    current_user: CurrentUser,
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.ADMIN))
):
    try:
        api_key, raw_key = await api_key_service.create_key(
            db=db,
            organization_id=organization_id,
            name=key_in.name,
            user_id=current_user.id
        )
        
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
    organization_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.ADMIN))
):
    keys = await api_key_service.list_keys(db, organization_id=organization_id)
    return keys

@router.delete("/{key_id}", response_model=APIKeyResponse)
async def revoke_api_key(
    organization_id: uuid.UUID,
    key_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.ADMIN))
):
    try:
        api_key = await api_key_service.revoke_key(
            db=db,
            key_id=key_id,
            organization_id=organization_id,
            user_id=current_user.id
        )
        return api_key
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
