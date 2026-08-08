from typing import Any
from pydantic import BaseModel, ConfigDict
import uuid
from app.models.workspace import WorkspaceStatus

class WorkspaceBase(BaseModel):
    name: str
    slug: str

class WorkspaceCreate(WorkspaceBase):
    settings: dict[str, Any] | None = None

class WorkspaceUpdate(BaseModel):
    name: str | None = None
    slug: str | None = None
    description: str | None = None
    settings: dict[str, Any] | None = None

class WorkspaceResponse(WorkspaceBase):
    id: uuid.UUID
    description: str | None = None
    logo_url: str | None = None
    status: WorkspaceStatus
    settings: dict[str, Any] | None
    created_at: Any | None = None

    model_config = ConfigDict(from_attributes=True)

class WorkspaceOverview(WorkspaceResponse):
    members_count: int = 0
    projects_count: int = 0
    repositories_count: int = 0
    ai_credits_remaining: int = 0
