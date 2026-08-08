from pydantic import BaseModel, ConfigDict, Field
from typing import Any
import uuid

class DeveloperProfileBase(BaseModel):
    bio: str | None = None
    company: str | None = None
    designation: str | None = None
    experience_years: int | None = Field(default=None, ge=0, le=50)
    location: str | None = None
    timezone: str | None = None
    
    primary_language: str | None = None
    preferred_languages: str | None = None
    
    github_username: str | None = None
    linkedin_url: str | None = None
    portfolio_url: str | None = None
    website: str | None = None
    
    tech_stack: dict[str, Any] | None = None
    frameworks: dict[str, Any] | None = None
    skills: dict[str, Any] | None = None
    certifications: dict[str, Any] | None = None

class DeveloperProfileCreate(DeveloperProfileBase):
    pass

class DeveloperProfileUpdate(DeveloperProfileBase):
    pass

class DeveloperProfileResponse(DeveloperProfileBase):
    id: uuid.UUID
    user_id: uuid.UUID
    profile_completion_percentage: int
    open_assignments: int
    availability: str | None = None
    available_for_assignment: bool
    open_to_collaboration: bool
    
    model_config = ConfigDict(from_attributes=True)