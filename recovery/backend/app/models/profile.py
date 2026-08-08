import uuid
from sqlalchemy import String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import AuditBase

class DeveloperProfile(AuditBase):
    __tablename__ = "developer_profiles"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    
    company: Mapped[str | None] = mapped_column(String, nullable=True)
    organization: Mapped[str | None] = mapped_column(String, nullable=True)
    designation: Mapped[str | None] = mapped_column(String, nullable=True)
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
    skills: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    certifications: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    
    github_username: Mapped[str | None] = mapped_column(String, nullable=True)
    linkedin_url: Mapped[str | None] = mapped_column(String, nullable=True)
    portfolio_url: Mapped[str | None] = mapped_column(String, nullable=True)
    website: Mapped[str | None] = mapped_column(String, nullable=True)
    
    profile_completion_percentage: Mapped[int] = mapped_column(default=0, nullable=False)
    
    availability: Mapped[str | None] = mapped_column(String, nullable=True)
    available_for_assignment: Mapped[bool] = mapped_column(default=True, nullable=False)
    open_to_collaboration: Mapped[bool] = mapped_column(default=True, nullable=False)


class UserPreference(AuditBase):
    __tablename__ = "user_preferences"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    
    theme: Mapped[str | None] = mapped_column(String, nullable=True)
    color_scheme: Mapped[str | None] = mapped_column(String, nullable=True)
    language: Mapped[str | None] = mapped_column(String, nullable=True)
    timezone: Mapped[str | None] = mapped_column(String, nullable=True)
    
    sidebar_collapsed: Mapped[bool] = mapped_column(default=False, nullable=False)
    density: Mapped[str | None] = mapped_column(String, nullable=True)
    
    default_workspace: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="SET NULL"), nullable=True)
    default_dashboard: Mapped[str | None] = mapped_column(String, nullable=True)
    default_repository: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("repositories.id", ondelete="SET NULL"), nullable=True)
    
    email_notifications: Mapped[bool] = mapped_column(default=True, nullable=False)
    push_notifications: Mapped[bool] = mapped_column(default=True, nullable=False)
    
    notification_preferences: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    dashboard_layout: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    command_palette_preferences: Mapped[dict | None] = mapped_column(JSONB, nullable=True)


class UserOnboarding(AuditBase):
    __tablename__ = "user_onboarding"
    
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True, index=True)
    
    google_connected: Mapped[bool] = mapped_column(default=True, nullable=False)
    profile_completed: Mapped[bool] = mapped_column(default=False, nullable=False)
    github_connected: Mapped[bool] = mapped_column(default=False, nullable=False)
    repository_connected: Mapped[bool] = mapped_column(default=False, nullable=False)
    first_ai_scan: Mapped[bool] = mapped_column(default=False, nullable=False)
    onboarding_completed: Mapped[bool] = mapped_column(default=False, nullable=False)
