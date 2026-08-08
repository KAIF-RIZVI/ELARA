import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.base_repository import BaseRepository
from app.models.identity import User, OAuthAccount

class RepositoryUser(BaseRepository[User]):
    async def get_by_email(self, db: AsyncSession, email: str) -> User | None:
        result = await db.execute(select(User).where(User.email == email))
        return result.scalars().first()
        
    async def get_by_oauth(self, db: AsyncSession, provider: str, provider_user_id: str) -> User | None:
        result = await db.execute(
            select(User).join(OAuthAccount).where(
                OAuthAccount.provider == provider,
                OAuthAccount.provider_user_id == provider_user_id
            )
        )
        return result.scalars().first()

user = RepositoryUser(User)
