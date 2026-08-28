import os
import aiofiles
import uuid
from abc import ABC, abstractmethod
from typing import Optional
from app.core.config import get_settings

settings = get_settings()

class StorageService(ABC):
    @abstractmethod
    async def upload_file(self, file_content: bytes, filename: str, content_type: str, prefix: str = "") -> str:
        """Upload a file and return its storage key/path."""
        pass

    @abstractmethod
    async def get_file(self, storage_key: str) -> Optional[bytes]:
        """Retrieve a file by its storage key/path."""
        pass

    @abstractmethod
    async def delete_file(self, storage_key: str) -> bool:
        """Delete a file by its storage key/path."""
        pass


class LocalStorageService(StorageService):
    def __init__(self):
        self.base_dir = settings.LOCAL_STORAGE_DIR
        os.makedirs(self.base_dir, exist_ok=True)

    async def upload_file(self, file_content: bytes, filename: str, content_type: str, prefix: str = "") -> str:
        # Generate a unique path to avoid collisions
        unique_filename = f"{uuid.uuid4()}_{filename}"
        if prefix:
            storage_key = os.path.join(prefix, unique_filename).replace("\\", "/")
        else:
            storage_key = unique_filename
            
        full_path = os.path.join(self.base_dir, storage_key)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        async with aiofiles.open(full_path, 'wb') as f:
            await f.write(file_content)
            
        return storage_key

    async def get_file(self, storage_key: str) -> Optional[bytes]:
        # Basic path traversal protection
        if ".." in storage_key:
            return None
            
        full_path = os.path.join(self.base_dir, storage_key)
        if not os.path.exists(full_path):
            return None
            
        async with aiofiles.open(full_path, 'rb') as f:
            return await f.read()

    async def delete_file(self, storage_key: str) -> bool:
        if ".." in storage_key:
            return False
            
        full_path = os.path.join(self.base_dir, storage_key)
        if os.path.exists(full_path):
            os.remove(full_path)
            return True
        return False

# We skip S3 implementation for now since the directives strictly forbid touching AWS.
class S3StorageService(StorageService):
    async def upload_file(self, file_content: bytes, filename: str, content_type: str, prefix: str = "") -> str:
        raise NotImplementedError("S3 integration is disabled in this phase.")

    async def get_file(self, storage_key: str) -> Optional[bytes]:
        raise NotImplementedError("S3 integration is disabled in this phase.")

    async def delete_file(self, storage_key: str) -> bool:
        raise NotImplementedError("S3 integration is disabled in this phase.")


def get_storage_service() -> StorageService:
    if settings.STORAGE_BACKEND.lower() == "s3":
        return S3StorageService()
    return LocalStorageService()

storage_service = get_storage_service()
