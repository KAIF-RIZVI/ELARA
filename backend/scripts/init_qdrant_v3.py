import requests
import json
import os

QDRANT_URL = "http://localhost:7333"
API_KEY = "elara-production-test-key"

headers = {
    "api-key": API_KEY,
    "Content-Type": "application/json"
}

def create_collection():
    print("Creating collection elara_global_v3...")
    payload = {
        "vectors": {
            "size": 768,
            "distance": "Cosine",
            "on_disk": True
        },
        "shard_number": 3,
        "replication_factor": 2,
        "write_consistency_factor": 2,
        "hnsw_config": {
            "m": 16,
            "ef_construct": 100,
            "full_scan_threshold": 10000,
            "max_elements_post_action": 100000,
            "on_disk": True
        },
        "quantization_config": {
            "scalar": {
                "type": "int8",
                "quantile": 0.99,
                "always_ram": True
            }
        }
    }
    
    response = requests.put(f"{QDRANT_URL}/collections/elara_global_v3", headers=headers, json=payload)
    if response.status_code == 200:
        print("Successfully created collection elara_global_v3.")
    else:
        print(f"Failed to create collection: {response.status_code} - {response.text}")

def create_payload_indexes():
    print("Creating payload indexes for organization_id and repository_id...")
    for field in ["organization_id", "repository_id"]:
        payload = {
            "field_name": field,
            "field_schema": "keyword"
        }
        res = requests.put(f"{QDRANT_URL}/collections/elara_global_v3/index", headers=headers, json=payload)
        if res.status_code == 200:
            print(f"Successfully created index for {field}.")
        else:
            print(f"Failed to create index for {field}: {res.status_code} - {res.text}")

if __name__ == "__main__":
    create_collection()
    create_payload_indexes()
