import logging
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue
from app.core.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()

class QdrantVectorStore:
    def __init__(self, collection_name: str = "elara_global_v1"):
        self.client = QdrantClient(url=settings.QDRANT_URL)
        self.collection_name = collection_name
        self.vector_size = 384  # all-MiniLM-L6-v2 embedding size
        self._ensure_collection_exists()
    
    def _ensure_collection_exists(self):
        try:
            collections = self.client.get_collections().collections
            if not any(c.name == self.collection_name for c in collections):
                logger.info(f"Creating Qdrant collection: {self.collection_name}")
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(size=self.vector_size, distance=Distance.COSINE),
                )
                # Ensure multi-tenant payload filtering is indexed for performance
                self.client.create_payload_index(
                    collection_name=self.collection_name,
                    field_name="workspace_id",
                    field_schema="uuid"
                )
        except Exception as e:
            logger.error(f"Error ensuring Qdrant collection exists: {e}")

    def upsert_vectors(self, workspace_id: str, repository_id: str, points: list[dict]):
        """
        points is a list of dicts: {"id": "uuid", "vector": [float], "payload": {"text": "...", "file_path": "..."}}
        """
        qdrant_points = []
        for p in points:
            payload = p.get("payload", {})
            # Hard enforce multi-tenancy at the payload level
            payload["workspace_id"] = workspace_id
            payload["repository_id"] = repository_id
            
            qdrant_points.append(
                PointStruct(
                    id=p["id"],
                    vector=p["vector"],
                    payload=payload
                )
            )
            
        self.client.upsert(
            collection_name=self.collection_name,
            points=qdrant_points
        )
        
    def search_similar_code(self, workspace_id: str, query_vector: list[float], limit: int = 5):
        """
        Search for similar code chunks ONLY within the user's workspace.
        """
        tenant_filter = Filter(
            must=[
                FieldCondition(
                    key="workspace_id",
                    match=MatchValue(value=workspace_id)
                )
            ]
        )
        
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            query_filter=tenant_filter,
            limit=limit,
            with_payload=True
        )
        
        return search_result

vector_store = QdrantVectorStore()