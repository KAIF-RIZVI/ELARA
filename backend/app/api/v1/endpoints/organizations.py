from fastapi import APIRouter, HTTPException, Depends, status
import uuid
from typing import List
from app.api.deps import SessionDep, CurrentUser, RequireOrganizationRole
from app.models.organization import OrganizationRole
from app.schemas.organization import (
    OrganizationCreate, 
    OrganizationResponse,
    OrganizationSwitcherResponse,
    OrganizationUpdate,
    OrganizationMemberResponse,
    OrganizationMemberUpdate,
    OrganizationInviteCreate,
    OrganizationInviteResponse,
    OrganizationSettingsUpdate,
    OrganizationSettingsResponse,
    OrganizationSettingsResponse,
    OrganizationAuditLogResponse,
    OrganizationStatsResponse,
    OrganizationDiscoveryResponse,
    OrganizationJoinRequestCreate,
    OrganizationJoinRequestResponse
)
from app.schemas.profile import PublicProfileResponse
from app.schemas.dashboard import OrganizationDashboardResponse
from app.services.organization import organization_service
from app.services.organization_member import organization_member_service
from app.services.organization_invitation import organization_invitation_service
from app.services.organization_settings import organization_settings_service
from app.services.organization_audit import organization_audit_service
from app.services.organization_dashboard import organization_dashboard_service
from app.services.organization_discovery import organization_discovery_service

router = APIRouter()

@router.post("", response_model=OrganizationResponse, status_code=status.HTTP_201_CREATED)
async def create_organization(
    db: SessionDep, 
    current_user: CurrentUser, 
    org_in: OrganizationCreate
):
    org = await organization_service.create_organization(db, org_in, current_user.id)
    return org

@router.get("/me", response_model=List[OrganizationSwitcherResponse])
async def list_my_organizations(
    db: SessionDep, 
    current_user: CurrentUser
):
    orgs = await organization_service.get_user_organizations(db, current_user.id)
    return orgs

# --- Discovery ---
@router.get("/discover", response_model=List[OrganizationDiscoveryResponse])
async def discover_organizations(
    db: SessionDep,
    current_user: CurrentUser,
    q: str = None,
    limit: int = 50,
    offset: int = 0
):
    return await organization_discovery_service.search_organizations(db, user_id=current_user.id, query=q, limit=limit, offset=offset)

@router.get("/{organization_id}", response_model=OrganizationResponse)
async def get_organization(
    organization_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.VIEWER))
):
    org = await organization_service.get_organization(db, organization_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org

@router.patch("/{organization_id}", response_model=OrganizationResponse)
async def update_organization(
    organization_id: uuid.UUID,
    org_in: OrganizationUpdate,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    return await organization_service.update_organization(db, organization_id, org_in, current_user.id)

# --- Members ---

@router.get("/{organization_id}/members", response_model=List[OrganizationMemberResponse])
async def list_members(
    organization_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.VIEWER))
):
    return await organization_member_service.get_members(db, organization_id)

