import os
import sys

# Ensure backend directory is in path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from qdrant_client import QdrantClient
from app.core.config import get_settings

def migrate():
    print("============================================================")
    print("    ELARA QDRANT MIGRATION SCRIPT - PRODUCTION MODE")
    print("============================================================")
    
    settings = get_settings()
    client = QdrantClient(url=settings.QDRANT_URL)
    
    collections = client.get_collections().collections
    collection_names = [c.name for c in collections]
    
    print(f"Detected active Qdrant collections: {collection_names}")
    
    if "elara_global_v1" not in collection_names:
        print("✅ SUCCESS: 'elara_global_v1' does not exist in Qdrant. No migration required.")
        return
        
    print("\n⚠️  WARNING: Legacy collection 'elara_global_v1' detected (384-dimensional).")
    print("This collection is incompatible with the true GraphCodeBERT 768-D architecture.")
    print("\n--- SAFETY CHECKS ---")
    print("Before proceeding, the system MUST confirm there are no active consumers of v1.")
    
    # Simple explicit confirmation for production safety
    print("Have you verified that NO active code references 'elara_global_v1'?")
    confirm1 = input("Type 'YES' to confirm: ")
    if confirm1 != "YES":
        print("Migration aborted.")
        return
        
    print("Are you absolutely sure you want to permanently delete 'elara_global_v1'?")
    print("This will destroy all legacy vectors.")
    confirm2 = input("Type 'DESTROY' to proceed: ")
    if confirm2 != "DESTROY":
        print("Migration aborted.")
        return
        
    print("\nDeleting collection 'elara_global_v1'...")
    try:
        client.delete_collection("elara_global_v1")
        print("✅ SUCCESS: Collection 'elara_global_v1' permanently deleted.")
    except Exception as e:
        print(f"❌ ERROR: Failed to delete collection: {e}")
        
    if "elara_global_v2" not in collection_names:
        print("\nCreating 'elara_global_v2' (768-dimensional)...")
        from qdrant_client.http.models import Distance, VectorParams
        try:
            client.create_collection(
                collection_name="elara_global_v2",
                vectors_config=VectorParams(size=768, distance=Distance.COSINE),
            )
            
            client.create_payload_index(
                collection_name="elara_global_v2",
                field_name="organization_id",
                field_schema="uuid"
            )
            print("✅ SUCCESS: Collection 'elara_global_v2' created.")
        except Exception as e:
            print(f"❌ ERROR: Failed to create v2 collection: {e}")
    else:
        print("\n✅ SUCCESS: Collection 'elara_global_v2' is already active.")
        
if __name__ == "__main__":
    migrate()
