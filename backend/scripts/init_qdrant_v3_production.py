import os
import requests
import json

# Production Qdrant Configuration
QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = os.getenv("QDRANT_PORT", "6333")
QDRANT_URL = f"http://{QDRANT_HOST}:{QDRANT_PORT}"
API_KEY = os.getenv("QDRANT_API_KEY", "")

COLLECTION_NAME = "elara_global_v3"

def init_production_collection():
    headers = {"Content-Type": "application/json"}
    if API_KEY:
        headers["api-key"] = API_KEY

    print(f"Connecting to Qdrant at {QDRANT_URL}")
    
    # 1. Check if collection already exists
    try:
        response = requests.get(f"{QDRANT_URL}/collections/{COLLECTION_NAME}", headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"Collection {COLLECTION_NAME} already exists. Skipping creation.")
            return
    except requests.exceptions.ConnectionError:
        print("Failed to connect to Qdrant. Make sure the cluster is running.")
        return

    # 2. Immutable ELARA contract payload for creation
    payload = {
        "vectors": {
            "size": 768,  # microsoft/graphcodebert-base dimension
            "distance": "Cosine",
        },
        "shard_number": 6, # Approved architecture specifies 6 shards for the 3-node HA cluster
        "replication_factor": 2, # Production requirement
        "write_consistency_factor": 2,
        "on_disk_payload": True,
        # We start with FP32 as requested by constraint 8 (do not enable quantization yet)
    }

    print(f"Creating collection {COLLECTION_NAME} with replication_factor=2...")
    res = requests.put(f"{QDRANT_URL}/collections/{COLLECTION_NAME}", headers=headers, json=payload)
    if res.status_code == 200:
        print(f"Successfully created collection {COLLECTION_NAME}.")
    else:
        print(f"Failed to create collection: {res.text}")
        return

    # 3. Create Payload Indexes (Phase 6 requirement)
    print("Creating payload indexes for organization_id and repository_id...")
    for field in ["organization_id", "repository_id"]:
        index_payload = {
            "field_name": field,
            "field_schema": "keyword"
        }
        idx_res = requests.put(f"{QDRANT_URL}/collections/{COLLECTION_NAME}/index", headers=headers, json=index_payload)
        if idx_res.status_code == 200:
            print(f"Successfully created payload index on {field}.")
        else:
            print(f"Failed to create payload index on {field}: {idx_res.text}")

if __name__ == "__main__":
    init_production_collection()
