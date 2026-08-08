from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status, Request, Response
from fastapi.responses import RedirectResponse
from app.api.deps import SessionDep, CurrentUser
from app.core.security import create_access_token
from app.core.config import get_settings
from app.services.user import user_service
from app.services.session_service import session_service
from app.schemas.user import Token, UserCreate, UserResponse
import uuid
import httpx
import secrets
import hashlib
import base64
import logging
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

router = APIRouter()
settings = get_settings()
logger = logging.getLogger(__name__)

# Note: We read GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET from settings
# The redirect URI must match exactly what is registered in Google Cloud Console
REDIRECT_URI = "http://localhost:8000/api/v1/auth/google/callback"

@router.get("/google/login")
async def google_login(response: Response):
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
        f"redirect_uri={REDIRECT_URI}&"
        f"scope=openid%20email%20profile&"
        f"state={state}&"
        f"code_challenge={code_challenge}&"
        f"code_challenge_method=S256"
    )
    
    res = RedirectResponse(url=auth_url)
    # Set temp cookies for validation in callback
    res.set_cookie("oauth_state", state, httponly=True, secure=True, max_age=300, samesite="lax")
    res.set_cookie("oauth_verifier", code_verifier, httponly=True, secure=True, max_age=300, samesite="lax")
    return res

@router.get("/google/callback")
async def google_callback(db: SessionDep, request: Request, response: Response, code: str = None, state: str = None, error: str = None):
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
        "redirect_uri": REDIRECT_URI,
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
    
    if not google_sub or not google_email:
        raise HTTPException(status_code=400, detail="Incomplete profile returned from Google")
    
    # 3. Match existing user by (provider, sub)
    user = await user_service.get_by_oauth(db, provider="google", subject_id=google_sub)
    
    if not user:
        # Fallback: Check if user exists by email to link account (Optional, but safe for enterprise)
        user = await user_service.repository.get_by_email(db, google_email)
        if user:
            from app.models.identity import OAuthAccount
            oauth_account = OAuthAccount(
                user_id=user.id,
                provider="google",
                provider_subject_id=google_sub,
                email=google_email
            )
            db.add(oauth_account)
            await db.commit()
        else:
            # Create JIT user along with default workspace, wallet, subscription
            user = await user_service.create_user(
                db, 
                email=google_email, 
                name=google_name or "Enterprise User", 
                auth_provider="google",
                provider_subject_id=google_sub
            )
        
    # 4. Create Session
    user_agent = request.headers.get("user-agent")
    ip_address = request.client.host if request.client else None
    
    session, refresh_token = await session_service.create_session(db, user.id, user_agent, ip_address)
    
    # 5. Generate 15-min JWT
    access_token = create_access_token(subject=user.id, session_id=session.id)
    
    # 6. Set HttpOnly Cookies and clear OAuth temp cookies
    res = RedirectResponse(url="http://localhost:3000/dashboard", status_code=status.HTTP_302_FOUND)
    res.set_cookie(key="access_token", value=access_token, httponly=True, secure=True, samesite="lax", max_age=900)
    res.set_cookie(key="refresh_token", value=refresh_token, httponly=True, secure=True, samesite="lax", max_age=604800)
    res.delete_cookie("oauth_state")
    res.delete_cookie("oauth_verifier")
    
    logger.info(f"User {user.id} logged in successfully via Google OAuth")
    return res

@router.post("/refresh")
async def refresh_token(db: SessionDep, request: Request, response: Response):
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
        
        response.set_cookie(key="access_token", value=new_access, httponly=True, secure=True, samesite="lax", max_age=900)
        response.set_cookie(key="refresh_token", value=new_refresh, httponly=True, secure=True, samesite="lax", max_age=604800)
        
        return {"message": "Tokens rotated"}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.post("/logout")
async def logout(db: SessionDep, request: Request, response: Response):
    """Implements proper logout by clearing cookies and revoking session in DB."""
    old_access = request.cookies.get("access_token")
    if old_access:
        import jwt
        try:
            unverified = jwt.decode(old_access, options={"verify_signature": False})
            session_id = unverified.get("sid")
            if session_id:
                await session_service.revoke_session(db, session_id)
        except Exception:
            pass
            
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return {"message": "Successfully logged out"}
