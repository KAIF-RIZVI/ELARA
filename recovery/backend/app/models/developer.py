import uuid
from sqlalchemy import String, ForeignKey, Integer, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base_model import WorkspaceEntityBase

class DeveloperProfile(WorkspaceEntityBase):
    __tablename__ = "developer_profiles"

    member_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("workspace_members.id"), nullable=False, index=True)
    github_username: Mapped[str] = mapped_column(String, nullable=False)
    skills: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    open_assignments: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    availability: Mapped[float] = mapped_column(Float, default=1.0, nullable=False) # 0.0 to 1.0

class ExpertiseScore(WorkspaceEntityBase):
    __tablename__ = "expertise_scores"

    developer_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("developer_profiles.id"), nullable=False, index=True)
    repository_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("repositories.id"), nullable=False, index=True)
    module_path: Mapped[str] = mapped_column(String, nullable=False)
    
    ownership_score: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    recency_score: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    resolution_score: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    
    computed_at: Mapped[str | None] = mapped_column(String, nullable=True)
