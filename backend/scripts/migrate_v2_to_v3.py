import time
from qdrant_client import QdrantClient

QDRANT_URL = "http://localhost:7333"
API_KEY = "elara-production-test-key"

SOURCE_COLLECTION = "elara_global_v2"
DEST_COLLECTION = "elara_global_v3"
BATCH_SIZE = 100

def migrate():
    client = QdrantClient(url=QDRANT_URL, api_key=API_KEY)
    
    # 1. Create a snapshot of v2
    print(f"Creating snapshot of {SOURCE_COLLECTION}...")
    snapshot = client.create_snapshot(collection_name=SOURCE_COLLECTION)
    print(f"Snapshot created: {snapshot.name}")
    
    # 2. Check if v3 exists
    collections = [c.name for c in client.get_collections().collections]
    if DEST_COLLECTION not in collections:
        print(f"Error: Destination collection {DEST_COLLECTION} does not exist.")
        return
        
    print(f"Migrating from {SOURCE_COLLECTION} to {DEST_COLLECTION}...")
    
    offset = None
    total_migrated = 0
    
    start_time = time.time()
    while True:
        # Scroll source collection
        records, next_offset = client.scroll(
            collection_name=SOURCE_COLLECTION,
            limit=BATCH_SIZE,
            offset=offset,
            with_payload=True,
            with_vectors=True
        )
        
        if not records:
            break
            
        # Insert to destination
        client.upsert(
            collection_name=DEST_COLLECTION,
            points=records,
            wait=True
        )
        
        total_migrated += len(records)
        print(f"Migrated {total_migrated} points...")
        
        if next_offset is None:
            break
        offset = next_offset
        
    duration = time.time() - start_time
    print(f"Migration completed! Migrated {total_migrated} points in {duration:.2f} seconds.")

if __name__ == "__main__":
    migrate()
