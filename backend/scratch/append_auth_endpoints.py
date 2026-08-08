import os

ENDPOINTS = """
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

"""

auth_path = "app/api/v1/endpoints/auth.py"
with open(auth_path, "a") as f:
    f.write(ENDPOINTS)

print("Endpoints appended!")
