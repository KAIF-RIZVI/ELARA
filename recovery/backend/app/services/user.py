from sqlalchemy.ext.asyncio import AsyncSession
from app.core.base_service import BaseService
from app.models.identity import User
from app.repositories.user import RepositoryUser, user as user_repo
from app.core.security import get_password_hash

class UserService(BaseService[User, RepositoryUser]):
    async def create_user(self, db: AsyncSession, *, email: str, name: str, password: str | None = None, auth_provider: str = "google") -> User:
        # Check if email exists
        existing = await self.repository.get_by_email(db, email)
        if existing:
            raise ValueError(f"User with email {email} already exists.")
        
        obj_in = {
            "email": email,
            "name": name,
            "auth_provider": auth_provider,
            "password_hash": get_password_hash(password) if password else None
        }
        return await self.create(db, obj_in=obj_in)

user_service = UserService(repository=user_repo)
