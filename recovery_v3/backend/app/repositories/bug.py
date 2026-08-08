from app.core.base_repository import BaseRepository
from app.models.bug import Bug

class RepositoryBug(BaseRepository[Bug]):
    pass

bug = RepositoryBug(Bug)
