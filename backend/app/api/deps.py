from typing import Annotated, AsyncGenerator
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
import jwt

from app.core.database import get_db as db_get_db
from app.core.security import decode_access_token
from app.models.identity import User, WorkspaceMember, MemberRole
from app.models.organization import OrganizationMember, OrganizationRole
from app.services.user import user_service
import uuid
from sqlalchemy import select

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async for session in db_get_db():
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_db)]

async def get_current_user(
    request: Request, db: SessionDep
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    token = request.cookies.get("access_token")
    if not token:
        # Fallback to Authorization header if no cookie
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            
    if not token:
        raise credentials_exception
    
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

ROLE_HIERARCHY = {
    MemberRole.OWNER: 50,
    MemberRole.ADMIN: 40,
    MemberRole.MANAGER: 30,
    MemberRole.DEVELOPER: 20,
    MemberRole.SUPPORT: 10,
    MemberRole.VIEWER: 0
}

class RequireRole:
    """
    Dependency to enforce Role-Based Access Control (RBAC).
    Requires a `workspace_id` path parameter or query parameter.
    """
    def __init__(self, required_role: MemberRole):
        self.required_role = required_role

    async def __call__(self, workspace_id: uuid.UUID, db: SessionDep, current_user: CurrentUser):
        stmt = select(WorkspaceMember).where(
            WorkspaceMember.workspace_id == workspace_id,
            WorkspaceMember.user_id == current_user.id
        )
        result = await db.execute(stmt)
        member = result.scalar_one_or_none()

        if not member:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not a member of this workspace"
            )

        if ROLE_HIERARCHY[member.role] < ROLE_HIERARCHY[self.required_role]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Requires {self.required_role} role or higher"
            )

        return member

ORG_ROLE_HIERARCHY = {
    OrganizationRole.OWNER: 60,
    OrganizationRole.ADMIN: 50,
    OrganizationRole.PROJECT_MANAGER: 40,
    OrganizationRole.DEVELOPER: 30,
    OrganizationRole.QA_ENGINEER: 20,
    OrganizationRole.REPORTER: 10,
    OrganizationRole.VIEWER: 0
}

class RequireOrganizationRole:
    """
    Dependency to enforce Enterprise Role-Based Access Control (RBAC).
    Requires an `organization_id` path parameter or query parameter.
    """
    def __init__(self, required_role: OrganizationRole):
        self.required_role = required_role

    async def __call__(self, organization_id: uuid.UUID, db: SessionDep, current_user: CurrentUser):
        stmt = select(OrganizationMember).where(
            OrganizationMember.organization_id == organization_id,
            OrganizationMember.user_id == current_user.id,
            OrganizationMember.status == "ACTIVE"
        )
        result = await db.execute(stmt)
        member = result.scalar_one_or_none()

        if not member:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not a member of this organization"
            )

        if ORG_ROLE_HIERARCHY[member.role] < ORG_ROLE_HIERARCHY[self.required_role]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Requires {self.required_role} role or higher"
            )

        return member