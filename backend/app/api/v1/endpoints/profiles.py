from fastapi import APIRouter, Depends, HTTPException, status, Request, Response
from fastapi.responses import RedirectResponse
from typing import Any
import httpx
import secrets
import logging
from app.core.config import get_settings
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
        
    # Log the activity
    activity = ActivityLog(
        workspace_id=None,
        action="profile.updated",
        target="Updated developer profile details",
        status="success",
        user_id=current_user.id
    )
    db.add(activity)
    await db.commit()
    
    return profile

@router.get("/github/authorize")
async def github_authorize(request: Request):
    """Initiates GitHub OAuth flow to connect a profile."""
    settings = get_settings()
    if not settings.GITHUB_CLIENT_ID:
        raise HTTPException(status_code=500, detail="GITHUB_CLIENT_ID not configured")
    
    state = secrets.token_urlsafe(32)
    # The callback URI MUST match exactly what is registered in GitHub
    callback_uri = f"http://localhost:3000/api/v1/profiles/github/callback"
    
    url = f"https://github.com/login/oauth/authorize?client_id={settings.GITHUB_CLIENT_ID}&redirect_uri={callback_uri}&scope=read:user user:email&state={state}"
    
    response = RedirectResponse(url=url)
    response.set_cookie(key="github_oauth_state", value=state, httponly=True, max_age=600, samesite="lax")
    return response

@router.get("/github/callback")
async def github_callback(request: Request, code: str, state: str, db: SessionDep, current_user: CurrentUser):
    """Handles the GitHub OAuth callback, fetches user data, and links it."""
    cookie_state = request.cookies.get("github_oauth_state")
    if not cookie_state or cookie_state != state:
        raise HTTPException(status_code=400, detail="Invalid state token (CSRF check failed)")
        
    settings = get_settings()
    callback_uri = f"http://localhost:3000/api/v1/profiles/github/callback"
    
    async with httpx.AsyncClient() as client:
        # Exchange code for access token
        token_response = await client.post(
            "https://github.com/login/oauth/access_token",
            headers={"Accept": "application/json"},
            data={
                "client_id": settings.GITHUB_CLIENT_ID,
                "client_secret": settings.GITHUB_CLIENT_SECRET,
                "code": code,
                "redirect_uri": callback_uri,
            }
        )
        token_data = token_response.json()
        
        if "error" in token_data:
            raise HTTPException(status_code=400, detail=token_data.get("error_description", "Failed to get access token"))
            
        access_token = token_data.get("access_token")
        
        # Fetch user profile
        user_response = await client.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/vnd.github.v3+json"
            }
        )
        
        if not user_response.is_success:
            raise HTTPException(status_code=400, detail="Failed to fetch GitHub user data")
            
        github_user = user_response.json()
        
        # Fetch user emails
        email_response = await client.get(
            "https://api.github.com/user/emails",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/vnd.github.v3+json"
            }
        )
        github_email = github_user.get("email")
        if email_response.is_success:
            emails = email_response.json()
            primary_email = next((e["email"] for e in emails if e.get("primary")), None)
            if primary_email:
                github_email = primary_email

    # Link OAuthAccount
    oauth_result = await db.execute(select(OAuthAccount).where(OAuthAccount.provider == "github", OAuthAccount.user_id == current_user.id))
    oauth_account = oauth_result.scalar_one_or_none()
    
    if not oauth_account:
        oauth_account = OAuthAccount(
            user_id=current_user.id,
            provider="github",
            provider_user_id=str(github_user["id"]),
            email=github_email or "unknown@github.com",
            # Zero-Token Policy: Do NOT store access_token in the DB!
        )
        db.add(oauth_account)
    else:
        oauth_account.provider_user_id = str(github_user["id"])
        oauth_account.email = github_email or "unknown@github.com"
        
    # Update DeveloperProfile
    profile = await profile_service.get_by_user(db, user_id=current_user.id)
    if profile:
        profile.github_username = github_user.get("login")
        profile.github_user_id = str(github_user.get("id"))
        profile.github_avatar_url = github_user.get("avatar_url")
        profile.github_public_repos = github_user.get("public_repos")
        profile.github_profile_url = github_user.get("html_url")
        
    await db.commit()
    
    response = RedirectResponse(url="http://localhost:3000/dashboard/profile")
    response.delete_cookie("github_oauth_state")
    return response

