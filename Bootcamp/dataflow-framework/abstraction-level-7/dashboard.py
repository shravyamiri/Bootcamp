import threading
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
import time

# Create FastAPI app
app = FastAPI()

# Example shared metrics dictionary
metrics_data = {}

# Shared memory to hold traces
trace_data = []

class Metrics(BaseModel):
    processor_name: str
    count: int
    time: float
    errors: int

@app.get("/stats")
def get_stats():
    return metrics_data

@app.get("/trace")
def get_trace():
    return trace_data

@app.get("/errors")
def get_errors():
    return {"errors": ["No errors so far"]}  # You can track errors if you want

def start_dashboard(metrics):
    def update_metrics():
        # Here, you would update your metrics based on your processing
        while True:
            time.sleep(5)  # Update every 5 seconds
            # You can modify this to update metrics dynamically as your system processes data
            metrics_data['example_processor'] = {
                'count': 100,
                'time': 1.5,
                'errors': 0
            }

    # Start FastAPI server in a separate thread
    def run():
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)

    # Start the background thread for FastAPI
    thread = threading.Thread(target=run)
    thread.start()

    # Start the metrics updater in another background thread
    metrics_thread = threading.Thread(target=update_metrics)
    metrics_thread.start()

    print("Dashboard started on http://127.0.0.1:8000")
