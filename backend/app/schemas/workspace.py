from typing import Any
from pydantic import BaseModel, ConfigDict
import uuid
from app.models.workspace import WorkspaceStatus

class WorkspaceBase(BaseModel):
    name: str
    slug: str

class WorkspaceCreate(WorkspaceBase):
    organization_id: uuid.UUID
    settings: dict[str, Any] | None = None

class WorkspaceUpdate(BaseModel):
    name: str | None = None
    slug: str | None = None
    description: str | None = None
    settings: dict[str, Any] | None = None

class WorkspaceResponse(WorkspaceBase):
    id: uuid.UUID
    organization_id: uuid.UUID | None = None
    description: str | None = None
    logo_url: str | None = None
    status: WorkspaceStatus
    settings: dict[str, Any] | None
    created_at: Any | None = None

    model_config = ConfigDict(from_attributes=True)

class WorkspaceOverview(WorkspaceResponse):
    members_count: int = 0
    repositories_count: int = 0
    ai_credits_remaining: int = 0

class ActivityLogResponse(BaseModel):
    id: uuid.UUID
    workspace_id: uuid.UUID | None = None
    organization_id: uuid.UUID | None = None
    bug_id: uuid.UUID | None = None
    action: str
    target: str
    status: str
    user_id: uuid.UUID | None = None
    metadata_payload: dict[str, Any] | None = None
    created_at: Any | None = None

    model_config = ConfigDict(from_attributes=True)
