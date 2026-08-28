import uuid
import logging
from typing import List, Optional, Dict
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.project import Repository
from app.models.integrations import GitHubIntegration, IntegrationStatus
from app.services.github_service import github_service
from app.core.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()

from app.ai.retrieval.engine import RetrievedContextChunk

class ContextBuilder:
    def __init__(self, max_context_chars: int = 32000):
        self.max_context_chars = max_context_chars

    async def build_context(self, db: AsyncSession, chunks: List[RetrievedContextChunk]) -> List[RetrievedContextChunk]:
        """
        Deduplicates chunks, fetches raw text from GitHub, and enforces context size limits.
        """
        if not chunks:
            return []

        # Deduplicate chunks by chunk_id
        unique_chunks = {}
        for chunk in chunks:
            if chunk.chunk_id not in unique_chunks:
                unique_chunks[chunk.chunk_id] = chunk
        
        deduped = list(unique_chunks.values())
        # Sort by score descending
        deduped.sort(key=lambda x: x.score, reverse=True)

        # Group by repository to optimize token fetching
        repo_chunks: Dict[uuid.UUID, List[RetrievedContextChunk]] = {}
        for chunk in deduped:
            repo_chunks.setdefault(chunk.repository_id, []).append(chunk)

        # Cache tokens per organization to avoid redundant queries
        org_tokens: Dict[uuid.UUID, str] = {}
        repo_cache: Dict[uuid.UUID, Repository] = {}
        
        # We will use download_repo_to_memory because GitHub doesn't have an easy way to fetch multiple single files efficiently without rate limiting quickly, but to avoid memory bloat we only fetch the files we need.
        # Actually, GitHub API has /repos/{owner}/{repo}/contents/{path}. Let's use that if we can, but we don't have it exposed in github_service. 
        # For P0, since we want to be safe, we will fetch the whole repo into memory ONCE per repo, extract the needed files, and release it.
        # This is safe because repos are capped at 500MB during extraction.
        
        final_context = []
        current_chars = 0

        for repo_id, r_chunks in repo_chunks.items():
            repo = await db.scalar(select(Repository).where(Repository.id == repo_id))
            if not repo:
                continue
                
            org_id = repo.organization_id
            
            # Get token
            if org_id not in org_tokens:
                integration = await db.scalar(
                    select(GitHubIntegration)
                    .where(GitHubIntegration.organization_id == org_id, GitHubIntegration.status == IntegrationStatus.CONNECTED)
                )
                access_token = None
                if integration:
                    if settings.ENVIRONMENT != "production" and settings.GITHUB_DEV_PAT_ENABLED and not integration.github_installation_id:
                        access_token = settings.GITHUB_WEBHOOK_SECRET
                    elif integration.github_installation_id:
                        access_token = await github_service.get_installation_access_token(integration.github_installation_id)
                org_tokens[org_id] = access_token
            
            token = org_tokens.get(org_id)
            if not token:
                logger.warning(f"No GitHub token for org {org_id}. Skipping context building for repo {repo_id}.")
                continue

            try:
                # Fetch repo zip to memory
                files_dict = await github_service.download_repo_to_memory(repo.full_name, token, repo.default_branch)
                
                for chunk in r_chunks:
                    file_content = files_dict.get(chunk.file_reference)
                    if file_content:
                        try:
                            decoded_content = file_content.decode("utf-8")
                            lines = decoded_content.splitlines()
                            
                            # Extract just the lines needed if we have them (1-indexed)
                            if chunk.start_line > 0 and chunk.end_line > 0:
                                start_idx = max(0, chunk.start_line - 1)
                                end_idx = min(len(lines), chunk.end_line)
                                extracted = "\n".join(lines[start_idx:end_idx])
                            else:
                                extracted = decoded_content
                                
                            chunk.text = extracted
                            
                            chunk_chars = len(extracted)
                            if current_chars + chunk_chars <= self.max_context_chars:
                                final_context.append(chunk)
                                current_chars += chunk_chars
                            else:
                                logger.info("Max context characters reached. Truncating further chunks.")
                                break
                        except Exception as decode_err:
                            logger.error(f"Failed to decode file {chunk.file_reference}: {decode_err}")
                            
            except Exception as e:
                logger.error(f"Failed to fetch repo {repo.full_name} for context: {e}")

        return final_context

    def format_for_llm(self, chunks: List[RetrievedContextChunk]) -> str:
        """
        Formats the final context chunks into a prompt-friendly string.
        """
        if not chunks:
            return "No supporting code evidence found."
            
        context_parts = []
        for i, chunk in enumerate(chunks, 1):
            context_parts.append(
                f"--- EVIDENCE {i} ---\n"
                f"File: {chunk.file_reference}\n"
                f"Lines: {chunk.start_line}-{chunk.end_line}\n"
                f"Type: {chunk.symbol_type}\n"
                f"Code:\n```\n{chunk.text}\n```\n"
            )
        return "\n".join(context_parts)

context_builder = ContextBuilder()
