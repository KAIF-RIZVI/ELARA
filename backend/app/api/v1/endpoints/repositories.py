from fastapi import APIRouter, status, HTTPException, Depends
from typing import Optional
from app.api.deps import CurrentUser, SessionDep, RequireRole, RequireOrganizationRole
from app.models.identity import MemberRole, WorkspaceMember
from app.models.organization import OrganizationMember, OrganizationRole
from app.worker.tasks.repo_tasks import sync_repository_task
from app.schemas.repository import RepositoryCreate, RepositoryResponse
from app.services.repository import repository_service
import uuid

router = APIRouter()

@router.get("", response_model=list[RepositoryResponse])
async def list_repositories(
    db: SessionDep, 
    current_user: CurrentUser,
    workspace_id: Optional[uuid.UUID] = None,
    organization_id: Optional[uuid.UUID] = None
):
    if workspace_id:
        await RequireRole(MemberRole.DEVELOPER)(workspace_id, db, current_user)
        repos = await repository_service.get_by_workspace(db, workspace_id=workspace_id)
    elif organization_id:
        await RequireOrganizationRole(OrganizationRole.DEVELOPER)(organization_id, db, current_user)
        repos = await repository_service.get_by_organization(db, organization_id=organization_id)
    else:
        raise HTTPException(status_code=400, detail="Must provide either workspace_id or organization_id")
        
    result = []
    for repo in repos:
        repo_dict = RepositoryResponse.model_validate(repo).model_dump()
        repo_dict["health_score"] = repository_service.calculate_health_score(repo)
        result.append(repo_dict)
    return result

@router.post("", response_model=RepositoryResponse)
async def connect_repository(
    repo_in: RepositoryCreate,
    db: SessionDep,
    current_user: CurrentUser
):
    if repo_in.workspace_id:
        await RequireRole(MemberRole.ADMIN)(repo_in.workspace_id, db, current_user)
    elif repo_in.organization_id:
        await RequireOrganizationRole(OrganizationRole.PROJECT_MANAGER)(repo_in.organization_id, db, current_user)
    else:
        raise HTTPException(status_code=400, detail="Must provide either workspace_id or organization_id")

    try:
        repo = await repository_service.connect_repository(
            db,
            repo_in=repo_in,
            user_id=current_user.id
        )
        repo_dict = RepositoryResponse.model_validate(repo).model_dump()
        repo_dict["health_score"] = repository_service.calculate_health_score(repo)
        return repo_dict
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{repository_id}", response_model=RepositoryResponse)
async def get_repository(
    repository_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    workspace_id: Optional[uuid.UUID] = None,
    organization_id: Optional[uuid.UUID] = None
):
    if workspace_id:
        await RequireRole(MemberRole.DEVELOPER)(workspace_id, db, current_user)
    elif organization_id:
        await RequireOrganizationRole(OrganizationRole.DEVELOPER)(organization_id, db, current_user)
    else:
        raise HTTPException(status_code=400, detail="Must provide either workspace_id or organization_id")

    repo = await repository_service.get(db, repository_id)
    if not repo:
        raise HTTPException(status_code=404, detail="Repository not found")
        
    repo_dict = RepositoryResponse.model_validate(repo).model_dump()
    repo_dict["health_score"] = repository_service.calculate_health_score(repo)
    return repo_dict

