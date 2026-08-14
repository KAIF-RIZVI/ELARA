import uuid
import enum
from datetime import datetime
from sqlalchemy import String, ForeignKey, Enum as SQLEnum, Boolean, DateTime
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base_model import AuditBase

class NotificationType(str, enum.Enum):
    # Organization
    JOIN_REQUEST = "JOIN_REQUEST"
    JOIN_APPROVED = "JOIN_APPROVED"
    JOIN_REJECTED = "JOIN_REJECTED"
    ORGANIZATION_INVITATION = "ORGANIZATION_INVITATION"
    ROLE_CHANGED = "ROLE_CHANGED"
    
    # Projects
    PROJECT_INVITED = "PROJECT_INVITED"
    PROJECT_CREATED = "PROJECT_CREATED"
    
    # Repositories
    REPOSITORY_CONNECTED = "REPOSITORY_CONNECTED"
    REPOSITORY_SYNC_FAILED = "REPOSITORY_SYNC_FAILED"
    
    # Bug Triage
    BUG_ASSIGNED = "BUG_ASSIGNED"
    BUG_STATUS_CHANGED = "BUG_STATUS_CHANGED"
    BUG_COMMENT = "BUG_COMMENT"
    BUG_MENTION = "BUG_MENTION"
    
    # AI
    AI_ANALYSIS_COMPLETED = "AI_ANALYSIS_COMPLETED"
    AI_ANALYSIS_FAILED = "AI_ANALYSIS_FAILED"
    
    # Billing
    PAYMENT_SUCCESS = "PAYMENT_SUCCESS"
    PAYMENT_FAILED = "PAYMENT_FAILED"
    SUBSCRIPTION_RENEWED = "SUBSCRIPTION_RENEWED"
    SUBSCRIPTION_EXPIRING = "SUBSCRIPTION_EXPIRING"
    USAGE_LIMIT_REACHED = "USAGE_LIMIT_REACHED"
    
    # System
    SYSTEM_ALERT = "SYSTEM_ALERT"
    SECURITY_ALERT = "SECURITY_ALERT"
    ANNOUNCEMENT = "ANNOUNCEMENT"

class NotificationPriority(str, enum.Enum):
    CRITICAL = "CRITICAL"
    WARNING = "WARNING"
    INFO = "INFO"
    SUCCESS = "SUCCESS"

class Notification(AuditBase):
    __tablename__ = "notifications"

    recipient_user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    organization_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("organizations.id", ondelete="CASCADE"), nullable=True, index=True)
    
    type: Mapped[NotificationType] = mapped_column(SQLEnum(NotificationType), nullable=False)
    priority: Mapped[NotificationPriority] = mapped_column(SQLEnum(NotificationPriority), default=NotificationPriority.INFO, nullable=False)
    
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    message: Mapped[str] = mapped_column(String(1024), nullable=False)
    
    action_url: Mapped[str | None] = mapped_column(String(512), nullable=True)
    action_label: Mapped[str | None] = mapped_column(String(100), nullable=True)
    
    metadata_: Mapped[dict | None] = mapped_column("metadata", JSONB, nullable=True)
    
    is_read: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False, index=True)
    read_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
