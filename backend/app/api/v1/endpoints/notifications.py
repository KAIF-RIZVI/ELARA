import uuid
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_current_user, get_db
from app.models.identity import User
from app.schemas.notification import NotificationListResponse, UnreadCountResponse, NotificationResponse
from app.services.notification_service import notification_service

router = APIRouter()

@router.get("", response_model=NotificationListResponse)
async def get_notifications(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
    limit: int = Query(20, ge=1, le=100),
    cursor: str | None = None,
    unread_only: bool = False
) -> Any:
    """Get user notifications."""
    items, next_cursor, has_more = await notification_service.get_notifications(
        db=db,
        user_id=current_user.id,
        limit=limit,
        cursor=cursor,
        unread_only=unread_only
    )
    return {
        "items": items,
        "next_cursor": next_cursor,
        "has_more": has_more
    }

@router.get("/unread-count", response_model=UnreadCountResponse)
async def get_unread_count(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """Get user unread notification count."""
    count = await notification_service.get_unread_count(db=db, user_id=current_user.id)
    return {"unread_count": count}

@router.patch("/{notification_id}/read", response_model=NotificationResponse)
async def mark_read(
    notification_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """Mark a notification as read."""
    notification = await notification_service.mark_read(
        db=db, 
        notification_id=notification_id, 
        user_id=current_user.id
    )
    if not notification:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Notification not found"
        )
    return notification

@router.post("/mark-all-read")
async def mark_all_read(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """Mark all notifications as read."""
    await notification_service.mark_all_read(db=db, user_id=current_user.id)
    return {"status": "success"}

@router.delete("/{notification_id}")
async def delete_notification(
    notification_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> Any:
    """Delete a notification."""
    success = await notification_service.delete_notification(
        db=db, 
        notification_id=notification_id, 
        user_id=current_user.id
    )
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Notification not found"
        )
    return {"status": "success"}
