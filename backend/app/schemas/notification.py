from pydantic import BaseModel, ConfigDict
import uuid
from datetime import datetime
from typing import Any
from app.models.notification import NotificationType, NotificationPriority

class NotificationBase(BaseModel):
    type: NotificationType
    priority: NotificationPriority
    title: str
    message: str
    action_url: str | None = None
    action_label: str | None = None
    metadata_: dict[str, Any] | None = None

class NotificationResponse(NotificationBase):
    id: uuid.UUID
    recipient_user_id: uuid.UUID
    organization_id: uuid.UUID | None
    is_read: bool
    created_at: datetime
    read_at: datetime | None

    model_config = ConfigDict(from_attributes=True)

class NotificationListResponse(BaseModel):
    items: list[NotificationResponse]
    next_cursor: str | None
    has_more: bool

class UnreadCountResponse(BaseModel):
    unread_count: int
