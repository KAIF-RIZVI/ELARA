from typing import Any
from pydantic import BaseModel, ConfigDict
import uuid
from app.models.workspace import WorkspaceStatus

class WorkspaceBase(BaseModel):
    name: str
    slug: str

class WorkspaceCreate(WorkspaceBase):
    settings: dict[str, Any] | None = None

class WorkspaceResponse(WorkspaceBase):
    id: uuid.UUID
    status: WorkspaceStatus
    settings: dict[str, Any] | None

    model_config = ConfigDict(from_attributes=True)
