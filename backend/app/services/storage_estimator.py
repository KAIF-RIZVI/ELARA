import json
from typing import Dict, Any, Tuple

class StorageEstimator:
    # 256 MiB in bytes
    HARD_BUDGET_LIMIT_BYTES = 268_435_456 
    
    # 768 float32 dimensions
    RAW_VECTOR_BYTES = 768 * 4 
    
    # Conservative estimate for HNSW graph overhead per point in Qdrant
    INDEX_OVERHEAD_BYTES = 1024 

    @classmethod
    def estimate_payload_bytes(cls, payload: Dict[str, Any]) -> int:
        """
        Estimates the JSON-serialized size of the payload.
        Adds a safety buffer for Qdrant internal persistence overhead.
        """
        try:
            # Add 20% safety buffer for structural overhead in DB
            return int(len(json.dumps(payload)) * 1.2)
        except Exception:
            return 500  # Fallback conservative estimate

    @classmethod
    def estimate_point_storage(cls, payload: Dict[str, Any]) -> Tuple[int, int, int, int]:
        """
        Calculates the estimated storage required for a single semantic point.
        Returns:
            (raw_vector_bytes, estimated_payload_bytes, estimated_index_bytes, estimated_total)
        """
        payload_bytes = cls.estimate_payload_bytes(payload)
        total = cls.RAW_VECTOR_BYTES + payload_bytes + cls.INDEX_OVERHEAD_BYTES
        return (
            cls.RAW_VECTOR_BYTES,
            payload_bytes,
            cls.INDEX_OVERHEAD_BYTES,
            total
        )

storage_estimator = StorageEstimator()
