from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from typing import List
import csv
import io
from .ingestion import IngestionPipeline, DataSource
from .storage import Storage
from .config import Config, load_config

app = FastAPI()
api_key_header = APIKeyHeader(name="X-API-Key")

class IngestRequest(BaseModel):
    pmcids: List[str]

def verify_api_key(api_key: str = Depends(api_key_header), config: Config = Depends(lambda: load_config('config.yaml'))):
    if api_key != config.api.key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key

@app.post("/ingest")
async def ingest_papers(request: IngestRequest, api_key: str = Depends(verify_api_key), config: Config = Depends(lambda: load_config('config.yaml'))):
    pipeline = IngestionPipeline(
        data_source=DataSource(config.data_source.bioc_pmc_url, config.data_source.pubtator3_url, config.data_source.api_key),
        storage=Storage(config.storage.path, config.storage.csv_path)
    )
    summary = pipeline.ingest(request.pmcids)
    return summary

@app.get("/papers")
async def get_papers(pmcids: List[str] = None, format: str = "json", api_key: str = Depends(verify_api_key), config: Config = Depends(lambda: load_config('config.yaml'))):
    storage = Storage(config.storage.path, config.storage.csv_path)
    papers = storage.query_papers(pmcids)
    if format == "csv":
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=['pmcid', 'pmid', 'title', 'abstract', 'captions'])
        writer.writeheader()
        writer.writerows(papers)
        return output.getvalue()
    return papers

@app.post("/upload")
async def upload_file(file: UploadFile = File(...), api_key: str = Depends(verify_api_key), config: Config = Depends(lambda: load_config('config.yaml'))):
    content = await file.read()
    pmcids = content.decode().splitlines()
    pipeline = IngestionPipeline(
        data_source=DataSource(config.data_source.bioc_pmc_url, config.data_source.pubtator3_url, config.data_source.api_key),
        storage=Storage(config.storage.path, config.storage.csv_path)
    )
    summary = pipeline.ingest(pmcids)
    return summary