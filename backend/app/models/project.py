import uuid
import enum
from sqlalchemy import String, Enum as SQLEnum, ForeignKey, Integer, DateTime, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import CheckConstraint, Boolean
from app.core.base_model import AuditBase

class ProjectStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    ON_HOLD = "ON_HOLD"

class Project(AuditBase):
    __tablename__ = "projects"

    organization_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    status: Mapped[ProjectStatus] = mapped_column(SQLEnum(ProjectStatus), default=ProjectStatus.ACTIVE, nullable=False)

    __table_args__ = (
        UniqueConstraint("organization_id", "name", name="uix_organization_project_name"),
    )

class SyncStatus(str, enum.Enum):
    PENDING = "PENDING"
    SYNCING = "SYNCING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Repository(AuditBase):
    __tablename__ = "repositories"

    workspace_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)
    organization_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=True, index=True)
    project_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"), nullable=True, index=True)
    
    provider: Mapped[str] = mapped_column(String, nullable=False) # e.g. "github"
    external_id: Mapped[str] = mapped_column(String, nullable=False)
    full_name: Mapped[str] = mapped_column(String, nullable=False)
    default_branch: Mapped[str] = mapped_column(String, nullable=False, default="main")
    
    provider_repository_id: Mapped[str | None] = mapped_column(String, nullable=True)
    github_installation_id: Mapped[str | None] = mapped_column(String, nullable=True)
    visibility: Mapped[str | None] = mapped_column(String, nullable=True)
    language: Mapped[str | None] = mapped_column(String, nullable=True)
    is_private: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    owner: Mapped[str | None] = mapped_column(String, nullable=True)
    clone_url: Mapped[str | None] = mapped_column(String, nullable=True)
    html_url: Mapped[str | None] = mapped_column(String, nullable=True)
    last_push_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    repository_size: Mapped[int | None] = mapped_column(Integer, nullable=True)
    stars: Mapped[int | None] = mapped_column(Integer, nullable=True, default=0)
    forks: Mapped[int | None] = mapped_column(Integer, nullable=True, default=0)
    open_issues: Mapped[int | None] = mapped_column(Integer, nullable=True, default=0)
    archived: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    disabled: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    index_status: Mapped[str] = mapped_column(String, default="UNINDEXED", nullable=False)
    ai_ready: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    __table_args__ = (
        UniqueConstraint("workspace_id", "full_name", name="uix_workspace_repo_fullname"),
        UniqueConstraint("workspace_id", "external_id", name="uix_workspace_repo_extid"),
        UniqueConstraint("organization_id", "full_name", name="uix_organization_repo_fullname"),
        UniqueConstraint("organization_id", "external_id", name="uix_organization_repo_extid"),
        CheckConstraint("(workspace_id IS NULL) <> (organization_id IS NULL)", name="chk_repo_owner"),
    )
    sync_status: Mapped[SyncStatus] = mapped_column(SQLEnum(SyncStatus), default=SyncStatus.PENDING, nullable=False)
    last_synced_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)

class JobStatus(str, enum.Enum):
    QUEUED = "QUEUED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"

class RepoIndexJob(AuditBase):
    __tablename__ = "repo_index_jobs"

    repository_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("repositories.id", ondelete="CASCADE"), nullable=False, index=True)
    status: Mapped[JobStatus] = mapped_column(SQLEnum(JobStatus), default=JobStatus.QUEUED, nullable=False)
    commit_sha: Mapped[str] = mapped_column(String, nullable=False)
    files_indexed: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    error: Mapped[str | None] = mapped_column(String, nullable=True)
    started_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)
    finished_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)