import uuid
import enum
from sqlalchemy import String, Enum as SQLEnum, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import WorkspaceEntityBase

class Project(WorkspaceEntityBase):
    __tablename__ = "projects"

    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)

class SyncStatus(str, enum.Enum):
    PENDING = "PENDING"
    SYNCING = "SYNCING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Repository(WorkspaceEntityBase):
    __tablename__ = "repositories"

    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id"), nullable=False, index=True)
    provider: Mapped[str] = mapped_column(String, nullable=False) # e.g. "github"
    external_id: Mapped[str] = mapped_column(String, nullable=False)
    full_name: Mapped[str] = mapped_column(String, nullable=False)
    default_branch: Mapped[str] = mapped_column(String, nullable=False, default="main")
    sync_status: Mapped[SyncStatus] = mapped_column(SQLEnum(SyncStatus), default=SyncStatus.PENDING, nullable=False)
    last_synced_at: Mapped[str | None] = mapped_column(String, nullable=True)

class JobStatus(str, enum.Enum):
    QUEUED = "QUEUED"
    IN_PROGRESS = "IN_PROGRESS"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"

class RepoIndexJob(WorkspaceEntityBase):
    __tablename__ = "repo_index_jobs"

    repository_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("repositories.id"), nullable=False, index=True)
    status: Mapped[JobStatus] = mapped_column(SQLEnum(JobStatus), default=JobStatus.QUEUED, nullable=False)
    commit_sha: Mapped[str] = mapped_column(String, nullable=False)
    files_indexed: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    error: Mapped[str | None] = mapped_column(String, nullable=True)
    started_at: Mapped[str | None] = mapped_column(String, nullable=True)
    finished_at: Mapped[str | None] = mapped_column(String, nullable=True)
