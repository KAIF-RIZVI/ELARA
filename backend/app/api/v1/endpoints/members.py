from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import uuid
import secrets
from datetime import datetime, timezone, timedelta

from app.api.deps import SessionDep, CurrentUser, RequireRole
from app.schemas.member import MemberResponse, MemberUpdate, InviteCreate, InviteResponse
from app.models.identity import WorkspaceMember, User, MemberRole, WorkspaceInvitation, InvitationStatus

router = APIRouter()

@router.get("", response_model=list[MemberResponse])
async def list_workspace_members(
    workspace_id: uuid.UUID,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    stmt = select(WorkspaceMember, User).join(User, WorkspaceMember.user_id == User.id).where(
        WorkspaceMember.workspace_id == workspace_id
    )
    result = await db.execute(stmt)
    
    response = []
    for ws_member, user in result.all():
        data = ws_member.__dict__.copy()
        data["full_name"] = user.full_name
        data["email"] = user.email
        data["avatar_url"] = user.avatar_url
        response.append(MemberResponse(**data))
        
    return response

@router.post("/invites", response_model=InviteResponse)
async def invite_member(
    workspace_id: uuid.UUID,
    invite_in: InviteCreate,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    # Check if already a member
    stmt = select(WorkspaceMember).join(User, WorkspaceMember.user_id == User.id).where(
        WorkspaceMember.workspace_id == workspace_id,
        User.email == invite_in.email
    )
    if (await db.execute(stmt)).scalar_one_or_none():
        raise HTTPException(status_code=400, detail="User is already a member")

    # Generate token
    token = secrets.token_urlsafe(32)
    expires_at = datetime.now(timezone.utc) + timedelta(days=7)

    invite = WorkspaceInvitation(
        workspace_id=workspace_id,
        email=invite_in.email,
        role=invite_in.role,
        token=token,
        expires_at=expires_at,
        created_by=member.user_id # Using created_by for invited_by
    )
    db.add(invite)
    await db.commit()
    await db.refresh(invite)
    
    print(f"DEBUG: Email sent to {invite.email} with token {invite.token}")
    return invite

@router.put("/{user_id}", response_model=MemberResponse)
async def update_member_role(
    workspace_id: uuid.UUID,
    user_id: uuid.UUID,
    update_in: MemberUpdate,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    stmt = select(WorkspaceMember).where(
        WorkspaceMember.workspace_id == workspace_id,
        WorkspaceMember.user_id == user_id
    )
    target_member = (await db.execute(stmt)).scalar_one_or_none()
    
    if not target_member:
        raise HTTPException(status_code=404, detail="Member not found")
        
    if target_member.role == MemberRole.OWNER and update_in.role and update_in.role != MemberRole.OWNER:
        if member.role != MemberRole.OWNER:
            raise HTTPException(status_code=403, detail="Only owners can demote owners")

    if update_in.role:
        target_member.role = update_in.role
    if update_in.status:
        target_member.status = update_in.status
        
    await db.commit()
    await db.refresh(target_member)
    
    user = (await db.execute(select(User).where(User.id == user_id))).scalar_one()
    data = target_member.__dict__.copy()
    data["full_name"] = user.full_name
    data["email"] = user.email
    data["avatar_url"] = user.avatar_url
    
    return MemberResponse(**data)

@router.delete("/{user_id}")
async def remove_member(
    workspace_id: uuid.UUID,
    user_id: uuid.UUID,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    stmt = select(WorkspaceMember).where(
        WorkspaceMember.workspace_id == workspace_id,
        WorkspaceMember.user_id == user_id
    )
    target_member = (await db.execute(stmt)).scalar_one_or_none()
    
    if not target_member:
        raise HTTPException(status_code=404, detail="Member not found")
        
    if target_member.role == MemberRole.OWNER and member.role != MemberRole.OWNER:
        raise HTTPException(status_code=403, detail="Only owners can remove owners")
        
    await db.delete(target_member)
    await db.commit()
    return {"message": "Member removed successfully"}