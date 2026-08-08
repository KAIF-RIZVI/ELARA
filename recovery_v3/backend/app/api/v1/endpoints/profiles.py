from fastapi import APIRouter, Depends, HTTPException, status
from typing import Any
from app.api.deps import SessionDep, CurrentUser
from app.schemas.profile import (
    DeveloperProfileCreate, 
    DeveloperProfileUpdate, 
    DeveloperProfileResponse,
    EnterpriseProfileResponse,
    AccountInfo,
    ConnectedAccounts,
    QuickStats
)
from app.services.profile import profile_service
from app.models.workspace import Workspace, Subscription, ActivityLog
from app.models.identity import OAuthAccount, WorkspaceMember
from app.models.project import Repository
from app.models.ai import Assignment
from app.models.bug import Bug
from sqlalchemy import select, func

router = APIRouter()

@router.get("/me", response_model=EnterpriseProfileResponse)
async def get_my_profile(db: SessionDep, current_user: CurrentUser):
    """
    Get the comprehensive enterprise developer profile dashboard for the current user.
    """
    # 1. Get Developer Profile
    profile = await profile_service.get_by_user(db, user_id=current_user.id)
    if not profile:
        profile_obj = DeveloperProfileCreate().model_dump(exclude_unset=True)
        profile = await profile_service.create_profile(db, user_id=current_user.id, obj_in=profile_obj)

    # 2. Get Workspace and Subscription Info
    workspace_info = None
    role = None
    plan = None
    joined_at = None
    
    workspace_member_result = await db.execute(
        select(WorkspaceMember, Workspace, Subscription)
        .join(Workspace, WorkspaceMember.workspace_id == Workspace.id)
        .outerjoin(Subscription, Subscription.workspace_id == Workspace.id)
        .where(WorkspaceMember.user_id == current_user.id)
    )
    row = workspace_member_result.first()
    if row:
        member, ws, sub = row
        workspace_info = ws.name
        role = member.role.value
        joined_at = member.joined_at.isoformat() if member.joined_at else None
        plan = sub.plan.value if sub else "FREE"

    # 3. Get OAuth Accounts
    oauth_result = await db.execute(select(OAuthAccount).where(OAuthAccount.user_id == current_user.id))
    oauth_accounts = oauth_result.scalars().all()
    providers = {acc.provider for acc in oauth_accounts}
    auth_method = "oauth" if providers else "email"

    # 4. Get Stats
    stats = QuickStats(
        repositories_connected=0,
        repositories_indexed=0,
        bugs_assigned=0,
        ai_recommendations_received=0,
        ai_recommendations_accepted=0,
        workspace_joined=joined_at,
        recent_activity_count=0
    )
    
    if row and row[1]:
        ws_id = row[1].id
        repo_count = await db.scalar(select(func.count(Repository.id)).where(Repository.workspace_id == ws_id))
        stats.repositories_connected = repo_count or 0
        stats.repositories_indexed = repo_count or 0  # Assuming all are indexed for now
        
        # Bugs assigned to this user in this workspace (not currently modeled in DB, mock to 0 for now)
        stats.bugs_assigned = 0
        
        # Activity count
        act_count = await db.scalar(
            select(func.count(ActivityLog.id))
            .where(ActivityLog.workspace_id == ws_id, ActivityLog.user_id == current_user.id)
        )
        stats.recent_activity_count = act_count or 0

    completion_percentage = profile_service._calculate_completion(profile)
    profile_dict = DeveloperProfileResponse.model_validate(profile).model_dump()
    profile_dict["profile_completion_percentage"] = completion_percentage

    return EnterpriseProfileResponse(
        profile=DeveloperProfileResponse(**profile_dict),
        account=AccountInfo(
            user_id=current_user.id,
            email=current_user.email,
            account_type="ENTERPRISE",
            auth_method=auth_method,
            workspace_name=workspace_info,
            workspace_role=role,
            subscription_plan=plan,
            member_since=joined_at,
            last_login=current_user.last_login_at.isoformat() if current_user.last_login_at else None,
            account_status="ACTIVE" if current_user.is_active else "INACTIVE",
            email_verification_status=current_user.email_verified,
            avatar_url=current_user.avatar_url
        ),
        connected_accounts=ConnectedAccounts(
            google_connected="google" in providers,
            github_connected="github" in providers or bool(profile.github_user_id),
            gitlab_connected="gitlab" in providers,
            microsoft_connected="microsoft" in providers
        ),
        stats=stats
    )

@router.post("/me", response_model=DeveloperProfileResponse, status_code=status.HTTP_201_CREATED)
async def create_my_profile(
    *,
    db: SessionDep,
    current_user: CurrentUser,
    profile_in: DeveloperProfileCreate
):
    """
    Create a developer profile for the currently authenticated user.
    """
    try:
        profile = await profile_service.create_profile(
            db, user_id=current_user.id, obj_in=profile_in.model_dump(exclude_unset=True)
        )
        return profile
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.patch("/me", response_model=DeveloperProfileResponse)
async def update_my_profile(
    *,
    db: SessionDep,
    current_user: CurrentUser,
    profile_in: DeveloperProfileUpdate
):
    """
    Update the developer profile for the currently authenticated user.
    """
    profile = await profile_service.update_profile(
        db, user_id=current_user.id, obj_in=profile_in.model_dump(exclude_unset=True)
    )
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Developer profile not found"
        )
    return profile
