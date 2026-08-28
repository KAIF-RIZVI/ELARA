import logging
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue
from app.core.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()

class QdrantVectorStore:
    def __init__(self, collection_name: str = "elara_global"):
        self.client = QdrantClient(url=settings.QDRANT_URL, api_key=settings.QDRANT_API_KEY)
        self.collection_name = collection_name
        self.vector_size = 768  # GraphCodeBERT embedding size
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
                    field_name="organization_id",
                    field_schema="uuid"
                )
        except Exception as e:
            logger.error(f"Error ensuring Qdrant collection exists: {e}")

    def upsert_vectors(self, organization_id: str, repository_id: str, points: list[dict]):
        """
        points is a list of dicts: {"id": "uuid", "vector": [float], "payload": {"text": "...", "file_path": "..."}}
        """
        qdrant_points = []
        for p in points:
            if len(p["vector"]) != 768:
                raise ValueError(f"CRITICAL: Vector dimension mismatch. Expected 768, got {len(p['vector'])}")
                
            payload = p.get("payload", {})
            # Hard enforce multi-tenancy at the payload level
            payload["organization_id"] = organization_id
            payload["repository_id"] = repository_id
            
            qdrant_points.append(
                PointStruct(
                    id=p["id"],
                    vector=p["vector"],
                    payload=payload
                )
            )
            
        # Chunk the upsert to avoid Qdrant's 32MB payload limit
        batch_size = 100
        for i in range(0, len(qdrant_points), batch_size):
            batch = qdrant_points[i:i + batch_size]
            self.client.upsert(
                collection_name=self.collection_name,
                points=batch
            )
        
    def search_similar_code(self, organization_id: str, query_vector: list[float], limit: int = 5, repository_id: str = None):
        """
        Search for similar code chunks ONLY within the specific organization (and optionally repository).
        """
        must_conditions = [
            FieldCondition(
                key="organization_id",
                match=MatchValue(value=organization_id)
            )
        ]
        
        if repository_id:
            must_conditions.append(
                FieldCondition(
                    key="repository_id",
                    match=MatchValue(value=repository_id)
                )
            )
            
        tenant_filter = Filter(must=must_conditions)
        
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            query_filter=tenant_filter,
            limit=limit,
            with_payload=True
        )
        
        return search_result

    def delete_repository_vectors(self, organization_id: str, repository_id: str):
        """
        Delete all vectors for a given repository within an organization (for full re-indexing).
        """
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=Filter(
                must=[
                    FieldCondition(
                        key="organization_id",
                        match=MatchValue(value=organization_id)
                    ),
                    FieldCondition(
                        key="repository_id",
                        match=MatchValue(value=repository_id)
                    )
                ]
            )
        )

    def delete_organization_vectors(self, organization_id: str):
        """
        Delete all vectors for an entire organization.
        Uses a strict payload filter to ensure tenant isolation.
        Idempotent operation (succeeds safely if vectors don't exist).
        """
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=Filter(
                must=[
                    FieldCondition(
                        key="organization_id",
                        match=MatchValue(value=organization_id)
                    )
                ]
            )
        )

vector_store = QdrantVectorStore()