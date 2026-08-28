import uuid
import secrets
import hashlib
import datetime
from typing import Sequence, Tuple, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.identity import WorkspaceAPIKey
from app.models.workspace import ActivityLog

class APIKeyService:
    def _hash_key(self, raw_key: str) -> str:
        return hashlib.sha256(raw_key.encode()).hexdigest()

    async def create_workspace_key(
        self, db: AsyncSession, *, organization_id: uuid.UUID, workspace_id: uuid.UUID, name: str, user_id: uuid.UUID
    ) -> Tuple[WorkspaceAPIKey, str]:
        # Generate raw key
        random_part = secrets.token_urlsafe(32)
        raw_key = f"elara_live_{random_part}"
        prefix = raw_key[:15]
        key_hash = self._hash_key(raw_key)

        async with db.begin_nested():
            api_key = WorkspaceAPIKey(
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
                action="API_KEY_CREATED",
                target=name,
                status="success",
                user_id=user_id
            )
            db.add(activity)
            
        await db.commit()
        await db.refresh(api_key)
        return api_key, raw_key

    async def list_workspace_keys(
        self, db: AsyncSession, *, workspace_id: uuid.UUID
    ) -> Sequence[WorkspaceAPIKey]:
        stmt = select(WorkspaceAPIKey).where(
            WorkspaceAPIKey.workspace_id == workspace_id
        ).order_by(WorkspaceAPIKey.created_at.desc())
        result = await db.execute(stmt)
        return result.scalars().all()

    async def revoke_workspace_key(
        self, db: AsyncSession, *, key_id: uuid.UUID, workspace_id: uuid.UUID, user_id: uuid.UUID
    ) -> WorkspaceAPIKey:
        stmt = select(WorkspaceAPIKey).where(
            WorkspaceAPIKey.id == key_id,
            WorkspaceAPIKey.workspace_id == workspace_id
        )
        api_key = await db.scalar(stmt)
        if not api_key:
            raise ValueError("API Key not found or unauthorized.")
            
        if api_key.revoked_at:
            return api_key

        async with db.begin_nested():
            api_key.revoked_at = datetime.datetime.now(datetime.timezone.utc)
            
            activity = ActivityLog(
                workspace_id=workspace_id,
                action="API_KEY_REVOKED",
                target=api_key.name,
                status="success",
                user_id=user_id
            )
            db.add(activity)
            
        await db.commit()
        await db.refresh(api_key)
        return api_key

    async def verify_and_get_workspace_for_key(
        self, db: AsyncSession, *, raw_key: str
    ) -> Optional[WorkspaceAPIKey]:
        key_hash = self._hash_key(raw_key)
        stmt = select(WorkspaceAPIKey).where(
            WorkspaceAPIKey.key_hash == key_hash,
            WorkspaceAPIKey.revoked_at.is_(None)
        )
        api_key = await db.scalar(stmt)
        if not api_key:
            return None
            
        # Update last_used_at
        api_key.last_used_at = datetime.datetime.now(datetime.timezone.utc)
        await db.commit()
        await db.refresh(api_key)
        
        return api_key

api_key_service = APIKeyService()
