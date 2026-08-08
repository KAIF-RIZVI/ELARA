from typing import Any, Generic, Type, TypeVar, Sequence
import uuid
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.base_model import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, id: Any) -> ModelType | None:
        result = await db.execute(select(self.model).where(self.model.id == id))
        return result.scalars().first()

    async def get_multi(
        self, db: AsyncSession, *, skip: int = 0, limit: int = 100
    ) -> Sequence[ModelType]:
        result = await db.execute(select(self.model).offset(skip).limit(limit))
        return result.scalars().all()
        
    async def get_count(self, db: AsyncSession) -> int:
        result = await db.execute(select(func.count(self.model.id)))
        return result.scalar_one()

    async def create(self, db: AsyncSession, *, obj_in: dict[str, Any]) -> ModelType:
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def update(self, db: AsyncSession, *, db_obj: ModelType, obj_in: dict[str, Any]) -> ModelType:
        for field, value in obj_in.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def remove(self, db: AsyncSession, *, id: Any) -> ModelType | None:
        obj = await self.get(db, id=id)
        if obj:
            await db.delete(obj)
            await db.commit()
        return obj

class WorkspaceEntityRepository(BaseRepository[ModelType]):
    async def get_by_workspace(
        self, db: AsyncSession, workspace_id: uuid.UUID, skip: int = 0, limit: int = 100
    ) -> Sequence[ModelType]:
        result = await db.execute(
            select(self.model)
            .where(self.model.workspace_id == workspace_id)
            .offset(skip)
            .limit(limit)
        )
        return result.scalars().all()

    async def get_count_by_workspace(self, db: AsyncSession, workspace_id: uuid.UUID) -> int:
        result = await db.execute(
            select(func.count(self.model.id))
            .where(self.model.workspace_id == workspace_id)
        )
        return result.scalar_one()
