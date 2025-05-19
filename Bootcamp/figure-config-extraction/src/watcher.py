import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .ingestion import IngestionPipeline, DataSource
from .storage import Storage
from .config import load_config

class WatcherHandler(FileSystemEventHandler):
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def on_created(self, event):
        if not event.is_directory:
            with open(event.src_path, 'r') as f:
                pmcids = f.read().splitlines()
            summary = self.pipeline.ingest(pmcids)
            print(f"Processed {event.src_path}: {summary}")

def start_watcher(config_path: str):
    config = load_config(config_path)
    pipeline = IngestionPipeline(
        data_source=DataSource(config.data_source.bioc_pmc_url, config.data_source.pubtator3_url),
        storage=Storage(config.storage.path)
    )
    event_handler = WatcherHandler(pipeline)
    observer = Observer()
    observer.schedule(event_handler, config.watched_folder.path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()