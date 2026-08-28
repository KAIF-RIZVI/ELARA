from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.models.identity import UserSession
from app.core.security import generate_refresh_token, get_refresh_token_hash, verify_refresh_token, create_access_token
import uuid
from datetime import datetime, timedelta, timezone

class SessionService:
    async def create_session(self, db: AsyncSession, user_id: uuid.UUID, user_agent: str | None = None, ip_address: str | None = None) -> tuple[UserSession, str]:
        """
        Creates a new user session, generates an opaque refresh token, hashes it, and stores it.
        Returns the UserSession and the PLAINTEXT refresh token.
        """
        plain_refresh_token = generate_refresh_token()
        hashed_token = get_refresh_token_hash(plain_refresh_token)
        
        # Sliding expiration: 7 days
        expires_at = datetime.now(timezone.utc) + timedelta(days=7)
        
        session = UserSession(
            user_id=user_id,
            refresh_token_hash=hashed_token,
            user_agent=user_agent,
            ip_address=ip_address,
            expires_at=expires_at,
            is_revoked=False
        )
        
        db.add(session)
        await db.commit()
        await db.refresh(session)
        
        return session, plain_refresh_token
        
    async def rotate_refresh_token(self, db: AsyncSession, plain_refresh_token: str, session_id: uuid.UUID | None = None) -> tuple[str, str]:
        """
        Validates the incoming refresh token. If valid, burns the old one, generates a new one, and issues a new JWT.
        Implements strict rotation and family tracking (theft detection).
        Returns (new_jwt_access_token, new_plain_refresh_token)
        """
        if session_id:
            stmt = select(UserSession).where(UserSession.id == session_id)
        else:
            token_hash = get_refresh_token_hash(plain_refresh_token)
            stmt = select(UserSession).where(UserSession.refresh_token_hash == token_hash)
            
        result = await db.execute(stmt)
        session = result.scalar_one_or_none()
        
        if not session:
            raise ValueError("Session not found")
            
        if session.is_revoked:
            # Token theft detected! The session was revoked but someone is trying to use it.
            # In a full system, alert the user and revoke all other sessions.
            raise ValueError("Session is revoked. Potential token theft detected.")
            
        if session.expires_at.tzinfo is None:
            # Ensure timezone awareness if database strips it
            session.expires_at = session.expires_at.replace(tzinfo=timezone.utc)
            
        if session.expires_at < datetime.now(timezone.utc):
            raise ValueError("Refresh token expired")
            
        if not verify_refresh_token(plain_refresh_token, session.refresh_token_hash):
            # The refresh token provided doesn't match the one in the DB.
            # This is a critical security event. A token was used that doesn't match the active family token.
            # Revoke the session immediately.
            session.is_revoked = True
            await db.commit()
            raise ValueError("Invalid refresh token. Session revoked for security.")
            
        # Rotation: Valid token. Burn it and create a new one.
        new_plain_refresh_token = generate_refresh_token()
        session.refresh_token_hash = get_refresh_token_hash(new_plain_refresh_token)
        # Extend sliding window
        session.expires_at = datetime.now(timezone.utc) + timedelta(days=7)
        
        await db.commit()
        
        # Issue new JWT
        access_token = create_access_token(subject=session.user_id, session_id=session.id)
        
        return access_token, new_plain_refresh_token

    async def revoke_session(self, db: AsyncSession, session_id: uuid.UUID):
        """Revokes a session, effectively logging the user out."""
        await db.execute(
            update(UserSession)
            .where(UserSession.id == session_id)
            .values(is_revoked=True)
        )
        await db.commit()

session_service = SessionService()