from pydantic import BaseModel, ConfigDict
from typing import List, Optional, Any, Dict
import uuid
from datetime import datetime

class SearchResultItem(BaseModel):
    id: str
    title: str
    subtitle: Optional[str] = None
    category: str
    icon: Optional[str] = None
    badge: Optional[str] = None
    url: str
    organization_id: Optional[uuid.UUID] = None
    metadata: Optional[Dict[str, Any]] = None

    model_config = ConfigDict(from_attributes=True)

class SearchCategory(BaseModel):
    quick_actions: List[SearchResultItem] = []
    recent: List[SearchResultItem] = []
    organizations: List[SearchResultItem] = []
    projects: List[SearchResultItem] = []
    repositories: List[SearchResultItem] = []
    bugs: List[SearchResultItem] = []
    members: List[SearchResultItem] = []
    teams: List[SearchResultItem] = []
    settings: List[SearchResultItem] = []

    model_config = ConfigDict(from_attributes=True)

class GlobalSearchResponse(BaseModel):
    results: SearchCategory
    query: str
    took_ms: int
