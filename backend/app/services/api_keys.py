import uuid
import secrets
import hashlib
import datetime
from typing import Sequence, Tuple, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.identity import APIKey
from app.models.workspace import ActivityLog

class APIKeyService:
    def _hash_key(self, raw_key: str) -> str:
        return hashlib.sha256(raw_key.encode()).hexdigest()

    async def create_key(
        self, db: AsyncSession, *, organization_id: Optional[uuid.UUID] = None, workspace_id: Optional[uuid.UUID] = None, name: str, user_id: uuid.UUID
    ) -> Tuple[APIKey, str]:
        if (organization_id is None) == (workspace_id is None):
            raise ValueError("API Key must belong to exactly one of Organization or Workspace.")

        random_part = secrets.token_urlsafe(32)
        raw_key = f"elara_live_{random_part}"
        prefix = raw_key[:15]
        key_hash = self._hash_key(raw_key)

        async with db.begin_nested():
            api_key = APIKey(
                workspace_id=workspace_id,
                organization_id=organization_id,
                name=name,
                prefix=prefix,
                key_hash=key_hash,
                created_by=user_id
            )
            db.add(api_key)
            
            activity = ActivityLog(
                workspace_id=workspace_id,
                organization_id=organization_id,
                action="API_KEY_CREATED",
                target=name,
                status="success",
                user_id=user_id
            )
            db.add(activity)
            
        await db.commit()
        await db.refresh(api_key)
        return api_key, raw_key

    async def list_keys(
        self, db: AsyncSession, *, organization_id: Optional[uuid.UUID] = None, workspace_id: Optional[uuid.UUID] = None
    ) -> Sequence[APIKey]:
        stmt = select(APIKey)
        if organization_id:
            stmt = stmt.where(APIKey.organization_id == organization_id)
        if workspace_id:
            stmt = stmt.where(APIKey.workspace_id == workspace_id)
        stmt = stmt.order_by(APIKey.created_at.desc())
        result = await db.execute(stmt)
        return result.scalars().all()

    async def revoke_key(
        self, db: AsyncSession, *, key_id: uuid.UUID, organization_id: Optional[uuid.UUID] = None, workspace_id: Optional[uuid.UUID] = None, user_id: uuid.UUID
    ) -> APIKey:
        stmt = select(APIKey).where(APIKey.id == key_id)
        if organization_id:
            stmt = stmt.where(APIKey.organization_id == organization_id)
        if workspace_id:
            stmt = stmt.where(APIKey.workspace_id == workspace_id)
            
        api_key = await db.scalar(stmt)
        if not api_key:
            raise ValueError("API Key not found or unauthorized.")
            
        if api_key.revoked_at:
            return api_key

        async with db.begin_nested():
            api_key.revoked_at = datetime.datetime.now(datetime.timezone.utc)
            
            activity = ActivityLog(
                workspace_id=workspace_id,
                organization_id=organization_id,
                action="API_KEY_REVOKED",
                target=api_key.name,
                status="success",
                user_id=user_id
            )
            db.add(activity)
            
        await db.commit()
        await db.refresh(api_key)
        return api_key

    async def verify_and_get_key(
        self, db: AsyncSession, *, raw_key: str
    ) -> Optional[APIKey]:
        key_hash = self._hash_key(raw_key)
        stmt = select(APIKey).where(
            APIKey.key_hash == key_hash,
            APIKey.revoked_at.is_(None)
        )
        api_key = await db.scalar(stmt)
        if not api_key:
            return None
            
        # Update last_used_at
        api_key.last_used_at = datetime.datetime.now(datetime.timezone.utc)
        await db.commit()
        return api_key

api_key_service = APIKeyService()
