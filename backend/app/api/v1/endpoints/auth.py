from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status, Request, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from app.api.deps import SessionDep, CurrentUser
from app.core.security import create_access_token, generate_verification_token, get_verification_token_hash
from app.services.email_service import email_service
from app.models.identity import EmailVerificationToken, PasswordResetToken
from datetime import datetime, timezone, timedelta
from app.core.config import get_settings
from app.services.user import user_service
from app.services.session_service import session_service
from app.services.activity import activity_service
from app.schemas.user import Token, UserCreate, UserResponse
import uuid
import httpx
import secrets
import hashlib
import base64
import logging
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from app.core.rate_limit import limiter

router = APIRouter()
settings = get_settings()
logger = logging.getLogger(__name__)

# Note: We read GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET from settings
# The redirect URI must match exactly what is registered in Google Cloud Console
# We use settings.GOOGLE_REDIRECT_URI for environments

@router.get("/google/login")
@limiter.limit("5/minute")
async def google_login(request: Request, response: Response):
    """Redirects the user to Google OAuth consent screen with PKCE."""
    if not settings.GOOGLE_CLIENT_ID:
        raise HTTPException(status_code=500, detail="GOOGLE_CLIENT_ID not configured")

    # Generate PKCE code verifier and challenge
    code_verifier = secrets.token_urlsafe(64)
    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode('ascii')).digest()
    ).decode('ascii').rstrip('=')
    
    # Generate CSRF state
    state = secrets.token_urlsafe(32)
    
    auth_url = (
        f"https://accounts.google.com/o/oauth2/v2/auth?"
        f"response_type=code&"
        f"client_id={settings.GOOGLE_CLIENT_ID}&"
        f"redirect_uri={settings.GOOGLE_REDIRECT_URI}&"
        f"scope=openid%20email%20profile&"
        f"state={state}&"
        f"code_challenge={code_challenge}&"
        f"code_challenge_method=S256"
    )
    
    res = RedirectResponse(url=auth_url)
    # Set temp cookies for validation in callback
    is_prod = settings.ENVIRONMENT == "production"
    res.set_cookie("oauth_state", state, httponly=True, secure=is_prod, max_age=300, samesite="lax")
    res.set_cookie("oauth_verifier", code_verifier, httponly=True, secure=is_prod, max_age=300, samesite="lax")
    return res

