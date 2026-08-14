import uuid
from typing import Optional
from fastapi import APIRouter, Depends, Query

from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db, get_current_user
from app.models.identity import User
from app.services.search import GlobalSearchService
from app.schemas.search import GlobalSearchResponse

router = APIRouter()

@router.get("", response_model=GlobalSearchResponse)
async def search_global(
    q: str = Query("", description="Search query"),
    organization_id: Optional[uuid.UUID] = Query(None, description="Optional organization ID to restrict search"),
    category: Optional[str] = Query(None, description="Category filter (e.g., repo, project)"),
    limit: int = Query(10, description="Limit per category", le=50),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Search globally across Organizations, Projects, Repositories, Bugs, and Members.
    Respects RBAC: only returns items in organizations the current user belongs to.
    """
    return await GlobalSearchService.search(
        db=db,
        current_user=current_user,
        query=q,
        organization_id=organization_id,
        category_filter=category,
        limit=limit
    )
