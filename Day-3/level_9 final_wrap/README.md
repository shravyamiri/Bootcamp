# Real-Time File Processing System

This project is a dynamic, fault-tolerant, self-managing file processing system built using Python and FastAPI. It can process files in two modes: single file mode or watch mode. It also includes a REST API for system monitoring and file upload.

---

## Features

- Supports both one-shot and continuous file processing
- Exposes FastAPI endpoints for monitoring and file interaction
- Docker support for easy containerized deployment
- Makefile to simplify build and run tasks
- Compatible with file drop, API upload, or CLI usage

---

## Requirements

- Python 3.8 or higher
- pip (Python package manager)
- Docker (optional, for containerized run)

Install Python dependencies:

```bash
pip install -r requirements.txt
Running the System
1. Local Execution
Single File Mode
Processes one file and exits.


python main.py --input path/to/file.txt
Watch Mode
Continuously monitors the watch_dir/unprocessed/ folder and processes files as they appear.

python main.py --watch
2. Docker Execution
Build the Docker image:
make build-docker

Run the container:

make run-docker
FastAPI Endpoints
Method	Endpoint	Description
GET	/health	Check system health
GET	/stats	View processing statistics
GET	/files	List processed files
POST	/upload	Upload a file for processing

Interactive API documentation is available at:
http://localhost:8000/docs

File Upload Methods
Files can be added for processing in several ways:

CLI: Place files in the watch_dir/unprocessed/ directory

API: Use the /upload endpoint to send files via HTTP

Command Line Tool:

curl -F 'file=@sample.txt' http://localhost:8000/upload

Monitoring Uptime
You can use a free uptime monitoring service like Better Uptime to track system availability:

Create a monitor for the /health endpoint

Configure alerts (email, Slack, etc.)

Track downtime and receive incident reports

Makefile Commands
The project includes a Makefile to simplify common tasks:

Command	Description
make build-docker	Build the Docker image
make run-docker	Run the Docker container
make clean	Remove build artifacts
make build-package	Build the Python package (if applicable)
make publish-package	Publish the package to PyPI (optional)

Project Structure

.
├── main.py              
├── processor.py         
├── api/server.py        
├── watch_dir/unprocessed/  
├── Makefile             
├── Dockerfile           
├── requirements.txt     
└── README.md            

License
This project is for educational and internal use. For external redistribution, please refer to the licensing terms specified (if any).