@router.get("/google/callback")
@limiter.limit("5/minute")
async def google_callback(request: Request, response: Response, db: SessionDep, code: str = None, state: str = None, error: str = None):
    """
    Exchanges the authorization code for an ID token, verifies it, 
    resolves the user, creates a session, and sets HttpOnly cookies.
    """
    if error:
        logger.error(f"Google OAuth Error: {error}")
        raise HTTPException(status_code=400, detail=f"Google OAuth error: {error}")
        
    if not code or not state:
        raise HTTPException(status_code=400, detail="Missing code or state parameter")
    
    saved_state = request.cookies.get("oauth_state")
    saved_verifier = request.cookies.get("oauth_verifier")
    
    if not saved_state or not saved_verifier:
        logger.error("Missing PKCE or state cookies")
        raise HTTPException(status_code=400, detail="Session expired. Please try logging in again.")
        
    if state != saved_state:
        logger.error("State mismatch in OAuth callback")
        raise HTTPException(status_code=400, detail="Invalid state parameter. CSRF attempt detected.")
        
    # 1. Exchange code for token
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "code": code,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "code_verifier": saved_verifier
    }
    
    async with httpx.AsyncClient() as client:
        try:
            token_res = await client.post(token_url, data=data)
            token_res.raise_for_status()
            token_data = token_res.json()
        except httpx.HTTPError as e:
            logger.error(f"Network error during code exchange: {str(e)}")
            raise HTTPException(status_code=502, detail="Failed to communicate with Google authentication servers")
        except Exception as e:
            logger.error(f"Error exchanging authorization code: {str(e)}")
            raise HTTPException(status_code=400, detail="Invalid or expired authorization code")
            
    id_token_jwt = token_data.get("id_token")
    if not id_token_jwt:
        logger.error("No id_token received from Google")
        raise HTTPException(status_code=400, detail="No ID token provided by Google")
        
    # 2. Cryptographically Verify ID token
    try:
        # verify_oauth2_token verifies signature, audience (aud), expiration (exp), and issuer (iss)
        id_info = id_token.verify_oauth2_token(
            id_token_jwt, google_requests.Request(), settings.GOOGLE_CLIENT_ID
        )
    except ValueError as e:
        logger.error(f"ID Token validation failed: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid Google ID token")
        
    google_sub = id_info.get("sub")
    google_email = id_info.get("email")
    google_name = id_info.get("name")
    google_picture = id_info.get("picture")
    
    if not google_sub or not google_email:
        raise HTTPException(status_code=400, detail="Incomplete profile returned from Google")
    
    # 3. Match existing user by (provider, provider_user_id)
    user = await user_service.get_by_oauth(db, provider="google", provider_user_id=google_sub)
    
    if not user:
        # Fallback: Check if user exists by email to link account (Optional, but safe for enterprise)
        user = await user_service.repository.get_by_email(db, google_email)
        if user:
            from app.models.identity import OAuthAccount
            oauth_account = OAuthAccount(
                user_id=user.id,
                provider="google",
                provider_user_id=google_sub,
                email=google_email
            )
            db.add(oauth_account)
            await db.commit()
        else:
            # Create JIT user along with default workspace, wallet, subscription
            user = await user_service.create_user(
                db, 
                email=google_email, 
                full_name=google_name or "Enterprise User", 
                auth_provider="google",
                provider_user_id=google_sub,
                email_verified=True
            )
            
    # Always synchronize latest Google avatar picture on login
    if google_picture and user.avatar_url != google_picture:
        user.avatar_url = google_picture
        db.add(user)
        await db.commit()
        await db.refresh(user)

    # 4. Create Session
    user_agent = request.headers.get("user-agent")
    ip_address = request.client.host if request.client else None
    
    session, refresh_token = await session_service.create_session(db, user.id, user_agent, ip_address)
    
    # 5. Generate 15-min JWT
    access_token = create_access_token(subject=user.id, session_id=session.id)
    
    # 6. Set HttpOnly Cookies and clear OAuth temp cookies
    is_prod = settings.ENVIRONMENT == "production"
    res = RedirectResponse(url="http://localhost:3000/dashboard", status_code=status.HTTP_302_FOUND)
    res.set_cookie(key="access_token", value=access_token, httponly=True, secure=is_prod, samesite="lax", max_age=900)
    res.set_cookie(key="refresh_token", value=refresh_token, httponly=True, secure=is_prod, samesite="lax", max_age=604800)
    res.delete_cookie("oauth_state")
    res.delete_cookie("oauth_verifier")
    
    # Audit Logging for SOC 2
    await activity_service.log_activity(
        db, 
        action="auth.login.success", 
        target="System", 
        user_id=user.id
    )
    
    logger.info(f"User {user.id} logged in successfully via Google OAuth")
    return res

