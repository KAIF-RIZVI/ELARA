from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

from app.api.deps import SessionDep, CurrentUser, RequireRole
from app.schemas.project import ProjectCreate, ProjectResponse, ProjectUpdate
from app.models.identity import WorkspaceMember, MemberRole, User
from app.models.project import Project, Repository

router = APIRouter()

@router.post("", response_model=ProjectResponse)
async def create_project(
    workspace_id: uuid.UUID,
    project_in: ProjectCreate,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    project = Project(
        workspace_id=workspace_id,
        name=project_in.name,
        description=project_in.description,
        status=project_in.status,
        created_by=member.user_id
    )
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return ProjectResponse(**project.__dict__)

@router.get("", response_model=list[ProjectResponse])
async def list_projects(
    workspace_id: uuid.UUID,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.VIEWER))
):
    stmt = select(Project).where(Project.workspace_id == workspace_id)
    projects = (await db.execute(stmt)).scalars().all()
    
    response = []
    for project in projects:
        repos_count = await db.scalar(
            select(func.count(Repository.id)).where(Repository.project_id == project.id)
        )
        owner_name = None
        if project.created_by:
            owner = await db.scalar(select(User).where(User.id == project.created_by))
            if owner:
                owner_name = owner.full_name
                
        data = project.__dict__.copy()
        data["repositories_count"] = repos_count or 0
        data["owner_name"] = owner_name
        response.append(ProjectResponse(**data))
        
    return response

@router.put("/{project_id}", response_model=ProjectResponse)
async def update_project(
    workspace_id: uuid.UUID,
    project_id: uuid.UUID,
    update_in: ProjectUpdate,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    stmt = select(Project).where(Project.workspace_id == workspace_id, Project.id == project_id)
    project = (await db.execute(stmt)).scalar_one_or_none()
    
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    if update_in.name is not None:
        project.name = update_in.name
    if update_in.description is not None:
        project.description = update_in.description
    if update_in.status is not None:
        project.status = update_in.status
        
    await db.commit()
    await db.refresh(project)
    return ProjectResponse(**project.__dict__)

@router.delete("/{project_id}")
async def delete_project(
    workspace_id: uuid.UUID,
    project_id: uuid.UUID,
    db: SessionDep,
    member: WorkspaceMember = Depends(RequireRole(MemberRole.ADMIN))
):
    stmt = select(Project).where(Project.workspace_id == workspace_id, Project.id == project_id)
    project = (await db.execute(stmt)).scalar_one_or_none()
    
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
        
    await db.delete(project)
    await db.commit()
    return {"message": "Project deleted"}
