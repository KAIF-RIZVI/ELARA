import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.base_repository import BaseRepository
from app.models.identity import User

class RepositoryUser(BaseRepository[User]):
    async def get_by_email(self, db: AsyncSession, email: str) -> User | None:
        result = await db.execute(select(User).where(User.email == email))
        return result.scalars().first()

user = RepositoryUser(User)