@router.post("/register", response_model=UserResponse)
@limiter.limit("5/minute")
async def register_user(request: Request, user_in: UserCreate, db: SessionDep):
    """
    Register a new user with standard email and password.
    """
    try:
        user = await user_service.create_user(
            db, 
            email=user_in.email, 
            full_name=user_in.full_name, 
            password=user_in.password,
            auth_provider="email",
            email_verified=False
        )
        await db.flush()
        
        token = generate_verification_token()
        token_hash = get_verification_token_hash(token)
        
        verification_token = EmailVerificationToken(
            user_id=user.id,
            token_hash=token_hash,
            expires_at=datetime.now(timezone.utc) + timedelta(hours=24)
        )
        db.add(verification_token)
        await db.commit()
        await db.refresh(user)
        
        try:
            await email_service.send_verification_email(user.email, user.full_name, token)
        except Exception as e:
            logger.error(f"Failed to send verification email: {e}")
            # Do not fail registration if email fails to send. They can resend.
        return user
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=Token)
@limiter.limit("10/minute")
async def login_access_token(
    request: Request,
    response: Response,
    db: SessionDep,
    form_data: OAuth2PasswordRequestForm = Depends()
) -> Token:
    """
    OAuth2 compatible token login, get an access token for future requests.
    """
    from app.repositories.user import user as user_repo
    from app.core.security import verify_password
    
    user = await user_repo.get_by_email(db, email=form_data.username)
    if not user or not user.password_hash:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
        
    if not user.email_verified:
        raise HTTPException(
            status_code=403, 
            detail="Please verify your email address before signing in.",
            headers={"X-Error-Code": "unverified_email"}
        )
    
    user_agent = request.headers.get("user-agent")
    ip_address = request.client.host if request.client else None
    
    session, refresh_token = await session_service.create_session(db, user.id, user_agent, ip_address)
    access_token = create_access_token(subject=user.id, session_id=session.id)
    
    is_prod = settings.ENVIRONMENT == "production"
    response.set_cookie(key="access_token", value=access_token, httponly=True, secure=is_prod, samesite="lax", max_age=900)
    response.set_cookie(key="refresh_token", value=refresh_token, httponly=True, secure=is_prod, samesite="lax", max_age=604800)
    
    # Audit Logging for SOC 2
    await activity_service.log_activity(
        db, 
        action="auth.login.success", 
        target="System", 
        user_id=user.id
    )
    
    return Token(access_token=access_token, token_type="bearer")

@router.post("/refresh")
@limiter.limit("10/minute")
async def refresh_token(request: Request, response: Response, db: SessionDep):
    """Rotates the refresh token and issues a new access token."""
    token = request.cookies.get("refresh_token")
    if not token:
        raise HTTPException(status_code=401, detail="Refresh token missing")
        
    # We would also extract the session_id from the expired access_token's unverified payload to look it up.
    old_access = request.cookies.get("access_token")
    session_id = None
    if old_access:
        import jwt
        try:
            unverified = jwt.decode(old_access, options={"verify_signature": False})
            session_id = unverified.get("sid")
        except Exception:
            pass
            
    if not session_id:
        raise HTTPException(status_code=401, detail="Could not determine session ID")
    
    try:
        new_access, new_refresh = await session_service.rotate_refresh_token(db, session_id, token)
        
        is_prod = settings.ENVIRONMENT == "production"
        response.set_cookie(key="access_token", value=new_access, httponly=True, secure=is_prod, samesite="lax", max_age=900)
        response.set_cookie(key="refresh_token", value=new_refresh, httponly=True, secure=is_prod, samesite="lax", max_age=604800)
        
        return {"message": "Tokens rotated"}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/logout")
@limiter.limit("10/minute")
async def logout(request: Request, response: Response, db: SessionDep):
    """Implements proper logout by clearing cookies and revoking session in DB."""
    old_access = request.cookies.get("access_token")
    if old_access:
        import jwt
        try:
            unverified = jwt.decode(old_access, options={"verify_signature": False})
            session_id = unverified.get("sid")
            if session_id:
                await session_service.revoke_session(db, session_id)
                user_id = unverified.get("sub")
                if user_id:
                    await activity_service.log_activity(
                        db, 
                        action="auth.logout.success", 
                        target="System", 
                        user_id=uuid.UUID(user_id)
                    )
        except Exception:
            pass
            
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return {"message": "Successfully logged out"}

from pydantic import BaseModel

