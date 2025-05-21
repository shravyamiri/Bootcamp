import yaml
from pydantic import BaseModel
from typing import Optional

class DataSourceConfig(BaseModel):
    type: str
    bioc_pmc_url: str
    pubtator3_url: str
    api_key: str

class StorageConfig(BaseModel):
    type: str
    path: str
    csv_path: str

class ApiConfig(BaseModel):
    key: str
    host: str
    port: int

class LoggingConfig(BaseModel):
    level: str

class WatchedFolderConfig(BaseModel):
    path: str

class Config(BaseModel):
    data_source: DataSourceConfig
    storage: StorageConfig
    api: ApiConfig
    logging: LoggingConfig
    watched_folder: WatchedFolderConfig

def load_config(path: str) -> Config:
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    return Config(**data)