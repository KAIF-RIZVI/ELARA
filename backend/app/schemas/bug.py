from typing import Any, Dict, Optional, List
from pydantic import BaseModel, ConfigDict, Field, constr
import uuid
from datetime import datetime

from app.models.bug import BugState, BugSeverity, BugPriority

class BugBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    priority: BugPriority = BugPriority.P2
    severity: BugSeverity = BugSeverity.MEDIUM
    
    project_id: Optional[uuid.UUID] = None
    repository_id: Optional[uuid.UUID] = None
    
    environment: Optional[Dict[str, Any]] = None
    reproduction_steps: Optional[str] = None
    expected_behavior: Optional[str] = None
    actual_behavior: Optional[str] = None
    reporter_metadata: Optional[Dict[str, Any]] = None
    
    category: Optional[str] = None
    external_ref: Optional[str] = None
    stack_trace: Optional[str] = None

class BugCreate(BugBase):
    pass

class BugIntakeCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    priority: BugPriority = BugPriority.P2
    severity: BugSeverity = BugSeverity.MEDIUM
    
    environment: Optional[Dict[str, Any]] = None
    reproduction_steps: Optional[str] = None
    expected_behavior: Optional[str] = None
    actual_behavior: Optional[str] = None
    reporter_metadata: Optional[Dict[str, Any]] = None


class BugUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, min_length=1)
    
    project_id: Optional[uuid.UUID] = None
    repository_id: Optional[uuid.UUID] = None
    
    environment: Optional[Dict[str, Any]] = None
    reproduction_steps: Optional[str] = None
    expected_behavior: Optional[str] = None
    actual_behavior: Optional[str] = None
    category: Optional[str] = None
    duplicate_of: Optional[uuid.UUID] = None
    stack_trace: Optional[str] = None

class BugStatusUpdate(BaseModel):
    state: BugState

class BugPriorityUpdate(BaseModel):
    priority: BugPriority

class BugAssignUpdate(BaseModel):
    developer_id: Optional[uuid.UUID] = None

class BugAssignmentResponse(BaseModel):
    id: uuid.UUID
    bug_id: uuid.UUID
    developer_id: uuid.UUID
    assigned_by: Optional[uuid.UUID] = None
    assigned_at: Optional[datetime] = None
    removed_at: Optional[datetime] = None
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class BugCommentCreate(BaseModel):
    body: str = Field(..., min_length=1)

class BugCommentResponse(BaseModel):
    id: uuid.UUID
    bug_id: uuid.UUID
    author_id: Optional[uuid.UUID] = None
    body: str
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class BugResponse(BugBase):
    id: uuid.UUID
    organization_id: uuid.UUID
    workspace_id: uuid.UUID
    state: BugState
    duplicate_of: Optional[uuid.UUID] = None
    reported_by: Optional[uuid.UUID] = None
    resolved_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime
    is_deleted: bool
    deleted_at: Optional[datetime] = None
    
    # Assignments can be joined but we can keep it simple here
    
    model_config = ConfigDict(from_attributes=True)


class BugAttachmentResponse(BaseModel):
    id: uuid.UUID
    bug_id: uuid.UUID
    s3_key: str
    mime_type: str
    size_bytes: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class ActivityLogResponse(BaseModel):
    id: uuid.UUID
    workspace_id: Optional[uuid.UUID] = None
    organization_id: Optional[uuid.UUID] = None
    bug_id: Optional[uuid.UUID] = None
    action: str
    target: str
    status: str
    user_id: Optional[uuid.UUID] = None
    metadata_payload: Optional[Dict[str, Any]] = None
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

