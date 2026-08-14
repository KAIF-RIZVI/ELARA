from pydantic import BaseModel, ConfigDict
import uuid
from datetime import datetime
from app.models.project import ProjectStatus

class ProjectBase(BaseModel):
    name: str
    description: str | None = None
    status: ProjectStatus = ProjectStatus.ACTIVE

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    status: ProjectStatus | None = None

class ProjectResponse(ProjectBase):
    id: uuid.UUID
    organization_id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    
    # UI joined fields
    repositories_count: int = 0
    members_count: int = 0
    owner_name: str | None = None

    model_config = ConfigDict(from_attributes=True)