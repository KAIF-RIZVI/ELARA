import uuid
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from app.api.deps import SessionDep, CurrentUser, RequireOrganizationRole
from app.schemas.bug import (
    BugCreate, BugResponse, BugUpdate, BugStatusUpdate, 
    BugPriorityUpdate, BugAssignUpdate, BugCommentCreate, 
    BugCommentResponse
)
from app.schemas.workspace import ActivityLogResponse
from app.services.bug import bug_service
from app.services.organization import organization_service
from app.models.organization import OrganizationMember, OrganizationRole as MemberRole

router = APIRouter()


@router.post("", response_model=BugResponse)
async def create_organization_bug(
    organization_id: uuid.UUID,
    bug_in: BugCreate,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    try:
        bug = await bug_service.create_bug(
            db, 
            obj_in=bug_in,
            organization_id=organization_id,
            user_id=current_user.id
        )
        return bug
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=List[BugResponse])
async def list_organization_bugs(
    organization_id: uuid.UUID,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    bugs = await bug_service.list_bugs(db, organization_id=organization_id)
    return bugs

@router.get("/{bug_id}", response_model=BugResponse)
async def get_organization_bug(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    bug = await bug_service.get_bug(db, bug_id=bug_id, organization_id=organization_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
    return bug

@router.patch("/{bug_id}", response_model=BugResponse)
async def update_organization_bug(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    bug_in: BugUpdate,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    try:
        bug = await bug_service.update_bug(
            db, 
            bug_id=bug_id,
            obj_in=bug_in,
            organization_id=organization_id,
            user_id=current_user.id
        )
        return bug
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{bug_id}/status", response_model=BugResponse)
async def update_bug_status(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    status_in: BugStatusUpdate,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    try:
        bug = await bug_service.change_status(
            db, 
            bug_id=bug_id,
            obj_in=status_in,
            organization_id=organization_id,
            user_id=current_user.id
        )
        return bug
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{bug_id}/priority", response_model=BugResponse)
async def update_bug_priority(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    priority_in: BugPriorityUpdate,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    try:
        bug = await bug_service.change_priority(
            db, 
            bug_id=bug_id,
            obj_in=priority_in,
            organization_id=organization_id,
            user_id=current_user.id
        )
        return bug
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{bug_id}/assign", response_model=BugResponse)
async def assign_bug_developer(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    assign_in: BugAssignUpdate,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    try:
        bug = await bug_service.assign_developer(
            db, 
            bug_id=bug_id,
            obj_in=assign_in,
            organization_id=organization_id,
            user_id=current_user.id
        )
        return bug
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{bug_id}/comments", response_model=BugCommentResponse)
async def add_bug_comment(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    comment_in: BugCommentCreate,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    try:
        comment = await bug_service.add_comment(
            db, 
            bug_id=bug_id,
            obj_in=comment_in,
            organization_id=organization_id,
            user_id=current_user.id
        )
        return comment
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{bug_id}/comments", response_model=List[BugCommentResponse])
async def list_bug_comments(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    try:
        comments = await bug_service.list_comments(
            db, 
            bug_id=bug_id,
            organization_id=organization_id
        )
        return comments
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{bug_id}/history", response_model=List[ActivityLogResponse])
async def get_bug_history(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    try:
        history = await bug_service.get_bug_history(
            db, 
            bug_id=bug_id,
            organization_id=organization_id
        )
        return history
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

from app.schemas.bug import BugCommentCreate, BugCommentResponse, ActivityLogResponse

@router.post("/{bug_id}/comments", response_model=BugCommentResponse)
async def add_bug_comment(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    comment_in: BugCommentCreate,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.DEVELOPER))
):
    try:
        return await bug_service.add_comment(
            db, 
            bug_id=bug_id,
            obj_in=comment_in,
            organization_id=organization_id,
            user_id=current_user.id
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{bug_id}/comments", response_model=list[BugCommentResponse])
async def list_bug_comments(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    try:
        return await bug_service.list_comments(
            db, 
            bug_id=bug_id,
            organization_id=organization_id
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{bug_id}/history", response_model=list[ActivityLogResponse])
async def get_bug_history(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    try:
        return await bug_service.get_bug_history(
            db, 
            bug_id=bug_id,
            organization_id=organization_id
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{bug_id}")
async def soft_delete_bug(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.ADMIN))
):
    try:
        await bug_service.delete_bug(
            db, 
            bug_id=bug_id,
            organization_id=organization_id,
            user_id=current_user.id
        )
        return {"status": "deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

from fastapi import UploadFile, File, Response
from app.services.attachment import attachment_service
from app.services.storage import storage_service
from app.schemas.bug import BugAttachmentResponse

@router.post("/{bug_id}/attachments", response_model=BugAttachmentResponse)
async def upload_bug_attachment(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    file: UploadFile = File(...),
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    try:
        attachment = await attachment_service.upload_attachment(
            db,
            bug_id=bug_id,
            organization_id=organization_id,
            file=file,
            user_id=current_user.id
        )
        return attachment
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
        
@router.get("/{bug_id}/attachments", response_model=List[BugAttachmentResponse])
async def list_bug_attachments(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    try:
        attachments = await attachment_service.list_attachments(
            db,
            bug_id=bug_id,
            organization_id=organization_id
        )
        return attachments
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{bug_id}/attachments/{attachment_id}/download")
async def download_bug_attachment(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    attachment_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.VIEWER))
):
    try:
        attachment = await attachment_service.get_attachment(
            db,
            attachment_id=attachment_id,
            bug_id=bug_id,
            organization_id=organization_id
        )
        if not attachment:
            raise HTTPException(status_code=404, detail="Attachment not found")
            
        file_bytes = await storage_service.get_file(attachment.s3_key)
        if not file_bytes:
            raise HTTPException(status_code=404, detail="File not found in storage")
            
        return Response(content=file_bytes, media_type=attachment.mime_type)
        
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{bug_id}/attachments/{attachment_id}")
async def delete_bug_attachment(
    organization_id: uuid.UUID,
    bug_id: uuid.UUID,
    attachment_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member: OrganizationMember = Depends(RequireOrganizationRole(MemberRole.ADMIN))
):
    try:
        await attachment_service.delete_attachment(
            db,
            attachment_id=attachment_id,
            bug_id=bug_id,
            organization_id=organization_id
        )
        return {"status": "deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


