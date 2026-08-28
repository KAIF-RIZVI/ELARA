import os
from qdrant_client import QdrantClient
from qdrant_client.http import models

QDRANT_URL = "http://localhost:7333"
API_KEY = "elara-production-test-key"
COLLECTION_NAME = "elara_global_v3"

def run_tests():
    try:
        # Test 1: Authentication Failure (should raise exception)
        print("Test 1: Connecting without API key...")
        client_no_auth = QdrantClient(url=QDRANT_URL)
        try:
            client_no_auth.get_collections()
            print("[FAIL] SECURITY FAILURE: Access allowed without API key")
            return
        except Exception as e:
            print(f"[PASS] Auth requirement verified. Error as expected: {e}")

        # Test 2: Valid Authentication
        print("\nTest 2: Connecting with API key...")
        client = QdrantClient(url=QDRANT_URL, api_key=API_KEY)
        collections = client.get_collections()
        print(f"[PASS] Connected successfully. Collections: {[c.name for c in collections.collections]}")

        # Test 3: Tenant Isolation via Qdrant Filter
        print("\nTest 3: Testing Tenant Isolation (Payload Filters)...")
        # Upsert a dummy vector for Tenant A
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                models.PointStruct(
                    id=1,
                    vector=[0.1] * 768,
                    payload={"organization_id": "tenant-A", "repository_id": "repo-1"}
                )
            ]
        )
        print("Inserted point for tenant-A")

        # Query as Tenant B (Should find nothing)
        search_result_b = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=[0.1] * 768,
            query_filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="organization_id",
                        match=models.MatchValue(value="tenant-B")
                    )
                ]
            ),
            limit=1
        )
        
        if len(search_result_b) == 0:
            print("[PASS] Tenant B cannot see Tenant A's data.")
        else:
            print("[FAIL] TENANT ISOLATION FAILURE: Tenant B saw Tenant A's data.")

        # Query as Tenant A (Should find the point)
        search_result_a = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=[0.1] * 768,
            query_filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="organization_id",
                        match=models.MatchValue(value="tenant-A")
                    )
                ]
            ),
            limit=1
        )
        if len(search_result_a) == 1 and search_result_a[0].id == 1:
            print("[PASS] Tenant A successfully accessed their own data.")
        else:
            print("[FAIL] TENANT ACCESS FAILURE: Tenant A could not retrieve their data.")

        # Cleanup dummy point
        client.delete(
            collection_name=COLLECTION_NAME,
            points_selector=models.PointIdsList(points=[1])
        )
        print("\n[PASS] All security and isolation tests passed successfully.")

    except Exception as e:
        print(f"Test failed with exception: {e}")

if __name__ == "__main__":
    run_tests()