@router.delete("/{repository_id}", status_code=status.HTTP_204_NO_CONTENT)
async def disconnect_repository(
    repository_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    workspace_id: Optional[uuid.UUID] = None,
    organization_id: Optional[uuid.UUID] = None
):
    if workspace_id:
        await RequireRole(MemberRole.ADMIN)(workspace_id, db, current_user)
    elif organization_id:
        await RequireOrganizationRole(OrganizationRole.PROJECT_MANAGER)(organization_id, db, current_user)
    else:
        raise HTTPException(status_code=400, detail="Must provide either workspace_id or organization_id")

    try:
        await repository_service.disconnect_repository(
            db,
            repository_id=repository_id,
            workspace_id=workspace_id,
            organization_id=organization_id,
            user_id=current_user.id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{repository_id}/sync", status_code=status.HTTP_202_ACCEPTED)
async def sync_repository(
    repository_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    workspace_id: Optional[uuid.UUID] = None,
    organization_id: Optional[uuid.UUID] = None
):
    """
    Deprecated compatibility wrapper for existing frontend workflows.
    Delegates internally to the new indexing system.
    """
    if workspace_id:
        raise HTTPException(status_code=403, detail="Enterprise AI pipelines are disabled for Personal Workspaces.")
    if not organization_id:
        raise HTTPException(status_code=400, detail="Organization ID is required")
        
    await RequireOrganizationRole(OrganizationRole.PROJECT_MANAGER)(organization_id, db, current_user)
    
    # Delegate to the new indexing service
    from app.services.repository_indexing import repository_indexing_service
    from app.worker.tasks.repo_tasks import index_repository_job
    
    job = await repository_indexing_service.create_indexing_job(db, organization_id, repository_id)
    index_repository_job.delay(str(job.id), str(organization_id))
    return {"message": "Repository sync initiated in the background", "job_id": str(job.id)}

@router.post("/{repository_id}/index", status_code=status.HTTP_202_ACCEPTED)
async def index_repository(
    repository_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    organization_id: uuid.UUID
):
    await RequireOrganizationRole(OrganizationRole.PROJECT_MANAGER)(organization_id, db, current_user)
    from app.services.repository_indexing import repository_indexing_service
    from app.worker.tasks.repo_tasks import index_repository_job
    
    job = await repository_indexing_service.create_indexing_job(db, organization_id, repository_id)
    index_repository_job.delay(str(job.id), str(organization_id))
    return {"job_id": str(job.id), "status": job.status}

@router.get("/{repository_id}/index-status")
async def get_index_status(
    repository_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    organization_id: uuid.UUID
):
    await RequireOrganizationRole(OrganizationRole.DEVELOPER)(organization_id, db, current_user)
    from app.services.repository_indexing import repository_indexing_service
    
    job = await repository_indexing_service.get_active_job_for_repository(db, repository_id)
    if not job:
        # If no active job, just return the latest state
        return {"active": False, "status": "UNINDEXED"}
    
    return {
        "active": True,
        "job_id": str(job.id),
        "status": job.status,
        "files_indexed": job.files_indexed,
        "files_skipped": getattr(job, 'files_skipped', 0),
        "symbols_processed": job.symbols_processed,
        "vectors_generated": job.vectors_generated,
        "bytes_processed": getattr(job, 'bytes_processed', 0),
        "estimated_total_semantic_storage": getattr(job, 'estimated_total_semantic_storage', 0),
        "budget_exceeded": getattr(job, 'budget_exceeded', False),
        "truncation_reason": getattr(job, 'truncation_reason', None),
        "commit_sha": getattr(job, 'commit_sha', None),
        "indexing_started_at": getattr(job, 'indexing_started_at', None),
        "indexing_completed_at": getattr(job, 'indexing_completed_at', None)
    }

@router.post("/{repository_id}/index/cancel")
async def cancel_index_job(
    repository_id: uuid.UUID,
    job_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    organization_id: uuid.UUID
):
    await RequireOrganizationRole(OrganizationRole.PROJECT_MANAGER)(organization_id, db, current_user)
    from app.services.repository_indexing import repository_indexing_service
    
    job = await repository_indexing_service.cancel_job(db, job_id, organization_id)
    return {"job_id": str(job.id), "status": job.status}

from pydantic import BaseModel
from app.ai.embeddings import embedding_service
from app.ai.vector_store import QdrantVectorStore

class SemanticSearchResult(BaseModel):
    id: str
    score: float
    file_reference: str
    symbol_type: str
    language: str

class SemanticSearchResponse(BaseModel):
    results: list[SemanticSearchResult]

@router.get("/{repository_id}/semantic-search", response_model=SemanticSearchResponse)
async def semantic_search_repository(
    repository_id: uuid.UUID,
    q: str,
    organization_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    limit: int = 10,
):
    """
    Search the semantic index (Qdrant) for a specific repository.
    """
    await RequireOrganizationRole(OrganizationRole.DEVELOPER)(organization_id, db, current_user)
    
    repo = await repository_service.get(db, id=repository_id)
    if not repo or repo.organization_id != organization_id:
        raise HTTPException(status_code=404, detail="Repository not found")

    vector_store = QdrantVectorStore()
    query_vector = embedding_service.embed_text(q)
    
    qdrant_results = vector_store.search_similar_code(
        organization_id=str(organization_id),
        query_vector=query_vector,
        limit=limit,
        repository_id=str(repository_id)
    )
    
    results = []
    for point in qdrant_results:
        results.append(
            SemanticSearchResult(
                id=point.id,
                score=point.score,
                file_reference=point.payload.get("file_reference", "unknown"),
                symbol_type=point.payload.get("symbol_type", "unknown"),
                language=point.payload.get("language", "unknown")
            )
        )
        
    return SemanticSearchResponse(results=results)

@router.get("/{repository_id}/jobs")
async def get_repository_jobs(
    repository_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    organization_id: uuid.UUID
):
    await RequireOrganizationRole(OrganizationRole.DEVELOPER)(organization_id, db, current_user)
    
    from sqlalchemy import select
    from app.models.project import RepoIndexJob
    
    stmt = select(RepoIndexJob).where(RepoIndexJob.repository_id == repository_id).order_by(RepoIndexJob.created_at.desc())
    result = await db.execute(stmt)
    jobs = result.scalars().all()
    
    return [
        {
            "id": str(job.id),
            "status": job.status,
            "commit_sha": job.commit_sha,
            "files_indexed": job.files_indexed,
            "files_skipped": getattr(job, 'files_skipped', 0),
            "symbols_processed": job.symbols_processed,
            "vectors_generated": job.vectors_generated,
            "bytes_processed": getattr(job, 'bytes_processed', 0),
            "estimated_total_semantic_storage": getattr(job, 'estimated_total_semantic_storage', 0),
            "budget_exceeded": getattr(job, 'budget_exceeded', False),
            "truncation_reason": getattr(job, 'truncation_reason', None),
            "indexing_started_at": getattr(job, 'indexing_started_at', None),
            "indexing_completed_at": getattr(job, 'indexing_completed_at', None),
            "created_at": job.created_at,
            "updated_at": job.updated_at
        }
        for job in jobs
    ]

@router.post("/{repository_id}/refresh", status_code=status.HTTP_202_ACCEPTED)
async def refresh_repository_metadata(
    repository_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser,
    workspace_id: Optional[uuid.UUID] = None,
    organization_id: Optional[uuid.UUID] = None
):
    """
    Deprecated compatibility wrapper for existing frontend workflows.
    Delegates internally to the new indexing system.
    """
    if workspace_id:
        raise HTTPException(status_code=403, detail="Enterprise AI pipelines are disabled for Personal Workspaces.")
    if not organization_id:
        raise HTTPException(status_code=400, detail="Organization ID is required")
        
    await RequireOrganizationRole(OrganizationRole.PROJECT_MANAGER)(organization_id, db, current_user)
    
    # Delegate to the new indexing service
    from app.services.repository_indexing import repository_indexing_service
    from app.worker.tasks.repo_tasks import index_repository_job
    
    job = await repository_indexing_service.create_indexing_job(db, organization_id, repository_id)
    index_repository_job.delay(str(job.id), str(organization_id))
    return {"message": "Repository refresh initiated in the background", "job_id": str(job.id)}

from pydantic import BaseModel

class BatchImportRequest(BaseModel):
    github_repository_ids: list[str]

@router.post("/batch", status_code=status.HTTP_202_ACCEPTED)
async def batch_import_repositories(
    req: BatchImportRequest,
    organization_id: uuid.UUID,
    db: SessionDep,
    current_user: CurrentUser
):
    """
    Batch import GitHub repositories from an organization's GitHub Integration.
    Fetches authoritative metadata, ensures idempotency, and queues indexing.
    """
    await RequireOrganizationRole(OrganizationRole.ADMIN)(organization_id, db, current_user)
    
    from app.models.integrations import GitHubIntegration, IntegrationStatus
    from app.models.project import Repository
    from app.models.organization import OrganizationAuditLog
    from sqlalchemy import select
    from app.services.github_service import github_service
    from app.core.config import get_settings
    
    settings = get_settings()
    
    stmt = select(GitHubIntegration).where(
        GitHubIntegration.organization_id == organization_id,
        GitHubIntegration.status == IntegrationStatus.CONNECTED
    )
    result = await db.execute(stmt)
    integration = result.scalar_one_or_none()
    
    import sys
    print(f"BATCH_IMPORT_PAYLOAD: {req.github_repository_ids}", file=sys.stderr)
    
    if not integration:
        raise HTTPException(status_code=400, detail="GITHUB_NOT_CONNECTED")
        
    try:
        if settings.ENVIRONMENT != "production" and settings.GITHUB_DEV_PAT_ENABLED and not integration.github_installation_id:
            token = settings.GITHUB_WEBHOOK_SECRET
        else:
            token = await github_service.get_installation_access_token(integration.github_installation_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="GITHUB_INSTALLATION_INVALID")
        
    from app.services.repository_indexing import repository_indexing_service
    from app.worker.tasks.repo_tasks import index_repository_job
    from datetime import datetime, timezone
    import dateutil.parser
    
    results = []
    
    for ext_id in req.github_repository_ids:
        # Check if already exists
        stmt_repo = select(Repository).where(
            Repository.organization_id == organization_id,
            Repository.external_id == ext_id,
            Repository.provider == "github"
        )
        repo_result = await db.execute(stmt_repo)
        existing_repo = repo_result.scalar_one_or_none()
        
        if existing_repo:
            results.append({"external_id": ext_id, "status": "ALREADY_EXISTS", "repository_id": str(existing_repo.id)})
            continue
            
        try:
            meta = await github_service.get_repository_metadata(token, ext_id)
        except Exception as e:
            import sys
            print(f"FETCH_FAILED for {ext_id}: {e}", file=sys.stderr)
            import traceback
            traceback.print_exc(file=sys.stderr)
            results.append({"external_id": ext_id, "status": "FETCH_FAILED"})
            continue
            
        last_push = None
        if meta.get("pushed_at"):
            try:
                last_push = dateutil.parser.parse(meta["pushed_at"])
            except:
                pass

        new_repo = Repository(
            organization_id=organization_id,
            provider="github",
            external_id=ext_id,
            full_name=meta.get("full_name"),
            default_branch=meta.get("default_branch", "main"),
            provider_repository_id=ext_id,
            github_installation_id=integration.github_installation_id,
            visibility="private" if meta.get("private") else "public",
            language=meta.get("language"),
            is_private=meta.get("private", False),
            owner=meta.get("owner", {}).get("login"),
            clone_url=meta.get("clone_url"),
            html_url=meta.get("html_url"),
            repository_size=meta.get("size"),
            last_push_at=last_push
        )
        db.add(new_repo)
        await db.flush() # flush to get new_repo.id
        
        repo_id_str = str(new_repo.id)
        
        # Queue indexing safely without blocking the event loop
        try:
            job = await repository_indexing_service.create_indexing_job(db, organization_id, new_repo.id)
            
            import asyncio
            loop = asyncio.get_running_loop()
            try:
                # Run the celery delay in a separate thread so it doesn't block the async event loop if Redis is down
                await asyncio.wait_for(
                    loop.run_in_executor(None, lambda: index_repository_job.delay(str(job.id), str(organization_id))),
                    timeout=2.0
                )
            except Exception as celery_err:
                import logging
                logger = logging.getLogger(__name__)
                logger.error(f"Failed to queue indexing job to Celery/Redis: {celery_err}")
                results.append({"external_id": ext_id, "status": "IMPORTED_BUT_INDEXING_FAILED", "repository_id": repo_id_str})
            else:
                try:
                    async with db.begin_nested():
                        audit = OrganizationAuditLog(
                            organization_id=organization_id,
                            actor_id=current_user.id,
                            event_type="repository.imported",
                            resource_type="Repository",
                            resource_id=repo_id_str,
                            new_values={"full_name": new_repo.full_name}
                        )
                        db.add(audit)
                except Exception as audit_err:
                    import logging
                    logger = logging.getLogger(__name__)
                    logger.error(f"Failed to save audit log for {ext_id}: {audit_err}")
                    # We still imported it successfully!
                
                results.append({"external_id": ext_id, "status": "IMPORTED", "repository_id": repo_id_str, "job_id": str(job.id)})
                
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Indexing queue failed for {ext_id}: {e}")
            results.append({"external_id": ext_id, "status": "INDEXING_QUEUE_FAILED", "repository_id": repo_id_str})
            
        try:
            await db.commit()
        except Exception as e:
            await db.rollback()
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Commit failed for repo {ext_id}: {e}")
            
            # Remove the previous successful result since we failed to commit
            results = [r for r in results if r.get("external_id") != ext_id]
            results.append({"external_id": ext_id, "status": "COMMIT_FAILED", "error": str(e)})
            continue
            
    return {"results": results}