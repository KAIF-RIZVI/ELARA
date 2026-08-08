from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

from app.api.deps import SessionDep, CurrentUser, RequireRole
from app.schemas.team import TeamCreate, TeamResponse, TeamUpdate
from app.models.identity import WorkspaceMember, MemberRole, User
from app.models.team import Team, TeamMember

router = APIRouter()

@router.post("/", response_model=TeamResponse)
async def create_team(
    workspace_id: uuid.UUID,
    team_in: TeamCreate,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    team = Team(
        workspace_id=workspace_id,
        name=team_in.name,
        description=team_in.description,
        created_by=member.user_id
    )
    db.add(team)
    await db.commit()
    await db.refresh(team)
    return TeamResponse(**team.__dict__)

@router.get("/", response_model=list[TeamResponse])
async def list_teams(
    workspace_id: uuid.UUID,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    stmt = select(Team).where(Team.workspace_id == workspace_id)
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

@router.delete("/{team_id}")
async def delete_team(
    workspace_id: uuid.UUID,
    team_id: uuid.UUID,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    stmt = select(Team).where(Team.workspace_id == workspace_id, Team.id == team_id)
    team = (await db.execute(stmt)).scalar_one_or_none()
    
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
        
    await db.delete(team)
    await db.commit()
    return {"message": "Team deleted"}
