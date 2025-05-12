

# Automated File Processing System – Folder Monitor and Recovery

This project transforms your file processing logic into a self-managing, resilient, and continuously running system. It monitors incoming files, processes them safely, and recovers gracefully from failures or crashes.

---

## Project Highlights

* Automatically monitors a folder for new incoming files
* Processes files line-by-line using a streaming/tag-routing engine
* Moves files through three lifecycle states: `unprocessed/`, `underprocess/`, and `processed/`
* Automatically recovers from crashes by resuming uncompleted work
* Exposes a live web dashboard for monitoring file status and progress

---

## Folder Queue Structure

The `watch_dir/` folder acts as a file-based queue with state management:

```
watch_dir/
├── unprocessed/     
├── underprocess/     
├── processed/       
```

### File Lifecycle

* Files arrive in `unprocessed/`
* The system picks up and moves them to `underprocess/`
* After processing, files are moved to `processed/`
* If the system crashes, on the next startup:

  * All files in `underprocess/` are returned to `unprocessed/` for retry
  * Idempotent processing ensures safety during retries

---

## Running the System

### 1. Watch Mode (Continuous Monitoring)

```bash
python main.py --watch
```

* The system monitors `watch_dir/unprocessed/` continuously
* Automatically starts the web dashboard alongside the monitoring loop

### 2. Single File Mode 

```bash
python main.py --input path/to/file.txt
```

* For manual one-shot processing and debugging

---

## Features

* **Background Monitoring**: Uses threads or async loops to watch for new files
* **Atomic File Movement**: Uses `shutil.move()` to safely transition files
* **Recovery Mechanism**: Re-initializes `underprocess/` files to `unprocessed/` on restart
* **Live Web Dashboard**:

  * Displays number of files in each folder
  * Shows the name of the file currently being processed
  * Logs the last N processed files with timestamps

---

## Deployment

### Using Docker

```bash
docker build -t file-monitor .
docker run -v $(pwd)/watch_dir:/app/watch_dir file-monitor --watch
```

### Locally

```bash
python main.py --watch
```

---

## API Endpoints (FastAPI)

* `GET /health` – Check system health
* `GET /stats` – Get file counts per folder
* `GET /files` – View recently processed files and current status
* Optional: `POST /upload` – Upload files via API (if implemented)

---

## Monitoring and Observability

* Compatible with external monitoring tools like Better Uptime or UptimeRobot
* Use `GET /health` endpoint for automated monitoring alerts
* Real-time file system status and file history viewable via web dashboard

---

## Key Design Considerations

* System runs continuously and autonomously
* Logs processing activity (optional logging system can be integrated)
* Recoverable and fault-tolerant architecture
* Modular and scalable folder queue design

---

## Reflection & Scalability Notes

* **Single Instance Limitation**: Two instances may try to process the same file. Consider adding file locks or a distributed queue (e.g., Redis) if scaling across nodes.
* **Parallel Processing**:

  * Threaded or multi-process file processing possible
  * Ensure atomic file handling to prevent race conditions
* **Partial File Safety**:

  * Avoid processing partially uploaded files by checking file size consistency or using temporary upload names

---


