from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

from app.api.deps import SessionDep, CurrentUser, RequireOrganizationRole
from app.schemas.team import TeamCreate, TeamResponse, TeamUpdate
from app.models.organization import OrganizationMember, OrganizationRole
from app.models.identity import User
from app.models.team import Team, TeamMember

router = APIRouter()

@router.post("", response_model=TeamResponse)
async def create_team(
    organization_id: uuid.UUID,
    team_in: TeamCreate,
    db: SessionDep,
    member: OrganizationMember = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    team = Team(
        organization_id=organization_id,
        name=team_in.name,
        description=team_in.description,
        created_by=member.user_id
    )
    db.add(team)
    await db.commit()
    await db.refresh(team)
    return TeamResponse(**team.__dict__)

@router.get("", response_model=list[TeamResponse])
async def list_teams(
    organization_id: uuid.UUID,
    db: SessionDep,
    member: OrganizationMember = Depends(RequireOrganizationRole(OrganizationRole.VIEWER))
):
    stmt = select(Team).where(Team.organization_id == organization_id)
    teams = (await db.execute(stmt)).scalars().all()
    
    response = []
    for team in teams:
        members_count = await db.scalar(
            select(func.count(TeamMember.id)).where(TeamMember.team_id == team.id)
        )
        lead_name = None
        if team.lead_id:
            lead = await db.scalar(select(User).where(User.id == team.lead_id))
            if lead:
                lead_name = lead.full_name
                
        data = team.__dict__.copy()
        data["members_count"] = members_count or 0
        data["lead_name"] = lead_name
        response.append(TeamResponse(**data))
        
    return response

@router.patch("/{team_id}", response_model=TeamResponse)
async def update_team(
    organization_id: uuid.UUID,
    team_id: uuid.UUID,
    team_in: TeamUpdate,
    db: SessionDep,
    member: OrganizationMember = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    stmt = select(Team).where(Team.organization_id == organization_id, Team.id == team_id)
    team = (await db.execute(stmt)).scalar_one_or_none()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
        
    if team_in.name is not None:
        team.name = team_in.name
    if team_in.description is not None:
        team.description = team_in.description
    if hasattr(team_in, "lead_id") and team_in.lead_id is not None:
        team.lead_id = team_in.lead_id

    await db.commit()
    await db.refresh(team)
    
    # Calculate extra fields for response
    members_count = await db.scalar(
        select(func.count(TeamMember.id)).where(TeamMember.team_id == team.id)
    )
    lead_name = None
    if team.lead_id:
        lead = await db.scalar(select(User).where(User.id == team.lead_id))
        if lead:
            lead_name = lead.full_name
            
    data = team.__dict__.copy()
    data["members_count"] = members_count or 0
    data["lead_name"] = lead_name
    return TeamResponse(**data)

@router.delete("/{team_id}")
async def delete_team(
    organization_id: uuid.UUID,
    team_id: uuid.UUID,
    db: SessionDep,
    member: OrganizationMember = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    stmt = select(Team).where(Team.organization_id == organization_id, Team.id == team_id)
    team = (await db.execute(stmt)).scalar_one_or_none()
    
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
        
    await db.delete(team)
    await db.commit()
    return {"message": "Team deleted"}

@router.get("/{team_id}/members")
async def list_team_members(
    organization_id: uuid.UUID,
    team_id: uuid.UUID,
    db: SessionDep,
    member: OrganizationMember = Depends(RequireOrganizationRole(OrganizationRole.VIEWER))
):
    stmt = select(User, TeamMember).join(
        TeamMember, User.id == TeamMember.user_id
    ).where(
        TeamMember.team_id == team_id
    )
    results = (await db.execute(stmt)).all()
    
    response = []
    for user, team_member in results:
        response.append({
            "id": user.id,
            "team_id": team_member.team_id,
            "user_id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "avatar_url": user.avatar_url,
            "created_at": team_member.created_at
        })
    return response

from pydantic import BaseModel
class AddTeamMemberRequest(BaseModel):
    user_id: uuid.UUID

@router.post("/{team_id}/members")
async def add_team_member(
    organization_id: uuid.UUID,
    team_id: uuid.UUID,
    req: AddTeamMemberRequest,
    db: SessionDep,
    member: OrganizationMember = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    # Verify team exists
    stmt = select(Team).where(Team.organization_id == organization_id, Team.id == team_id)
    team = (await db.execute(stmt)).scalar_one_or_none()
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
        
    # Verify user is part of the organization
    org_member_stmt = select(OrganizationMember).where(
        OrganizationMember.organization_id == organization_id,
        OrganizationMember.user_id == req.user_id
    )
    org_member = (await db.execute(org_member_stmt)).scalar_one_or_none()
    if not org_member:
        raise HTTPException(status_code=400, detail="User is not a member of this organization")
        
    # Check if already in team
    existing_stmt = select(TeamMember).where(
        TeamMember.team_id == team_id,
        TeamMember.user_id == req.user_id
    )
    existing = (await db.execute(existing_stmt)).scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="User is already in this team")
        
    new_member = TeamMember(team_id=team_id, user_id=req.user_id)
    db.add(new_member)
    await db.commit()
    return {"message": "Member added successfully"}

@router.delete("/{team_id}/members/{user_id}")
async def remove_team_member(
    organization_id: uuid.UUID,
    team_id: uuid.UUID,
    user_id: uuid.UUID,
    db: SessionDep,
    member: OrganizationMember = Depends(RequireOrganizationRole(OrganizationRole.ADMIN))
):
    stmt = select(TeamMember).where(
        TeamMember.team_id == team_id,
        TeamMember.user_id == user_id
    )
    team_member = (await db.execute(stmt)).scalar_one_or_none()
    if not team_member:
        raise HTTPException(status_code=404, detail="Member not found in team")
        
    await db.delete(team_member)
    await db.commit()
    return {"message": "Member removed successfully"}
