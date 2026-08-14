import uuid
from datetime import datetime, timezone
from typing import List, Tuple, Any
from sqlalchemy import select, update, delete, desc, asc
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.notification import Notification, NotificationType, NotificationPriority

class NotificationService:
    @staticmethod
    async def create_notification(
        db: AsyncSession,
        recipient_user_id: uuid.UUID,
        type: NotificationType,
        title: str,
        message: str,
        priority: NotificationPriority = NotificationPriority.INFO,
        organization_id: uuid.UUID | None = None,
        action_url: str | None = None,
        action_label: str | None = None,
        metadata_: dict[str, Any] | None = None,
    ) -> Notification:
        notification = Notification(
            recipient_user_id=recipient_user_id,
            organization_id=organization_id,
            type=type,
            priority=priority,
            title=title,
            message=message,
            action_url=action_url,
            action_label=action_label,
            metadata_=metadata_
        )
        db.add(notification)
        await db.commit()
        await db.refresh(notification)
        return notification

    @staticmethod
    async def create_bulk_notifications(
        db: AsyncSession,
        recipient_user_ids: List[uuid.UUID],
        type: NotificationType,
        title: str,
        message: str,
        priority: NotificationPriority = NotificationPriority.INFO,
        organization_id: uuid.UUID | None = None,
        action_url: str | None = None,
        action_label: str | None = None,
        metadata_: dict[str, Any] | None = None,
    ) -> None:
        if not recipient_user_ids:
            return
            
        notifications = [
            Notification(
                recipient_user_id=uid,
                organization_id=organization_id,
                type=type,
                priority=priority,
                title=title,
                message=message,
                action_url=action_url,
                action_label=action_label,
                metadata_=metadata_
            ) for uid in recipient_user_ids
        ]
        db.add_all(notifications)
        await db.commit()

    @staticmethod
    async def get_notifications(
        db: AsyncSession,
        user_id: uuid.UUID,
        limit: int = 20,
        cursor: str | None = None,
        unread_only: bool = False
    ) -> Tuple[List[Notification], str | None, bool]:
        
        query = select(Notification).where(Notification.recipient_user_id == user_id)
        
        if unread_only:
            query = query.where(Notification.is_read == False)
            
        if cursor:
            try:
                # Assuming cursor is an ISO format datetime string
                cursor_dt = datetime.fromisoformat(cursor)
                query = query.where(Notification.created_at < cursor_dt)
            except ValueError:
                pass
                
        # Order by created_at descending
        query = query.order_by(desc(Notification.created_at)).limit(limit + 1)
        
        result = await db.execute(query)
        items = list(result.scalars().all())
        
        has_more = len(items) > limit
        if has_more:
            items.pop()
            next_cursor = items[-1].created_at.isoformat() if items else None
        else:
            next_cursor = None
            
        return items, next_cursor, has_more

    @staticmethod
    async def get_unread_count(db: AsyncSession, user_id: uuid.UUID) -> int:
        query = select(Notification).where(
            Notification.recipient_user_id == user_id,
            Notification.is_read == False
        )
        result = await db.execute(query)
        return len(result.scalars().all())

    @staticmethod
    async def mark_read(db: AsyncSession, notification_id: uuid.UUID, user_id: uuid.UUID) -> Notification | None:
        query = select(Notification).where(
            Notification.id == notification_id,
            Notification.recipient_user_id == user_id
        )
        result = await db.execute(query)
        notification = result.scalar_one_or_none()
        
        if notification and not notification.is_read:
            notification.is_read = True
            notification.read_at = datetime.now(timezone.utc)
            await db.commit()
            await db.refresh(notification)
            
        return notification

    @staticmethod
    async def mark_all_read(db: AsyncSession, user_id: uuid.UUID) -> None:
        stmt = update(Notification).where(
            Notification.recipient_user_id == user_id,
            Notification.is_read == False
        ).values(
            is_read=True,
            read_at=datetime.now(timezone.utc)
        )
        await db.execute(stmt)
        await db.commit()

    @staticmethod
    async def delete_notification(db: AsyncSession, notification_id: uuid.UUID, user_id: uuid.UUID) -> bool:
        stmt = delete(Notification).where(
            Notification.id == notification_id,
            Notification.recipient_user_id == user_id
        )
        result = await db.execute(stmt)
        await db.commit()
        return result.rowcount > 0

notification_service = NotificationService()
