import time
import os
from qdrant_client import QdrantClient
from qdrant_client.http import models
import random

QDRANT_URL = "http://localhost:7333"
API_KEY = "elara-production-test-key"

def run_benchmarks():
    client = QdrantClient(url=QDRANT_URL, api_key=API_KEY)
    
    vector_size = 768 # ELARA uses GraphCodeBERT
    num_points = 5000
    
    print(f"Benchmarking Qdrant with {num_points} vectors of size {vector_size}")
    
    collections = {
        "benchmark_fp32": models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE
        ),
        "benchmark_int8": models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE
        )
    }

    # Recreate collections
    for name, params in collections.items():
        print(f"Creating collection: {name}")
        
        quantization_config = None
        if "int8" in name:
            quantization_config = models.ScalarQuantization(
                scalar=models.ScalarQuantizationConfig(
                    type=models.ScalarType.INT8,
                    quantile=0.99,
                    always_ram=True
                )
            )

        client.recreate_collection(
            collection_name=name,
            vectors_config=params,
            hnsw_config=models.HnswConfigDiff(on_disk=True),
            optimizers_config=models.OptimizersConfigDiff(default_segment_number=2),
            quantization_config=quantization_config
        )
        
    # Generate points
    print("Generating random vectors...")
    points = []
    for i in range(num_points):
        vec = [random.random() for _ in range(vector_size)]
        points.append(
            models.PointStruct(
                id=i,
                vector=vec,
                payload={"organization_id": "bench-org", "repository_id": "bench-repo"}
            )
        )
        
    # Insert points
    for name in collections.keys():
        print(f"\nInserting points into {name}...")
        start_time = time.time()
        # Insert in batches
        batch_size = 100
        for i in range(0, num_points, batch_size):
            client.upsert(
                collection_name=name,
                points=points[i:i+batch_size],
                wait=True
            )
        duration = time.time() - start_time
        print(f"Insertion took {duration:.2f} seconds")
        
    # Query points
    print("\nBenchmarking queries (100 random queries each)...")
    query_vectors = [[random.random() for _ in range(vector_size)] for _ in range(100)]
    
    for name in collections.keys():
        start_time = time.time()
        for q_vec in query_vectors:
            client.search(
                collection_name=name,
                query_vector=q_vec,
                limit=10,
                query_filter=models.Filter(
                    must=[
                        models.FieldCondition(
                            key="organization_id",
                            match=models.MatchValue(value="bench-org")
                        )
                    ]
                )
            )
        duration = time.time() - start_time
        print(f"Collection {name} - 100 queries took {duration:.2f} seconds ({duration/100:.4f} s/query)")
        
    # Get collection info
    print("\nCollection Stats:")
    for name in collections.keys():
        info = client.get_collection(collection_name=name)
        print(f"--- {name} ---")
        print(f"Points count: {info.points_count}")
        print(f"Vectors count: {info.vectors_count}")
        print(f"Segments count: {info.segments_count}")
        print(f"Status: {info.status}")
        
    # Cleanup
    print("\nCleaning up benchmark collections...")
    for name in collections.keys():
        client.delete_collection(collection_name=name)
        print(f"Deleted {name}")
        
if __name__ == "__main__":
    run_benchmarks()
