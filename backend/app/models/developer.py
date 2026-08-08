import uuid
from sqlalchemy import String, ForeignKey, Integer, Float, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base_model import WorkspaceEntityBase, AuditBase

class DeveloperProfile(AuditBase):
    __tablename__ = "developer_profiles"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    
    # Identity
    first_name: Mapped[str | None] = mapped_column(String, nullable=True)
    last_name: Mapped[str | None] = mapped_column(String, nullable=True)
    display_name: Mapped[str | None] = mapped_column(String, nullable=True)
    username: Mapped[str | None] = mapped_column(String, nullable=True)
    
    company: Mapped[str | None] = mapped_column(String, nullable=True)
    organization: Mapped[str | None] = mapped_column(String, nullable=True)
    designation: Mapped[str | None] = mapped_column(String, nullable=True)
    primary_role: Mapped[str | None] = mapped_column(String, nullable=True)
    current_company: Mapped[str | None] = mapped_column(String, nullable=True)
    current_position: Mapped[str | None] = mapped_column(String, nullable=True)
    experience_years: Mapped[int | None] = mapped_column(Integer, nullable=True)
    
    bio: Mapped[str | None] = mapped_column(String, nullable=True)
    location: Mapped[str | None] = mapped_column(String, nullable=True)
    timezone: Mapped[str | None] = mapped_column(String, nullable=True)
    
    primary_language: Mapped[str | None] = mapped_column(String, nullable=True)
    preferred_languages: Mapped[str | None] = mapped_column(String, nullable=True)
    
    tech_stack: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    frameworks: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    databases: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    cloud_platforms: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    devops_tools: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    ai_ml_technologies: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    areas_of_expertise: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    skills: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    certifications: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    
    github_username: Mapped[str | None] = mapped_column(String, nullable=True)
    github_user_id: Mapped[str | None] = mapped_column(String, nullable=True)
    github_avatar_url: Mapped[str | None] = mapped_column(String, nullable=True)
    github_public_repos: Mapped[int | None] = mapped_column(Integer, nullable=True)
    github_profile_url: Mapped[str | None] = mapped_column(String, nullable=True)
    twitter_username: Mapped[str | None] = mapped_column(String, nullable=True)
    linkedin_url: Mapped[str | None] = mapped_column(String, nullable=True)
    portfolio_url: Mapped[str | None] = mapped_column(String, nullable=True)
    website: Mapped[str | None] = mapped_column(String, nullable=True)
    
    open_assignments: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    availability: Mapped[str | None] = mapped_column(String, nullable=True)
    available_for_assignment: Mapped[bool] = mapped_column(default=True, nullable=False)
    open_to_collaboration: Mapped[bool] = mapped_column(default=True, nullable=False)

class ExpertiseScore(WorkspaceEntityBase):
    __tablename__ = "expertise_scores"

    developer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("developer_profiles.id", ondelete="CASCADE"), nullable=False, index=True)
    repository_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("repositories.id", ondelete="CASCADE"), nullable=False, index=True)
    module_path: Mapped[str] = mapped_column(String, nullable=False)
    
    ownership_score: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    recency_score: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    resolution_score: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    
    computed_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)