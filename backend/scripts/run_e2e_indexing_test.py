import asyncio
import uuid
import os
import sys

# Ensure backend directory is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.core.database import AsyncSessionLocal
from app.models.project import Repository, RepoIndexJob, JobStatus, Project, ProjectStatus
from app.models.organization import Organization, OrganizationRole, OrganizationMember
from app.services.repository_processor import repository_processor
from app.ai.vector_store import vector_store
from sqlalchemy import select
from datetime import datetime, timezone

async def test_e2e():
    print("Starting E2E Indexing Test...")
    async with AsyncSessionLocal() as db:
        # Create a mock organization
        org_id = uuid.uuid4()
        org = Organization(id=org_id, name="Test Org E2E", slug=f"test-org-{org_id}")
        db.add(org)
        
        # Create a mock repo
        repo_id = uuid.uuid4()
        repo = Repository(
            id=repo_id,
            organization_id=org_id,
            provider="github",
            external_id="mock_ext_id",
            full_name="mock/test-repo",
            default_branch="main",
            visibility="private",
            is_private=True
        )
        db.add(repo)
        
        # Create a job
        job_id = uuid.uuid4()
        job = RepoIndexJob(
            id=job_id,
            repository_id=repo_id,
            organization_id=org_id,
            commit_sha="mock_sha",
            status=JobStatus.QUEUED
        )
        db.add(job)
        await db.commit()
        
        # We need to mock github_service.download_repo_to_memory just for this test
        # so it doesn't try to use an invalid token
        from app.services.github_service import github_service
        
        async def mock_download(*args, **kwargs):
            return {
                "test.py": b"def hello():\n    print('world')\n",
                "index.js": b"console.log('test');\n",
                "styles.css": b"body { color: red; }\n",
                "index.html": b"<html><body>Hello</body></html>\n",
                "README.md": b"# Test Repo\nThis is a test.\n",
                ".git/config": b"[core]\n\trepositoryformatversion = 0\n",
                "node_modules/test/index.js": b"console.log('should be ignored');\n"
            }
            
        github_service.download_repo_to_memory = mock_download
        
        print("Mock DB entries created. Running processor...")
        
        # Inject our mock integration token logic bypass in the processor just by temporarily overriding the integration check
        # Wait, the processor explicitly fetches an integration and token. 
        # Since this is a test, I can just monkeypatch `get_installation_access_token` and `Integration` check.
        # It's easier to just temporarily patch `github_service.get_installation_access_token` and create an integration.
        
        from app.models.integrations import GitHubIntegration, IntegrationStatus
        integration = GitHubIntegration(
            organization_id=org_id,
            status=IntegrationStatus.CONNECTED,
            github_installation_id="mock_install_id"
        )
        db.add(integration)
        await db.commit()
        
        async def mock_token(*args, **kwargs):
            return "mock_token"
            
        github_service.get_installation_access_token = mock_token
        
        # Run process
        try:
            await repository_processor.process_job(db, job_id, org_id)
        except Exception as e:
            print(f"Error during processing: {e}")
            
        # Verify job
        db_job = await db.scalar(select(RepoIndexJob).where(RepoIndexJob.id == job_id))
        print(f"Job Status: {db_job.status}")
        print(f"Bytes Processed: {db_job.bytes_processed}")
        print(f"Files Indexed: {db_job.files_indexed}")
        print(f"Vectors Generated: {db_job.vectors_generated}")
        print(f"Truncation Reason: {db_job.truncation_reason}")
        
        # Verify vector store
        results = vector_store.search_similar_code(
            organization_id=str(org_id),
            query_vector=[0.1] * 768,  # random vector
            repository_id=str(repo_id),
            limit=10
        )
        
        print(f"Found {len(results)} vectors in Qdrant:")
        for r in results:
            print(f" - Vector len: {len(r.vector) if r.vector else 'Hidden (but Qdrant requires 768)'}")
            print(f" - Payload: {r.payload}")
            if "source_code" in r.payload or "text" in r.payload:
                print("   !!! WARNING: Raw source code found in payload!")
                
        # Cleanup
        vector_store.delete_repository_vectors(str(org_id), str(repo_id))
        
if __name__ == "__main__":
    asyncio.run(test_e2e())
