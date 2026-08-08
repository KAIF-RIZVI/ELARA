import uuid
import enum
from sqlalchemy import String, Enum as SQLEnum, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from app.core.base_model import WorkspaceEntityBase

class NotifChannel(str, enum.Enum):
    EMAIL = "EMAIL"
    IN_APP = "IN_APP"
    SLACK = "SLACK"

class NotifStatus(str, enum.Enum):
    PENDING = "PENDING"
    SENT = "SENT"
    FAILED = "FAILED"
    READ = "READ"

class Notification(WorkspaceEntityBase):
    __tablename__ = "notifications"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    channel: Mapped[NotifChannel] = mapped_column(SQLEnum(NotifChannel), default=NotifChannel.IN_APP, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    payload: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
    status: Mapped[NotifStatus] = mapped_column(SQLEnum(NotifStatus), default=NotifStatus.PENDING, nullable=False)

class ActivityLog(WorkspaceEntityBase):
    __tablename__ = "activity_log"

    entity_type: Mapped[str] = mapped_column(String, nullable=False)
    entity_id: Mapped[uuid.UUID] = mapped_column(nullable=False, index=True)
    action: Mapped[str] = mapped_column(String, nullable=False)
    actor_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    detail: Mapped[dict | None] = mapped_column(JSONB, nullable=True)
