import uuid
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from app.api.deps import SessionDep, CurrentUser, RequireRole
from app.schemas.bug import (
    BugCreate, BugResponse, BugUpdate, BugStatusUpdate, 
    BugPriorityUpdate, BugAssignUpdate, BugCommentCreate, 
    BugCommentResponse
)
from app.schemas.workspace import ActivityLogResponse
from app.services.bug import bug_service
from app.services.workspace import workspace_service
from app.models.identity import WorkspaceMember, MemberRole

router = APIRouter()

async def get_org_id_for_workspace(db: SessionDep, workspace_id: uuid.UUID) -> uuid.UUID:
    workspace = await workspace_service.get(db, id=workspace_id)
    if not workspace or not workspace.organization_id:
        raise HTTPException(status_code=400, detail="Invalid workspace context. Legacy workspaces must be migrated to an organization.")
    return workspace.organization_id

@router.post("", response_model=BugResponse)
async def create_workspace_bug(
    workspace_id: uuid.UUID,
    bug_in: BugCreate,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        bug = await bug_service.create_bug(
            db, 
            obj_in=bug_in,
            organization_id=organization_id,
            workspace_id=workspace_id,
            user_id=current_user.id
        )
        return bug
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=List[BugResponse])
async def list_workspace_bugs(
    workspace_id: uuid.UUID,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    bugs = await bug_service.list_bugs(db, organization_id=organization_id, workspace_id=workspace_id)
    return bugs

@router.get("/{bug_id}", response_model=BugResponse)
async def get_workspace_bug(
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    bug = await bug_service.get_bug(db, bug_id=bug_id, organization_id=organization_id, workspace_id=workspace_id)
    if not bug:
        raise HTTPException(status_code=404, detail="Bug not found")
    return bug

@router.patch("/{bug_id}", response_model=BugResponse)
async def update_workspace_bug(
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    bug_in: BugUpdate,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        bug = await bug_service.update_bug(
            db, 
            bug_id=bug_id,
            obj_in=bug_in,
            organization_id=organization_id,
            workspace_id=workspace_id,
            user_id=current_user.id
        )
        return bug
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{bug_id}/status", response_model=BugResponse)
async def update_bug_status(
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    status_in: BugStatusUpdate,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        bug = await bug_service.change_status(
            db, 
            bug_id=bug_id,
            obj_in=status_in,
            organization_id=organization_id,
            workspace_id=workspace_id,
            user_id=current_user.id
        )
        return bug
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{bug_id}/priority", response_model=BugResponse)
async def update_bug_priority(
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    priority_in: BugPriorityUpdate,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        bug = await bug_service.change_priority(
            db, 
            bug_id=bug_id,
            obj_in=priority_in,
            organization_id=organization_id,
            workspace_id=workspace_id,
            user_id=current_user.id
        )
        return bug
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{bug_id}/assign", response_model=BugResponse)
async def assign_bug_developer(
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    assign_in: BugAssignUpdate,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        bug = await bug_service.assign_developer(
            db, 
            bug_id=bug_id,
            obj_in=assign_in,
            organization_id=organization_id,
            workspace_id=workspace_id,
            user_id=current_user.id
        )
        return bug
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{bug_id}/comments", response_model=BugCommentResponse)
async def add_bug_comment(
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    comment_in: BugCommentCreate,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        comment = await bug_service.add_comment(
            db, 
            bug_id=bug_id,
            obj_in=comment_in,
            organization_id=organization_id,
            workspace_id=workspace_id,
            user_id=current_user.id
        )
        return comment
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{bug_id}/comments", response_model=List[BugCommentResponse])
async def list_bug_comments(
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        comments = await bug_service.list_comments(
            db, 
            bug_id=bug_id,
            organization_id=organization_id,
            workspace_id=workspace_id
        )
        return comments
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{bug_id}/history", response_model=List[ActivityLogResponse])
async def get_bug_history(
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        history = await bug_service.get_bug_history(
            db, 
            bug_id=bug_id,
            organization_id=organization_id,
            workspace_id=workspace_id
        )
        return history
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

from app.schemas.bug import BugCommentCreate, BugCommentResponse, ActivityLogResponse

@router.post("/{bug_id}/comments", response_model=BugCommentResponse)
async def add_bug_comment(
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    comment_in: BugCommentCreate,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.DEVELOPER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        return await bug_service.add_comment(
            db, 
            bug_id=bug_id,
            obj_in=comment_in,
            organization_id=organization_id,
            workspace_id=workspace_id,
            user_id=current_user.id
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{bug_id}/comments", response_model=list[BugCommentResponse])
async def list_bug_comments(
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        return await bug_service.list_comments(
            db, 
            bug_id=bug_id,
            organization_id=organization_id,
            workspace_id=workspace_id
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{bug_id}/history", response_model=list[ActivityLogResponse])
async def get_bug_history(
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        return await bug_service.get_bug_history(
            db, 
            bug_id=bug_id,
            organization_id=organization_id,
            workspace_id=workspace_id
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{bug_id}")
async def soft_delete_bug(
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep, 
    current_user: CurrentUser, 
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        await bug_service.delete_bug(
            db, 
            bug_id=bug_id,
            organization_id=organization_id,
            workspace_id=workspace_id,
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
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    file: UploadFile = File(...),
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        attachment = await attachment_service.upload_attachment(
            db,
            bug_id=bug_id,
            organization_id=organization_id,
            workspace_id=workspace_id,
            file=file,
            user_id=current_user.id
        )
        return attachment
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
        
@router.get("/{bug_id}/attachments", response_model=List[BugAttachmentResponse])
async def list_bug_attachments(
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        attachments = await attachment_service.list_attachments(
            db,
            bug_id=bug_id,
            organization_id=organization_id,
            workspace_id=workspace_id
        )
        return attachments
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{bug_id}/attachments/{attachment_id}/download")
async def download_bug_attachment(
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    attachment_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        attachment = await attachment_service.get_attachment(
            db,
            attachment_id=attachment_id,
            bug_id=bug_id,
            organization_id=organization_id,
            workspace_id=workspace_id
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
    workspace_id: uuid.UUID,
    bug_id: uuid.UUID,
    attachment_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    organization_id = await get_org_id_for_workspace(db, workspace_id)
    try:
        await attachment_service.delete_attachment(
            db,
            attachment_id=attachment_id,
            bug_id=bug_id,
            organization_id=organization_id,
            workspace_id=workspace_id
        )
        return {"status": "deleted"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
