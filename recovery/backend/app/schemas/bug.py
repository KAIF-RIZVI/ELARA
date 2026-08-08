from typing import Any
from pydantic import BaseModel, ConfigDict
import uuid
from app.models.bug import BugState, BugSeverity

class BugBase(BaseModel):
    title: str
    description: str
    severity: BugSeverity = BugSeverity.MEDIUM
    category: str | None = None

class BugCreate(BugBase):
    project_id: uuid.UUID
    external_ref: str | None = None
    stack_trace: str | None = None

class BugResponse(BugBase):
    id: uuid.UUID
    project_id: uuid.UUID
    state: BugState
    external_ref: str | None
    stack_trace: str | None
    duplicate_of: uuid.UUID | None
    reported_by: uuid.UUID | None

    model_config = ConfigDict(from_attributes=True)
