import os
import shutil
import uuid
import hashlib
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.project import RepoIndexJob, JobStatus, Repository, SyncStatus
from app.models.organization import OrganizationAuditLog
from app.services.repository_indexing import repository_indexing_service
from app.services.github_service import github_service
from app.services.storage_estimator import storage_estimator
from app.ai.ast_parser import ast_parser
from app.ai.code_chunker import code_chunker
from app.ai.vector_store import vector_store
from app.ai.embeddings import embedding_service
from app.core.config import get_settings
from datetime import datetime, timezone

settings = get_settings()

class RepositoryProcessor:
    async def process_job(self, db: AsyncSession, job_id: uuid.UUID, organization_id: uuid.UUID) -> None:
        """
        Executes the repository processing pipeline using a memory-bounded streaming architecture.
        """
        job = await repository_indexing_service.get_job(db, job_id, organization_id)
        if not job or job.status == JobStatus.CANCELLED:
            return

        repo = await db.scalar(select(Repository).where(Repository.id == job.repository_id))
        if not repo:
            await repository_indexing_service.update_job_status(db, job_id, JobStatus.FAILED, error="Repository not found")
            return

        workspace_dir = f"/tmp/elara/indexing/{job_id}/"
        
        # Emit Audit Log - Started
        audit_start = OrganizationAuditLog(
            organization_id=organization_id,
            event_type="INDEX_STARTED",
            resource_type="Repository",
            resource_id=str(repo.id),
            new_values={"job_id": str(job.id)}
        )
        db.add(audit_start)
        await db.commit()
        
        try:
            # === STAGE 1: CLONING ===
            await repository_indexing_service.update_job_status(db, job_id, JobStatus.CLONING)
            repo.sync_status = SyncStatus.SYNCING
            await db.commit()
            
            os.makedirs(workspace_dir, exist_ok=True)
            
            from app.models.integrations import GitHubIntegration, IntegrationStatus
            integration = await db.scalar(select(GitHubIntegration).where(
                GitHubIntegration.organization_id == organization_id,
                GitHubIntegration.status == IntegrationStatus.CONNECTED
            ))
            
            access_token = None
            if integration:
                if settings.ENVIRONMENT != "production" and settings.GITHUB_DEV_PAT_ENABLED and not integration.github_installation_id:
                    access_token = settings.GITHUB_WEBHOOK_SECRET
                elif integration.github_installation_id:
                    access_token = await github_service.get_installation_access_token(integration.github_installation_id)
            
            if not access_token:
                raise ValueError("No valid GitHub integration found to download repository source.")
                
            files_dict = await github_service.download_repo_to_memory(repo.full_name, access_token, repo.default_branch)
            
            # Write to ephemeral disk
            for filepath, content in files_dict.items():
                full_path = os.path.join(workspace_dir, filepath)
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, "wb") as f:
                    f.write(content)
                    
            # === STAGE 2: PURGE OLD VECTORS ===
            # We clear out old index before beginning our streaming loop
            vector_store.delete_repository_vectors(str(organization_id), str(repo.id))
            
            # === STAGE 3: STREAMING INDEX (Parse -> Embed -> Store) ===
            await repository_indexing_service.update_job_status(db, job_id, JobStatus.EMBEDDING)
            
            ast_supported = {
                ".py": "python", ".js": "javascript", ".jsx": "javascript", ".ts": "typescript", ".tsx": "typescript",
                ".java": "java", ".c": "c", ".h": "c", ".cpp": "cpp", ".hpp": "cpp", ".cc": "cpp", ".cxx": "cpp",
                ".cs": "c-sharp", ".go": "go", ".rs": "rust", ".php": "php", ".kt": "kotlin", ".kts": "kotlin", ".swift": "swift"
            }
            structure_supported = {
                ".html": "html", ".htm": "html", ".css": "css", ".scss": "scss", ".sql": "sql", 
                ".json": "json", ".yaml": "yaml", ".yml": "yaml", ".xml": "xml", ".md": "markdown"
            }
            
            # Prioritize files (P0/P1 first)
            def get_file_priority(path: str) -> int:
                path = path.lower()
                if "test" in path or "mock" in path or "fixture" in path:
                    return 100
                if path.endswith((".py", ".js", ".ts", ".go", ".rs", ".java", ".cpp")):
                    return 10
                if path.endswith((".html", ".css", ".scss", ".json", ".yaml", ".md")):
                    return 50
                return 200
                
            sorted_files = sorted(files_dict.keys(), key=get_file_priority)
            
            job.budget_limit = storage_estimator.HARD_BUDGET_LIMIT_BYTES
            job.budget_exceeded = False
            job.files_indexed = 0
            job.files_skipped = 0
            job.bytes_processed = 0
            await db.commit()

            batch_size = 32
            current_batch = []
            
            for filepath in sorted_files:
                if job.budget_exceeded:
                    job.files_skipped += 1
                    continue
                    
                full_path = os.path.join(workspace_dir, filepath)
                with open(full_path, "rb") as f:
                    source_bytes = f.read()
                    
                job.bytes_processed += len(source_bytes)
                job.files_indexed += 1
                
                _, ext = os.path.splitext(filepath)
                ext = ext.lower()
                
                chunks = None
                actual_language = "unknown"
                
                if ext in ast_supported:
                    actual_language = ast_supported[ext]
                    try:
                        chunks = ast_parser.chunk_code(source_bytes, filepath, actual_language)
                    except Exception:
                        pass
                        
                if not chunks and ext in structure_supported:
                    actual_language = structure_supported[ext]
                    try:
                        chunks = code_chunker.structure_aware_chunk(source_bytes, filepath, actual_language)
                    except Exception:
                        pass
                        
                if not chunks:
                    if ext in ast_supported:
                        actual_language = ast_supported[ext]
                    elif ext in structure_supported:
                        actual_language = structure_supported[ext]
                    try:
                        chunks = code_chunker.generic_chunk(source_bytes, filepath, language=actual_language)
                    except Exception:
                        chunks = []
                        
                for chunk in chunks:
                    chunk["language"] = actual_language
                    chunk["filepath"] = filepath
                    current_batch.append(chunk)
                    
                    if len(current_batch) >= batch_size:
                        budget_hit = await self._process_batch(current_batch, repo, job, organization_id, db)
                        current_batch = []
                        if budget_hit:
                            job.budget_exceeded = True
                            job.truncation_reason = "256_MIB_QUOTA_EXCEEDED"
                            break

            # Flush remaining chunks
            if current_batch and not job.budget_exceeded:
                budget_hit = await self._process_batch(current_batch, repo, job, organization_id, db)
                if budget_hit:
                    job.budget_exceeded = True
                    job.truncation_reason = "256_MIB_QUOTA_EXCEEDED"

            # === SUCCESS ===
            final_status = JobStatus.PARTIALLY_INDEXED if job.budget_exceeded else JobStatus.COMPLETED
            
            await repository_indexing_service.update_job_status(db, job_id, final_status)
            repo.sync_status = SyncStatus.COMPLETED
            repo.last_synced_at = datetime.now(timezone.utc)
            await db.commit()
            
            # Emit Audit Log - Success/Partial
            audit_end = OrganizationAuditLog(
                organization_id=organization_id,
                event_type=f"INDEX_{final_status.value}",
                resource_type="Repository",
                resource_id=str(repo.id),
                new_values={
                    "job_id": str(job.id),
                    "bytes_processed": job.bytes_processed,
                    "estimated_total_semantic_storage": job.estimated_total_semantic_storage,
                    "vectors_generated": job.vectors_generated,
                    "truncation_reason": job.truncation_reason
                }
            )
            db.add(audit_end)
            await db.commit()

        except Exception as e:
            await repository_indexing_service.update_job_status(
                db, job_id, JobStatus.FAILED, error=str(e), error_code="PROCESSING_FAILURE"
            )
            repo.sync_status = SyncStatus.FAILED
            
            audit_fail = OrganizationAuditLog(
                organization_id=organization_id,
                event_type="INDEX_FAILED",
                resource_type="Repository",
                resource_id=str(repo.id),
                new_values={"job_id": str(job.id), "error": str(e)}
            )
            db.add(audit_fail)
            await db.commit()
            raise e
        finally:
            # === STAGE 6: CLEANUP ===
            if os.path.exists(workspace_dir):
                shutil.rmtree(workspace_dir, ignore_errors=True)

    async def _process_batch(self, batch_chunks, repo, job, organization_id, db) -> bool:
        # --- Safety Quiescence Check ---
        # Before every Qdrant write, strictly verify the organization is still active.
        from app.models.organization import Organization, OrganizationStatus
        org_status = await db.scalar(select(Organization.status).where(Organization.id == organization_id))
        if not org_status or org_status == OrganizationStatus.DELETING or org_status == OrganizationStatus.DELETED:
            raise Exception("Organization is being deleted. Aborting worker to prevent vector recreation.")

        texts = [c["text"] for c in batch_chunks]
        vectors = embedding_service.embed_texts(texts)
        
        points = []
        batch_vector_bytes = 0
        batch_payload_bytes = 0
        batch_index_bytes = 0
        batch_total_bytes = 0
        
        for chunk, vector in zip(batch_chunks, vectors):
            hash_input = f"{repo.id}:{chunk['filepath']}:{chunk['id']}"
            det_id = str(uuid.UUID(hashlib.md5(hash_input.encode()).hexdigest()))
            
            # Data minimization layer: NEVER include raw source code
            payload = {
                "organization_id": str(organization_id),
                "repository_id": str(repo.id),
                "file_reference": chunk['filepath'],
                "symbol_type": chunk.get("type", "unknown"),
                "chunk_id": chunk["id"],
                "language": chunk.get("language", "unknown"),
                "embedding_model": "microsoft/graphcodebert-base",
                "model_version": "microsoft/graphcodebert-base",
                "index_version": "v2",
                "start_line": chunk.get("start_line", 0),
                "end_line": chunk.get("end_line", 0),
                "processing_tier": chunk.get("processing_tier", 3),
                "processing_method": chunk.get("processing_method", "generic_line_chunker")
            }
            
            vec_bytes, pay_bytes, idx_bytes, total_bytes = storage_estimator.estimate_point_storage(payload)
            
            if job.estimated_total_semantic_storage + batch_total_bytes + total_bytes > storage_estimator.HARD_BUDGET_LIMIT_BYTES:
                if points:
                    vector_store.upsert_vectors(str(organization_id), str(repo.id), points)
                    job.estimated_vector_storage += batch_vector_bytes
                    job.estimated_payload_storage += batch_payload_bytes
                    job.estimated_index_overhead_bytes += batch_index_bytes
                    job.estimated_total_semantic_storage += batch_total_bytes
                    job.vectors_generated += len(points)
                    job.symbols_processed += len(points)
                    await db.commit()
                return True
                
            batch_vector_bytes += vec_bytes
            batch_payload_bytes += pay_bytes
            batch_index_bytes += idx_bytes
            batch_total_bytes += total_bytes
            
            points.append({
                "id": det_id,
                "vector": vector,
                "payload": payload
            })
            
        if points:
            vector_store.upsert_vectors(str(organization_id), str(repo.id), points)
            job.estimated_vector_storage += batch_vector_bytes
            job.estimated_payload_storage += batch_payload_bytes
            job.estimated_index_overhead_bytes += batch_index_bytes
            job.estimated_total_semantic_storage += batch_total_bytes
            job.vectors_generated += len(points)
            job.symbols_processed += len(points)
            await db.commit()
            
        return False

repository_processor = RepositoryProcessor()
