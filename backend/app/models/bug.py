import uuid
import enum
from sqlalchemy import String, Enum as SQLEnum, ForeignKey, Integer, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.base_model import AuditBase

class BugSource(str, enum.Enum):
    MANUAL = "MANUAL"
    API = "API"
    INTEGRATION = "INTEGRATION"

class BugState(str, enum.Enum):
    OPEN = "OPEN"
    ANALYZING = "ANALYZING"
    RECOMMENDATION_READY = "RECOMMENDATION_READY"
    ASSIGNED = "ASSIGNED"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"

class BugSeverity(str, enum.Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

class Bug(AuditBase):
    __tablename__ = "bugs"

    project_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True)
    source: Mapped[BugSource] = mapped_column(SQLEnum(BugSource), default=BugSource.MANUAL, nullable=False)
    external_ref: Mapped[str | None] = mapped_column(String, nullable=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    stack_trace: Mapped[str | None] = mapped_column(Text, nullable=True)
    
    state: Mapped[BugState] = mapped_column(SQLEnum(BugState), default=BugState.OPEN, nullable=False)
    severity: Mapped[BugSeverity] = mapped_column(SQLEnum(BugSeverity), default=BugSeverity.MEDIUM, nullable=False)
    category: Mapped[str | None] = mapped_column(String, nullable=True)
    
    duplicate_of: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("bugs.id", ondelete="SET NULL"), nullable=True)
    reported_by: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    
    resolved_at: Mapped[str | None] = mapped_column(DateTime(timezone=True), nullable=True)

class BugAttachment(AuditBase):
    __tablename__ = "bug_attachments"

    bug_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("bugs.id", ondelete="CASCADE"), nullable=False, index=True)
    s3_key: Mapped[str] = mapped_column(String, nullable=False)
    mime_type: Mapped[str] = mapped_column(String, nullable=False)
    size_bytes: Mapped[int] = mapped_column(Integer, nullable=False)
