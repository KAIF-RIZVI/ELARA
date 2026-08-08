from fastapi import APIRouter
from app.api.v1.endpoints import auth, workspaces, bugs, repositories, users, dashboard, profiles, members, teams, projects

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(workspaces.router, prefix="/workspaces", tags=["workspaces"])
api_router.include_router(bugs.router, prefix="/bugs", tags=["bugs"])
api_router.include_router(repositories.router, prefix="/repositories", tags=["repositories"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(profiles.router, prefix="/profiles", tags=["profiles"])
api_router.include_router(members.router, prefix="/workspaces/{workspace_id}/members", tags=["members"])
api_router.include_router(teams.router, prefix="/workspaces/{workspace_id}/teams", tags=["teams"])
api_router.include_router(projects.router, prefix="/workspaces/{workspace_id}/projects", tags=["projects"])