@router.get("/github/callback")
async def github_callback(request: Request, code: str, state: str, db: SessionDep, current_user: CurrentUser):
    """Handles the GitHub OAuth callback, fetches user data, and links it."""
    cookie_state = request.cookies.get("github_oauth_state")
    if not cookie_state or cookie_state != state:
        raise HTTPException(status_code=400, detail="Invalid state token (CSRF check failed)")
        
    settings = get_settings()
    callback_uri = f"http://localhost:3000/api/v1/profiles/github/callback"
    
    async with httpx.AsyncClient() as client:
        # Exchange code for access token
        token_response = await client.post(
            "https://github.com/login/oauth/access_token",
            headers={"Accept": "application/json"},
            data={
                "client_id": settings.GITHUB_CLIENT_ID,
                "client_secret": settings.GITHUB_CLIENT_SECRET,
                "code": code,
                "redirect_uri": callback_uri,
            }
        )
        token_data = token_response.json()
        
        if "error" in token_data:
            raise HTTPException(status_code=400, detail=token_data.get("error_description", "Failed to get access token"))
            
        access_token = token_data.get("access_token")
        
        # Fetch user profile
        user_response = await client.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/vnd.github.v3+json"
            }
        )
        
        if not user_response.is_success:
            raise HTTPException(status_code=400, detail="Failed to fetch GitHub user data")
            
        github_user = user_response.json()
        
        # Fetch user emails
        email_response = await client.get(
            "https://api.github.com/user/emails",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Accept": "application/vnd.github.v3+json"
            }
        )
        github_email = github_user.get("email")
        if email_response.is_success:
            emails = email_response.json()
            primary_email = next((e["email"] for e in emails if e.get("primary")), None)
            if primary_email:
                github_email = primary_email

    # Link OAuthAccount
    oauth_result = await db.execute(select(OAuthAccount).where(OAuthAccount.provider == "github", OAuthAccount.user_id == current_user.id))
    oauth_account = oauth_result.scalar_one_or_none()
    
    if not oauth_account:
        oauth_account = OAuthAccount(
            user_id=current_user.id,
            provider="github",
            provider_user_id=str(github_user["id"]),
            email=github_email or "unknown@github.com",
            # Zero-Token Policy: Do NOT store access_token in the DB!
        )
        db.add(oauth_account)
    else:
        oauth_account.provider_user_id = str(github_user["id"])
        oauth_account.email = github_email or "unknown@github.com"
        
    # Update DeveloperProfile
    profile = await profile_service.get_by_user(db, user_id=current_user.id)
    if profile:
        profile.github_username = github_user.get("login")
        profile.github_user_id = str(github_user.get("id"))
        profile.github_avatar_url = github_user.get("avatar_url")
        profile.github_public_repos = github_user.get("public_repos")
        profile.github_profile_url = github_user.get("html_url")
        
    await db.commit()
    
    response = RedirectResponse(url="http://localhost:3000/dashboard/profile")
    response.delete_cookie("github_oauth_state")
    return response

@router.delete("/github/disconnect")
async def github_disconnect(db: SessionDep, current_user: CurrentUser):
    """Disconnects GitHub profile integration."""
    # Delete OAuthAccount
    await db.execute(
        OAuthAccount.__table__.delete().where(
            OAuthAccount.user_id == current_user.id, 
            OAuthAccount.provider == "github"
        )
    )
    
    # Clear DeveloperProfile fields
    profile = await profile_service.get_by_user(db, user_id=current_user.id)
    if profile:
        profile.github_username = None
        profile.github_user_id = None
        profile.github_avatar_url = None
        profile.github_public_repos = None
        profile.github_profile_url = None
        
    await db.commit()
    return {"message": "GitHub account disconnected successfully"}
