import requests
import json

def fetch_qdrant_info():
    base_url = "http://localhost:6333"
    results = {}

    try:
        results["root"] = requests.get(base_url).json()
    except Exception as e:
        results["root"] = str(e)

    try:
        results["cluster"] = requests.get(f"{base_url}/cluster").json()
    except Exception as e:
        results["cluster"] = str(e)

    try:
        results["elara_global_v2"] = requests.get(f"{base_url}/collections/elara_global_v2").json()
    except Exception as e:
        results["elara_global_v2"] = str(e)

    try:
        results["aliases"] = requests.get(f"{base_url}/aliases").json()
    except Exception as e:
        results["aliases"] = str(e)
        
    try:
        results["collections"] = requests.get(f"{base_url}/collections").json()
    except Exception as e:
        results["collections"] = str(e)
        
    try:
        results["telemetry"] = requests.get(f"{base_url}/telemetry?anonymize=false").json()
    except Exception as e:
        results["telemetry"] = str(e)

    with open("qdrant_dump.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    fetch_qdrant_info()
