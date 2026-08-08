from app.core.base_repository import BaseRepository
from app.models.project import Repository

class RepositoryRepo(BaseRepository[Repository]):
    pass

repository_repo = RepositoryRepo(Repository)