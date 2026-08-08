from typing import Annotated, AsyncGenerator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
import jwt

from app.core.database import async_session_maker
from app.core.security import decode_access_token
from app.models.identity import User
from app.services.user import user_service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_db)]

async def get_current_user(
    db: SessionDep, token: Annotated[str, Depends(oauth2_scheme)]
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception
        
    user_id: str = payload.get("sub")
    if user_id is None:
        raise credentials_exception
        
    user = await user_service.get(db, id=user_id)
    if user is None:
        raise credentials_exception
        
    return user

CurrentUser = Annotated[User, Depends(get_current_user)]
