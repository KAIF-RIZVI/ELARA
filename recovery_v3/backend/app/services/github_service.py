import io
import zipfile
import httpx
import logging

logger = logging.getLogger(__name__)

class GitHubService:
    @staticmethod
    async def download_repo_to_memory(repo_full_name: str, access_token: str | None = None, branch: str = "main") -> dict[str, bytes]:
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
        with zipfile.ZipFile(zip_stream) as zf:
            for file_info in zf.infolist():
                if not file_info.is_dir():
                    # Extract python files for now. In a real system, support more extensions.
                    if file_info.filename.endswith(".py"):
                        with zf.open(file_info) as f:
                            # Use the filename excluding the root zip directory name (GitHub formats it as Org-Repo-Commit/)
                            parts = file_info.filename.split("/", 1)
                            clean_name = parts[1] if len(parts) > 1 else file_info.filename
                            files_dict[clean_name] = f.read()
                            
        logger.info(f"Extracted {len(files_dict)} Python files into volatile RAM.")
        return files_dict

github_service = GitHubService()