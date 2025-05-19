Setup Guide for Figure Caption Extraction and Access System
This guide provides step-by-step instructions to set up the environment for the Figure Caption Extraction and Access System, a FastAPI-based application that extracts figure captions and entities from PMC papers using a DuckDB database and external APIs (BioC-PMC/PubTator3). The project runs in a Docker container and is managed via PowerShell commands on Windows.

Prerequisites
Software Requirements
Docker Desktop: Required to build and run the project container. Compatible with Windows 10/11 Pro, Enterprise, Education, or Windows 11 Home with WSL 2.
PowerShell: Windows PowerShell (built-in) or PowerShell 7 (recommended) for executing commands.
Internet Connection: Needed for pulling Docker images and accessing external APIs.
Hardware Requirements
Operating System: Windows 10/11 (64-bit).
RAM: Minimum 4GB (8GB recommended).
Disk Space: Approximately 2GB for Docker images and project files.
CPU: Modern CPU with virtualization support (for WSL 2).
Project Directory
The project requires a specific directory structure in C:\Users\Shravya Miriyanam\OneDrive\Desktop\figure-config. Ensure the following files and folders are present:

src/ (with subdirectories api/, ingestion/, cli/, utils/, and Python files like main.py, endpoints.py, etc.).
data/ (with input/ subdirectory).
config.yaml, Dockerfile, requirements.txt, README.md, runbook.md, .gitignore.
Setup Instructions
1. Install Docker Desktop
Download Docker Desktop:
Visit the official Docker website and download Docker Desktop for Windows.
Install Docker Desktop:
Run the installer with administrative privileges.
During installation, enable WSL 2 if prompted (required for Windows Home or WSL 2 backend).
Enable WSL 2 (if not already enabled):
Open PowerShell as Administrator.
Run commands to enable WSL and the Virtual Machine Platform feature.
Restart your computer if prompted.
Start Docker Desktop:
Launch Docker Desktop from the Start menu.
Ensure it’s running (check the system tray icon).
Verify Installation:
In PowerShell, run a command to check the Docker version.
Expected output: A version number like Docker version 24.x.x.
2. Set Up the Project Directory
Navigate to Project Directory:
Open PowerShell.
Change to the project directory: C:\Users\Shravya Miriyanam\OneDrive\Desktop\figure-config.
Verify Directory Structure:
Ensure all required folders (src/, data/, etc.) and files (config.yaml, Dockerfile, etc.) exist.
If missing, create the directory structure with src/, src/api/, src/ingestion/, src/cli/, src/utils/, data/, and data/input/.
Configure config.yaml:
Ensure config.yaml contains:
Database path: data/data.db.
API key: beafaa69c8ca82900b029902b54c78e8a108.
Data source: PMC.
Logging level: debug.
Verify requirements.txt:
Ensure it lists dependencies: fastapi, uvicorn, aiohttp, duckdb, pyyaml, watchdog, pandas, pytest, responses with specific versions.
Create .gitignore:
Ensure it ignores __pycache__/, *.pyc, data/data.db, and data/*.bak.
3. Build the Docker Image
Build the Image:
In PowerShell, from the project directory, run the Docker build command to create the caption-extractor image.
This uses the Dockerfile to install dependencies and copy project files.
Verify Image:
Run a Docker command to list images.
Ensure caption-extractor appears.
4. Run the Docker Container
Start the Container:
Run a Docker command to start the container in detached mode, mapping port 8001 on the host to 8000 in the container, and mounting the data/ directory.
Name the container caption-extractor-container.
Verify Container:
Run a Docker command to list running containers.
Ensure caption-extractor-container is listed with ports 0.0.0.0:8001->8000/tcp.
Check Logs:
Run a Docker command to view container logs.
Expected output: Messages indicating the FastAPI server started, e.g., Uvicorn running on http://0.0.0.0:8000.
5. Test the Server
Test Connectivity:
In PowerShell, send a GET request to http://localhost:8001.
Expected response: {"status":"FastAPI running!"}.
Troubleshoot Issues:
If the connection fails, check container status and logs.
Ensure port 8001 is not used by other processes.
Allow port 8001 in the Windows Firewall if needed.
6. Ingest Paper Data
Send Ingestion Request:
Run a PowerShell Invoke-WebRequest command to send a POST request to http://localhost:8001/extract.
Include headers for the API key and JSON content type.
Provide a body with paper IDs ["PMC7441787", "PMC7146658"].
Use error handling to catch issues.
Expected Output:
A JSON response with details for each paper, including title, abstract, captions, and entities (e.g., genes like BRCA1, TP53).
Check Logs:
View container logs to confirm ingestion (e.g., Ingestion completed: 2 papers processed, 0 failures).
7. Query Paper Data
Send Query Request:
Run a PowerShell Invoke-WebRequest command to send a GET request to http://localhost:8001/query/PMC7441787?format=json.
Include the API key header.
Use error handling.
Expected Output:
A JSON response with caption and entity details for PMC7441787.
8. Clean Up
Stop and Remove Container:
Run Docker commands to stop and remove caption-extractor-container.
Remove Database:
Delete data/data.db to clear the database.
Remove Cache:
Delete __pycache__ directories in src/ and subdirectories.
Troubleshooting Common Issues
Docker Not Running:
Ensure Docker Desktop is running (system tray).
Restart Docker Desktop or your computer.
Database Lock Errors:
Delete data/data.db and ensure data/ has full permissions (Everyone:F).
Connection Errors:
Check container status and port 8001 availability.
Allow port 8001 in the firewall.
500 Internal Server Error:
Check container logs for database, API, or code issues.
Delete data/data.db or rebuild the image.
API Connectivity:
Ensure internet access and test connectivity to api.ncbi.nlm.nih.gov:443.
Additional Notes
Run PowerShell as Administrator for commands requiring elevated permissions (e.g., firewall changes).
If files are missing, ensure the project directory matches the required structure.
For CLI usage outside Docker, install Python 3.11 and dependencies from requirements.txt.