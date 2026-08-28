import uuid
import logging
from typing import List, Optional
from pydantic import BaseModel
from app.ai.embeddings import embedding_service
from app.ai.vector_store import vector_store
from app.schemas.ai import AIEvidence

logger = logging.getLogger(__name__)

class RetrievedContextChunk(BaseModel):
    score: float
    file_reference: str
    chunk_id: str
    start_line: int
    end_line: int
    repository_id: uuid.UUID
    organization_id: uuid.UUID
    symbol_type: str
    text: Optional[str] = None

class RetrievalEngine:
    def retrieve(
        self,
        query: str,
        organization_id: uuid.UUID,
        repository_id: Optional[uuid.UUID] = None,
        limit: int = 10
    ) -> List[RetrievedContextChunk]:
        """
        Retrieves context-aware code chunks from Qdrant using GraphCodeBERT embeddings.
        STRICTLY enforces organization_id filtering.
        """
        logger.info(f"Retrieving context for query in org {organization_id}. Repo constraint: {repository_id}")
        
        # 1. Generate query embedding (768-dim GraphCodeBERT)
        try:
            query_vector = embedding_service.embed_text(query)
        except Exception as e:
            logger.error(f"Embedding generation failed: {e}")
            raise RuntimeError(f"Embedding generation failed: {e}")
            
        # 2. Query Qdrant with tenant isolation
        try:
            search_results = vector_store.search_similar_code(
                organization_id=str(organization_id),
                query_vector=query_vector,
                limit=limit,
                repository_id=str(repository_id) if repository_id else None
            )
        except Exception as e:
            logger.error(f"Qdrant retrieval failed: {e}")
            raise RuntimeError(f"Qdrant retrieval failed: {e}")

        # 3. Structure the results
        retrieved_chunks = []
        for result in search_results:
            payload = result.payload or {}
            
            chunk = RetrievedContextChunk(
                score=result.score,
                file_reference=payload.get("file_reference", "unknown"),
                chunk_id=payload.get("chunk_id", "unknown"),
                start_line=payload.get("start_line", 0),
                end_line=payload.get("end_line", 0),
                repository_id=uuid.UUID(payload.get("repository_id", "")),
                organization_id=uuid.UUID(payload.get("organization_id", "")),
                symbol_type=payload.get("symbol_type", "unknown")
            )
            retrieved_chunks.append(chunk)
            
        logger.info(f"Retrieved {len(retrieved_chunks)} chunks for query.")
        return retrieved_chunks

retrieval_engine = RetrievalEngine()
