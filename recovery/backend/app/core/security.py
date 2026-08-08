from datetime import datetime, timedelta, timezone
from typing import Any
import jwt
import secrets
import string
from passlib.context import CryptContext
from app.core.config import get_settings

settings = get_settings()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = settings.JWT_ALGORITHM

def create_access_token(subject: str | Any, session_id: str | Any, expires_delta: timedelta | None = None) -> str:
    # Strictly 15 minutes for Enterprise
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    
    to_encode = {
        "exp": expire, 
        "sub": str(subject),
        "sid": str(session_id),
        "iss": "elara-auth"
    }
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str) -> dict[str, Any] | None:
    try:
        decoded = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[ALGORITHM], issuer="elara-auth")
        return decoded
    except jwt.InvalidTokenError:
        return None

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def generate_refresh_token() -> str:
    """Generate a secure, opaque random string for a refresh token."""
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(64))

def get_refresh_token_hash(token: str) -> str:
    """Hash the refresh token before storing it in DB."""
    return get_password_hash(token)

def verify_refresh_token(plain_token: str, hashed_token: str) -> bool:
    """Verify an opaque refresh token."""
    return verify_password(plain_token, hashed_token)
