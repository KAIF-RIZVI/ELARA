from typing import Any, Generic, Type, TypeVar, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.base_repository import BaseRepository
from app.core.base_model import Base

ModelType = TypeVar("ModelType", bound=Base)
RepoType = TypeVar("RepoType", bound=BaseRepository)

class BaseService(Generic[ModelType, RepoType]):
    def __init__(self, repository: RepoType):
        self.repository = repository

    async def get(self, db: AsyncSession, id: Any) -> ModelType | None:
        return await self.repository.get(db, id)

    async def get_multi(self, db: AsyncSession, *, skip: int = 0, limit: int = 100) -> Sequence[ModelType]:
        return await self.repository.get_multi(db, skip=skip, limit=limit)

    async def create(self, db: AsyncSession, *, obj_in: dict[str, Any]) -> ModelType:
        return await self.repository.create(db, obj_in=obj_in)

    async def update(self, db: AsyncSession, *, db_obj: ModelType, obj_in: dict[str, Any]) -> ModelType:
        return await self.repository.update(db, db_obj=db_obj, obj_in=obj_in)

    async def remove(self, db: AsyncSession, *, id: Any) -> ModelType | None:
        return await self.repository.remove(db, id=id)
