import uuid
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import UploadFile

from app.models.bug import BugAttachment, Bug
from app.services.storage import storage_service
from app.models.identity import User
from app.models.organization import Organization

class BugAttachmentService:
    async def upload_attachment(
        self, 
        db: AsyncSession, 
        *, 
        bug_id: uuid.UUID, 
        organization_id: uuid.UUID,
        workspace_id: uuid.UUID,
        file: UploadFile,
        user_id: Optional[uuid.UUID] = None
    ) -> BugAttachment:
        # First verify the bug exists and belongs to the workspace
        bug = await db.scalar(
            select(Bug).where(
                Bug.id == bug_id,
                Bug.organization_id == organization_id,
                Bug.workspace_id == workspace_id
            )
        )
        if not bug:
            raise ValueError("Bug not found or access denied")

        # Read content
        content = await file.read()
        
        # Upload via storage service
        prefix = f"org_{organization_id}/ws_{workspace_id}/bug_{bug_id}"
        storage_key = await storage_service.upload_file(
            file_content=content,
            filename=file.filename or "unnamed_file",
            content_type=file.content_type or "application/octet-stream",
            prefix=prefix
        )

        # Create DB record
        attachment = BugAttachment(
            bug_id=bug_id,
            s3_key=storage_key,
            mime_type=file.content_type or "application/octet-stream",
            size_bytes=len(content)
        )
        db.add(attachment)
        await db.commit()
        await db.refresh(attachment)
        
        return attachment

    async def list_attachments(
        self, 
        db: AsyncSession, 
        *, 
        bug_id: uuid.UUID,
        organization_id: uuid.UUID,
        workspace_id: uuid.UUID
    ) -> List[BugAttachment]:
        # Verify access
        bug = await db.scalar(
            select(Bug).where(
                Bug.id == bug_id,
                Bug.organization_id == organization_id,
                Bug.workspace_id == workspace_id
            )
        )
        if not bug:
            raise ValueError("Bug not found or access denied")
            
        result = await db.execute(
            select(BugAttachment).where(BugAttachment.bug_id == bug_id)
        )
        return list(result.scalars().all())

    async def get_attachment(
        self, 
        db: AsyncSession, 
        *, 
        attachment_id: uuid.UUID,
        bug_id: uuid.UUID,
        organization_id: uuid.UUID,
        workspace_id: uuid.UUID
    ) -> Optional[BugAttachment]:
        # Verify bug access
        bug = await db.scalar(
            select(Bug).where(
                Bug.id == bug_id,
                Bug.organization_id == organization_id,
                Bug.workspace_id == workspace_id
            )
        )
        if not bug:
            raise ValueError("Bug not found or access denied")
            
        return await db.scalar(
            select(BugAttachment).where(
                BugAttachment.id == attachment_id,
                BugAttachment.bug_id == bug_id
            )
        )

    async def delete_attachment(
        self, 
        db: AsyncSession, 
        *, 
        attachment_id: uuid.UUID,
        bug_id: uuid.UUID,
        organization_id: uuid.UUID,
        workspace_id: uuid.UUID
    ) -> bool:
        attachment = await self.get_attachment(
            db, 
            attachment_id=attachment_id, 
            bug_id=bug_id, 
            organization_id=organization_id, 
            workspace_id=workspace_id
        )
        if not attachment:
            raise ValueError("Attachment not found")

        # Delete from storage first
        deleted = await storage_service.delete_file(attachment.s3_key)
        
        # We can still delete from DB even if storage delete fails, but log it in prod
        await db.delete(attachment)
        await db.commit()
        
        return True

attachment_service = BugAttachmentService()
