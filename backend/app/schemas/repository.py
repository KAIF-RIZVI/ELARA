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
    workspace_id: Optional[uuid.UUID] = None
    organization_id: Optional[uuid.UUID] = None
    provider_repository_id: Optional[str] = None
    github_installation_id: Optional[str] = None
    visibility: Optional[str] = None
    language: Optional[str] = None
    is_private: bool = False
    owner: Optional[str] = None
    clone_url: Optional[str] = None
    html_url: Optional[str] = None
    repository_size: Optional[int] = None
    stars: Optional[int] = 0
    forks: Optional[int] = 0
    open_issues: Optional[int] = 0
    archived: bool = False
    disabled: bool = False

class RepositoryResponse(RepositoryBase):
    id: uuid.UUID
    workspace_id: Optional[uuid.UUID]
    organization_id: Optional[uuid.UUID]
    project_id: Optional[uuid.UUID]
    provider_repository_id: Optional[str]
    github_installation_id: Optional[str]
    visibility: Optional[str]
    language: Optional[str]
    is_private: bool
    sync_status: str
    last_synced_at: Optional[datetime]
    
    owner: Optional[str]
    clone_url: Optional[str]
    html_url: Optional[str]
    last_push_at: Optional[datetime]
    repository_size: Optional[int]
    stars: Optional[int]
    forks: Optional[int]
    open_issues: Optional[int]
    archived: bool
    disabled: bool
    index_status: str
    ai_ready: bool
    
    # Calculated health score
    health_score: Optional[int] = None

    class Config:
        from_attributes = True
