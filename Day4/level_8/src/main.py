import os
import time
import shutil
import yaml
import sys
from fastapi import FastAPI
from threading import Thread
from engine import RoutingEngine
from metrics import Metrics
from dashboard import start_dashboard

WATCH_DIR = "watch_dir"
UNPROCESSED_DIR = os.path.join(WATCH_DIR, "unprocessed")
UNDERPROCESS_DIR = os.path.join(WATCH_DIR, "underprocess")
PROCESSED_DIR = os.path.join(WATCH_DIR, "processed")

# Create directories if they don't exist
os.makedirs(UNPROCESSED_DIR, exist_ok=True)
os.makedirs(UNDERPROCESS_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)


def load_config():
    """ Load configuration from config.yaml in the same folder as this script """
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    if not os.path.exists(config_path):
        print(f"Error: {config_path} not found!")
        sys.exit(1)
    with open(config_path) as f:
        return yaml.safe_load(f)



def move_file(src, dest):
    """ Move file atomically """
    shutil.move(src, dest)


def process_file(file_path, engine, metrics):
    """ Process the file using RoutingEngine """
    print(f"Processing {file_path}...")
    with open(file_path, "r") as file:
        lines = file.readlines()
    engine.run(lines)
    move_file(file_path, PROCESSED_DIR)
    metrics.update(file_path)  # Track the file processing


def monitor_unprocessed(engine, metrics):
    """ Continuously monitor the unprocessed folder """
    while True:
        for filename in os.listdir(UNPROCESSED_DIR):
            src_path = os.path.join(UNPROCESSED_DIR, filename)
            dest_path = os.path.join(UNDERPROCESS_DIR, filename)
            move_file(src_path, dest_path)
            process_file(dest_path, engine, metrics)  # Use new path here
        time.sleep(1)



def run_dashboard(metrics):
    """ Start FastAPI dashboard """
    start_dashboard(metrics)


def start_monitoring():
    """ Main loop for monitoring and processing """
    config = load_config()
    metrics = Metrics()
    engine = RoutingEngine(config, metrics, enable_trace="--trace" in sys.argv)

    # Start the dashboard in a separate thread
    dashboard_thread = Thread(target=run_dashboard, args=(metrics,))
    dashboard_thread.daemon = True
    dashboard_thread.start()

    # Start monitoring files
    monitor_unprocessed(engine, metrics)


if __name__ == "__main__":
    start_monitoring()
