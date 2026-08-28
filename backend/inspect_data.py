import asyncio
from sqlalchemy import select, text
from sqlalchemy.orm import selectinload

from app.core.database import AsyncSessionLocal
from app.models.workspace import Workspace
from app.models.project import Project, Repository
from app.models.bug import Bug
from app.models.identity import WorkspaceMember
from app.models.organization import OrganizationMember

async def inspect():
    async with AsyncSessionLocal() as db:
        print("--- EXISTING WORKSPACES ---")
        ws_res = await db.execute(select(Workspace))
        workspaces = ws_res.scalars().all()
        print(f"Total Workspaces: {len(workspaces)}")
        
        for w in workspaces:
            print(f"  Workspace: {w.name} (id: {w.id})")
            # Try to infer organization from members
            mem_res = await db.execute(select(WorkspaceMember).where(WorkspaceMember.workspace_id == w.id))
            members = mem_res.scalars().all()
            print(f"    Members: {len(members)}")
            
            for m in members:
                # find their org
                org_res = await db.execute(select(OrganizationMember).where(OrganizationMember.user_id == m.user_id))
                org_mems = org_res.scalars().all()
                for om in org_mems:
                    print(f"      User {m.user_id} belongs to Org {om.organization_id}")
        
        print("\n--- EXISTING PROJECTS ---")
        proj_res = await db.execute(select(Project))
        projects = proj_res.scalars().all()
        print(f"Total Projects: {len(projects)}")
        for p in projects:
            print(f"  Project: {p.name} (org: {p.organization_id})")
            
        print("\n--- EXISTING BUGS ---")
        bug_res = await db.execute(select(Bug))
        bugs = bug_res.scalars().all()
        print(f"Total Bugs: {len(bugs)}")
        for b in bugs:
            print(f"  Bug: {b.title} (project: {b.project_id})")

        print("\n--- EXISTING REPOSITORIES ---")
        repo_res = await db.execute(select(Repository))
        repos = repo_res.scalars().all()
        print(f"Total Repositories: {len(repos)}")
        for r in repos:
            print(f"  Repo: {r.full_name} (org: {r.organization_id}, ws: {r.workspace_id}, project: {r.project_id})")

asyncio.run(inspect())