@router.post("/verify-email")
@limiter.limit("5/minute")
async def verify_email(request: Request, token: str, db: SessionDep):
    from sqlalchemy import select
    from app.core.security import get_verification_token_hash
    from app.repositories.user import user as user_repo
    
    token_hash = get_verification_token_hash(token)
    
    result = await db.execute(
        select(EmailVerificationToken).where(EmailVerificationToken.token_hash == token_hash)
    )
    verification_token = result.scalar_one_or_none()
    
    if not verification_token:
        raise HTTPException(status_code=400, detail="Invalid verification link.")
        
    if verification_token.used_at:
        raise HTTPException(status_code=400, detail="This verification link has already been used.")
        
    if verification_token.expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=400, detail="This verification link has expired.")
        
    user = await user_repo.get(db, id=verification_token.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
        
    # Mark verified
    user.email_verified = True
    user.email_verified_at = datetime.now(timezone.utc)
    db.add(user)
    
    # Mark token used
    verification_token.used_at = datetime.now(timezone.utc)
    db.add(verification_token)
    
    await db.commit()
    return {"message": "Email verified successfully."}


class EmailRequest(BaseModel):
    email: str

@router.post("/resend-verification")
@limiter.limit("3/minute")
async def resend_verification(request: Request, body: EmailRequest, db: SessionDep):
    from app.repositories.user import user as user_repo
    
    user = await user_repo.get_by_email(db, email=body.email)
    if not user or user.email_verified:
        # Return success even if invalid to prevent email enumeration
        return {"message": "If your email is unregistered or unverified, a new link has been sent."}
        
    token = generate_verification_token()
    token_hash = get_verification_token_hash(token)
    
    verification_token = EmailVerificationToken(
        user_id=user.id,
        token_hash=token_hash,
        expires_at=datetime.now(timezone.utc) + timedelta(hours=24)
    )
    db.add(verification_token)
    await db.commit()
    
    try:
        await email_service.send_verification_email(user.email, user.full_name, token)
    except Exception as e:
        logger.error(f"Failed to send verification email: {e}")
        
    return {"message": "If your email is unregistered or unverified, a new link has been sent."}


@router.post("/forgot-password")
@limiter.limit("3/minute")
async def forgot_password(request: Request, body: EmailRequest, db: SessionDep):
    from app.repositories.user import user as user_repo
    
    user = await user_repo.get_by_email(db, email=body.email)
    if not user:
        # Prevent email enumeration
        return {"message": "If that email exists, a password reset link has been sent."}
        
    token = generate_verification_token()
    token_hash = get_verification_token_hash(token)
    
    reset_token = PasswordResetToken(
        user_id=user.id,
        token_hash=token_hash,
        expires_at=datetime.now(timezone.utc) + timedelta(hours=1)
    )
    db.add(reset_token)
    await db.commit()
    
    try:
        await email_service.send_password_reset_email(user.email, user.full_name, token)
    except Exception as e:
        logger.error(f"Failed to send reset email: {e}")
        
    return {"message": "If that email exists, a password reset link has been sent."}


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str

@router.post("/reset-password")
@limiter.limit("5/minute")
async def reset_password(request: Request, body: ResetPasswordRequest, db: SessionDep):
    from sqlalchemy import select
    from app.core.security import get_verification_token_hash, get_password_hash
    from app.repositories.user import user as user_repo
    
    token_hash = get_verification_token_hash(body.token)
    
    result = await db.execute(
        select(PasswordResetToken).where(PasswordResetToken.token_hash == token_hash)
    )
    reset_token = result.scalar_one_or_none()
    
    if not reset_token:
        raise HTTPException(status_code=400, detail="Invalid password reset link.")
        
    if reset_token.used_at:
        raise HTTPException(status_code=400, detail="This password reset link has already been used.")
        
    if reset_token.expires_at < datetime.now(timezone.utc):
        raise HTTPException(status_code=400, detail="This password reset link has expired.")
        
    user = await user_repo.get(db, id=reset_token.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
        
    # Update password
    user.password_hash = get_password_hash(body.new_password)
    db.add(user)
    
    # Mark token used
    reset_token.used_at = datetime.now(timezone.utc)
    db.add(reset_token)
    
    # Revoke all sessions
    from app.models.identity import UserSession
    from sqlalchemy import update
    await db.execute(
        update(UserSession)
        .where(UserSession.user_id == user.id)
        .values(revoked_at=datetime.now(timezone.utc))
    )
    
    await db.commit()
    return {"message": "Password has been successfully reset."}