@router.get("/{organization_id}/members/{user_id}/profile", response_model=PublicProfileResponse)
async def get_member_profile(
    organization_id: uuid.UUID,
    user_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.VIEWER))
):
    profile = await organization_service.get_member_public_profile(db, organization_id, user_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Member profile not found in this organization")
    return profile

@router.patch("/{organization_id}/members/{user_id}", response_model=OrganizationMemberResponse)
async def update_member(
    organization_id: uuid.UUID,
    user_id: uuid.UUID,
    member_in: OrganizationMemberUpdate,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    if not member_in.role:
        raise HTTPException(status_code=400, detail="Role is required")
        
    # Only OWNER can assign OWNER
    if member_in.role == OrganizationRole.OWNER and member.role != OrganizationRole.OWNER:
        raise HTTPException(status_code=403, detail="Only owners can assign the owner role")
        
    return await organization_member_service.update_member_role(db, organization_id, user_id, member_in.role, current_user.id)

@router.delete("/{organization_id}/members/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_member(
    organization_id: uuid.UUID,
    user_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    await organization_member_service.remove_member(db, organization_id, user_id, current_user.id)

# --- Invitations ---

@router.get("/{organization_id}/invitations", response_model=List[OrganizationInviteResponse])
async def list_invitations(
    organization_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    return await organization_invitation_service.get_invitations(db, organization_id)

@router.post("/{organization_id}/members/invite", response_model=OrganizationInviteResponse)
async def invite_member(
    organization_id: uuid.UUID,
    invite_in: OrganizationInviteCreate,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    return await organization_invitation_service.create_invitation(
        db, organization_id, invite_in.email, invite_in.role, current_user.id
    )
    
@router.delete("/{organization_id}/invitations/{invitation_id}", status_code=status.HTTP_204_NO_CONTENT)
async def revoke_invitation(
    organization_id: uuid.UUID,
    invitation_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    await organization_invitation_service.revoke_invitation(db, organization_id, invitation_id, current_user.id)

@router.post("/invitations/{token}/accept", response_model=OrganizationMemberResponse)
async def accept_invitation(
    token: str,
    db: SessionDep,
    current_user: CurrentUser
):
    return await organization_invitation_service.accept_invitation(db, token, current_user.id)

@router.post("/invitations/{token}/reject", status_code=status.HTTP_204_NO_CONTENT)
async def reject_invitation(
    token: str,
    db: SessionDep,
    current_user: CurrentUser
):
    await organization_invitation_service.reject_invitation(db, token, current_user.id)

# --- Settings ---

@router.get("/{organization_id}/settings", response_model=OrganizationSettingsResponse)
async def get_settings(
    organization_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    return await organization_settings_service.get_settings(db, organization_id)

@router.patch("/{organization_id}/settings", response_model=OrganizationSettingsResponse)
async def update_settings(
    organization_id: uuid.UUID,
    settings_in: OrganizationSettingsUpdate,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    return await organization_settings_service.update_settings(db, organization_id, settings_in, current_user.id)

# --- Audit Logs ---

@router.get("/{organization_id}/audit-logs", response_model=List[OrganizationAuditLogResponse])
async def get_audit_logs(
    organization_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    return await organization_audit_service.get_audit_logs(db, organization_id)

# --- Stats ---

@router.get("/{organization_id}/stats", response_model=OrganizationStatsResponse)
async def get_stats(
    organization_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.VIEWER))
):
    return await organization_service.get_organization_stats(db, organization_id)

# --- Dashboard ---

@router.get("/{organization_id}/dashboard", response_model=OrganizationDashboardResponse)
async def get_organization_dashboard(
    organization_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.VIEWER))
):
    dashboard_data = await organization_dashboard_service.get_dashboard_data(db, organization_id, current_user.id)
    if not dashboard_data:
        raise HTTPException(status_code=404, detail="Dashboard data not found")
    return dashboard_data

# --- Join Requests ---

@router.get("/{organization_id}/join-requests", response_model=List[OrganizationJoinRequestResponse])
async def list_join_requests(
    organization_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    return await organization_discovery_service.get_join_requests(db, organization_id)

@router.post("/{organization_id}/join-request", response_model=OrganizationJoinRequestResponse)
async def create_join_request(
    organization_id: uuid.UUID,
    req_in: OrganizationJoinRequestCreate,
    db: SessionDep,
    current_user: CurrentUser
):
    return await organization_discovery_service.create_join_request(
        db, organization_id, current_user.id, req_in.message
    )

@router.delete("/{organization_id}/join-request")
async def cancel_join_request(
    organization_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser
):
    await organization_discovery_service.cancel_join_request(db, organization_id, current_user.id)
    return {"message": "Join request cancelled"}

@router.post("/{organization_id}/join-requests/{request_id}/approve", response_model=OrganizationMemberResponse)
async def approve_join_request(
    organization_id: uuid.UUID,
    request_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    return await organization_discovery_service.approve_join_request(
        db, organization_id, request_id, current_user.id
    )

@router.post("/{organization_id}/join-requests/{request_id}/reject")
async def reject_join_request(
    organization_id: uuid.UUID,
    request_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    await organization_discovery_service.reject_join_request(
        db, organization_id, request_id, current_user.id
    )
    return {"message": "Join request rejected"}
