from fastapi import FastAPI, Request, HTTPException, Query
import yaml
import requests
from typing import List

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

API_KEY = config["api"]["key"]
NCBI_API_KEY = config["data_source"]["api_key"]
NCBI_BIOC_URL = config["data_source"]["bioc_pmc_url"]

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is working"}

@app.get("/papers")
def get_papers(
    pmcids: List[str] = Query(..., description="List of PMC IDs"),
    request: Request = None
):
    # API key check
    client_key = request.headers.get("X-API-Key")
    if client_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    results = []
    for pmcid in pmcids:
        url = f"{NCBI_BIOC_URL}/{pmcid}?api_key={NCBI_API_KEY}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                results.append({"pmcid": pmcid, "bioc_data": response.text})
            else:
                results.append({
                    "pmcid": pmcid,
                    "error": f"Failed to fetch. Status {response.status_code}",
                    "url": url
                })
        except Exception as e:
            results.append({"pmcid": pmcid, "error": str(e)})

    return results
