import asyncio
import uuid
from app.worker.celery_app import celery_app
from app.services.github_service import github_service
from app.ai.ast_parser import ast_parser
from app.ai.vector_store import vector_store
from app.ai.embeddings import embedding_service

def _run_async(coro):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)

@celery_app.task(name="sync_repository_task")
def sync_repository_task(repository_id: str, workspace_id: str):
    """
    Background task to sync a repository from GitHub.
    """
    print(f"Starting zero-trust sync for repository {repository_id} in workspace {workspace_id}")
    
    # In a real app, we'd fetch the repo full_name and access_token from DB using repository_id
    # For now, we mock fetching a small public repo.
    repo_full_name = "jina-ai/jina"  # Placeholder public repo
    access_token = None
    
    # 1. Download to memory
    files_dict = _run_async(github_service.download_repo_to_memory(repo_full_name, access_token))
    
    # 2. AST Parsing
    all_chunks = []
    for file_path, source_code in files_dict.items():
        try:
            chunks = ast_parser.chunk_code(source_code, file_path)
            all_chunks.extend(chunks)
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
            
    print(f"Total chunks extracted: {len(all_chunks)}")
    
    # 3. Vector Embeddings
    points = []
    for chunk in all_chunks:
        vector = embedding_service.embed_text(chunk["text"])
        points.append({
            "id": str(uuid.uuid4()),
            "vector": vector, 
            "payload": {
                "file_path": chunk["text"].split("\n")[0].replace("File: ", ""),
                "type": chunk["type"],
                # Note: In production, text would be encrypted with BYOK KMS before payload insertion
                "text": chunk["text"]
            }
        })
        
    # 4. Upsert to Qdrant
    if points:
        vector_store.upsert_vectors(workspace_id, repository_id, points)
        print(f"Successfully upserted {len(points)} vectors to Qdrant.")
    
    # 5. Volatile RAM is automatically garbage collected here.
    return {"status": "SUCCESS", "repository_id": repository_id, "chunks": len(all_chunks)}