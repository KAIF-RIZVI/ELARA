import io
import zipfile
import httpx
import logging
import time
import jwt
import fnmatch
from typing import Any
from fastapi import HTTPException

from app.core.config import get_settings

logger = logging.getLogger(__name__)

class GitHubService:
    def __init__(self):
        self.settings = get_settings()
        
    def _get_app_jwt(self) -> str:
        """Generate a short-lived JWT for the GitHub App."""
        if not self.settings.GITHUB_APP_ID or not self.settings.GITHUB_APP_PRIVATE_KEY:
            raise ValueError("GitHub App configuration is missing.")
            
        payload = {
            "iat": int(time.time()) - 60, # Subtract 60s for clock skew
            "exp": int(time.time()) + (9 * 60),  # 9 minutes maximum to avoid GitHub strict limits
            "iss": self.settings.GITHUB_APP_ID
        }
        
        # Format the private key properly if it contains escaped newlines from env
        private_key = self.settings.GITHUB_APP_PRIVATE_KEY.replace('\\n', '\n')
        
        return jwt.encode(payload, private_key, algorithm="RS256")
        
    async def get_installation_access_token(self, installation_id: str) -> str:
        """Obtain a short-lived installation access token for a specific installation."""
        app_jwt = self._get_app_jwt()
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://api.github.com/app/installations/{installation_id}/access_tokens",
                headers={
                    "Authorization": f"Bearer {app_jwt}",
                    "Accept": "application/vnd.github.v3+json",
                }
            )
            
            if response.status_code != 201:
                logger.error(f"Failed to get installation token: {response.text}")
                raise HTTPException(status_code=401, detail="Failed to authenticate with GitHub App")
                
            return response.json()["token"]

    async def get_installation_details(self, installation_id: str) -> dict[str, Any]:
        """Fetch details about an installation from GitHub."""
        app_jwt = self._get_app_jwt()
        
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://api.github.com/app/installations/{installation_id}",
                headers={
                    "Authorization": f"Bearer {app_jwt}",
                    "Accept": "application/vnd.github.v3+json",
                }
            )
            response.raise_for_status()
            return response.json()

    async def delete_installation(self, installation_id: str) -> None:
        """Uninstall the app from GitHub by deleting the installation."""
        app_jwt = self._get_app_jwt()
        
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"https://api.github.com/app/installations/{installation_id}",
                headers={
                    "Authorization": f"Bearer {app_jwt}",
                    "Accept": "application/vnd.github.v3+json",
                    "User-Agent": "ELARA-App"
                }
            )
            # GitHub returns 204 No Content on success
            if response.status_code not in (204, 404):
                logger.error(f"Failed to delete GitHub installation: {response.text}")
                # We do not raise an exception here because we still want to disconnect locally

    async def list_accessible_repositories(self, token: str, page: int = 1, per_page: int = 30) -> tuple[list[dict], int]:
        """List repositories accessible to the installation token or PAT."""
        headers = {
            "Authorization": f"token {token}" if token.startswith("ghp_") or token.startswith("github_pat_") else f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
        }
        
        url = "https://api.github.com/installation/repositories" if not token.startswith("ghp_") and not token.startswith("github_pat_") else "https://api.github.com/user/repos"
        
        if url.endswith("/user/repos"):
            url = f"{url}?page={page}&per_page={per_page}&sort=updated"
        else:
            url = f"{url}?page={page}&per_page={per_page}"
            
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            repos = data.get("repositories", data) if isinstance(data, dict) and "repositories" in data else data
            total_count = data.get("total_count", len(repos)) if isinstance(data, dict) else len(repos)
            
            return repos, total_count

    async def get_repository_metadata(self, token: str, repo_id: str) -> dict[str, Any]:
        """Fetch metadata for a specific repository by ID."""
        headers = {
            "Authorization": f"token {token}" if token.startswith("ghp_") or token.startswith("github_pat_") else f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://api.github.com/repositories/{repo_id}", headers=headers)
            response.raise_for_status()
            return response.json()

    async def download_repo_to_memory(self, repo_full_name: str, access_token: str | None = None, branch: str = "main") -> dict[str, bytes]:
        """
        Downloads a GitHub repository as a ZIP archive directly into memory.
        Returns a dictionary mapping file paths to their raw bytes.
        Never writes to disk to satisfy Zero-Trust / Zero-Retention architecture.
        """
        url = f"https://api.github.com/repos/{repo_full_name}/zipball/{branch}"
        headers = {
            "Accept": "application/vnd.github.v3+json",
        }
        if access_token:
            headers["Authorization"] = f"token {access_token}"
            
        logger.info(f"Downloading repository {repo_full_name} into memory stream...")
        
        async with httpx.AsyncClient(follow_redirects=True) as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            
            zip_stream = io.BytesIO(response.content)
            
        files_dict = {}
        MAX_TOTAL_SIZE = 500 * 1024 * 1024  # 500 MB
        MAX_FILE_SIZE = 2 * 1024 * 1024     # 2 MB
        MAX_FILES = 10000
        
        total_extracted_size = 0
        extracted_count = 0
        
        # Comprehensive denylists
        denylist_dirs = {
            ".git", "node_modules", "vendor", "dist", "build", ".next",
            ".cache", "coverage", "__pycache__", ".pytest_cache", "target", "bin", "obj"
        }
        
        denylist_secrets = [
            ".env", ".env.*", "*.pem", "*.key", "*.p12", "*.pfx",
            "credentials.json", "credentials*.json", "service-account*.json"
        ]
        
        supported_extensions = (
            ".py", ".java", ".js", ".jsx", ".ts", ".tsx", ".c", ".h", ".cpp", ".hpp", ".cc", ".cxx", ".cs", ".go", ".rs",
            ".php", ".rb", ".kt", ".kts", ".swift", ".dart", ".scala",
            ".html", ".htm", ".css", ".scss", ".sql",
            ".json", ".yaml", ".yml", ".xml", ".md"
        )
        
        with zipfile.ZipFile(zip_stream) as zf:
            for file_info in zf.infolist():
                if file_info.is_dir():
                    continue
                    
                # 1. ZIP Security: Path traversal protection
                if ".." in file_info.filename or file_info.filename.startswith("/"):
                    continue
                    
                # Get the clean filename (without the root zip directory Org-Repo-Commit/)
                parts = file_info.filename.split("/", 1)
                clean_name = parts[1] if len(parts) > 1 else file_info.filename
                
                # 2. Dependency & Vendor Exclusion
                path_parts = clean_name.split("/")
                if any(part in denylist_dirs for part in path_parts):
                    continue
                    
                # 3. Secret File Exclusion
                filename_only = path_parts[-1]
                if any(fnmatch.fnmatch(filename_only, pattern) for pattern in denylist_secrets):
                    continue
                    
                # 4. Extension Check
                if not clean_name.endswith(supported_extensions):
                    continue
                    
                # 5. ZIP Security: File size limits
                if file_info.file_size > MAX_FILE_SIZE:
                    continue
                    
                if total_extracted_size + file_info.file_size > MAX_TOTAL_SIZE:
                    logger.warning(f"Repository exceeded total extraction limit of {MAX_TOTAL_SIZE} bytes.")
                    break
                    
                if extracted_count >= MAX_FILES:
                    logger.warning(f"Repository exceeded maximum file count of {MAX_FILES}.")
                    break

                with zf.open(file_info) as f:
                    content = f.read()
                    
                    # 6. Binary/Encoding Protection
                    try:
                        # Ensure it's valid UTF-8
                        content.decode("utf-8")
                        files_dict[clean_name] = content
                        
                        total_extracted_size += file_info.file_size
                        extracted_count += 1
                    except UnicodeDecodeError:
                        # Skip binary/invalid encoding files
                        continue
                            
        logger.info(f"Extracted {len(files_dict)} source files into volatile RAM.")
        return files_dict

github_service = GitHubService()