import uuid
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class RepositoryBase(BaseModel):
    provider: str
    full_name: str
    external_id: str
    default_branch: str = "main"

class RepositoryCreate(RepositoryBase):
    workspace_id: uuid.UUID

class RepositoryResponse(RepositoryBase):
    id: uuid.UUID
    workspace_id: uuid.UUID
    project_id: Optional[uuid.UUID]
    sync_status: str
    last_synced_at: Optional[datetime]

    class Config:
        from_attributes = True
