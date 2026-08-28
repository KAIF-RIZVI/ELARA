from qdrant_client import QdrantClient
from qdrant_client.models import UpdateAliasOperation, CreateAliasOperation, DeleteAliasOperation
import sys

QDRANT_URL = "http://localhost:7333"
API_KEY = "elara-production-test-key"
ALIAS_NAME = "elara_global"
TARGET_COLLECTION = "elara_global_v3"

def create_alias():
    client = QdrantClient(url=QDRANT_URL, api_key=API_KEY)
    
    print(f"Creating alias {ALIAS_NAME} -> {TARGET_COLLECTION}...")
    try:
        client.update_collection_aliases(
            change_aliases_operations=[
                CreateAliasOperation(
                    create_alias={
                        "collection_name": TARGET_COLLECTION,
                        "alias_name": ALIAS_NAME
                    }
                )
            ]
        )
        print("Alias created successfully.")
    except Exception as e:
        print(f"Error creating alias: {e}")
        # Try to delete alias first if it points to something else
        try:
             client.update_collection_aliases(
                change_aliases_operations=[
                    DeleteAliasOperation(
                        delete_alias={
                            "alias_name": ALIAS_NAME
                        }
                    )
                ]
            )
             client.update_collection_aliases(
                change_aliases_operations=[
                    CreateAliasOperation(
                        create_alias={
                            "collection_name": TARGET_COLLECTION,
                            "alias_name": ALIAS_NAME
                        }
                    )
                ]
            )
             print("Alias recreated successfully.")
        except Exception as e2:
             print(f"Error recreating alias: {e2}")


if __name__ == "__main__":
    create_alias()
