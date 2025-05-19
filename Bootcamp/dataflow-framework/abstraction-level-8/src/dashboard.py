from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class Metrics:
    def __init__(self):
        self.processed_files = []

    def update(self, file_name):
        """ Track processed file """
        self.processed_files.append(file_name)

    def get_processed_files(self):
        return self.processed_files

metrics = Metrics()

@app.get("/stats")
def get_stats():
    """ Return the stats of processed files """
    return {
        "total_processed_files": len(metrics.get_processed_files()),
        "last_processed_files": metrics.get_processed_files()[-5:]  # Show last 5 processed files
    }

@app.get("/health")
def health_check():
    """ Check system health """
    return {"status": "healthy"}

@app.get("/files")
def get_files():
    """ Return all processed files """
    return metrics.get_processed_files()

def start_dashboard(metrics):
    """ Run the FastAPI server """
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
