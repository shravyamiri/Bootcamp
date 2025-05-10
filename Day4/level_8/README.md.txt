Automated File Processing System with Folder Monitoring and Recovery
This project provides a self-running, fault-tolerant file processing system that continuously monitors a folder for new files, processes them using a streaming/tag-routing engine, and recovers from failures automatically. The system simulates a real-world ingestion service or ETL daemon, ensuring robustness, safety, and visibility.

Project Overview
The system monitors a directory for incoming files, processes them in real-time, and ensures that files are handled even in the event of system crashes or restarts. It moves files through various stages (unprocessed/, underprocess/, processed/), ensuring that only successfully processed files reach the processed/ folder.

Key Features:
Continuous File Monitoring: Automatically watches the unprocessed/ folder for new files.

Fault Tolerance: Automatically recovers and retries any files that were in progress during a crash.

Live Dashboard: A web dashboard that shows real-time file processing status, including the number of files in each folder, the file currently being processed, and the last few processed files.

Non-blocking Processing: The main process runs continuously and does not block, ensuring smooth operation.

Idempotency: If a file is reprocessed, it will not cause issues due to idempotency, which guarantees that the file can be safely processed multiple times.

Folder Queue Design
The directory structure is as follows:

bash
Copy
Edit
watch_dir/
├── unprocessed/     # Incoming files to watch
├── underprocess/    # Files being processed
├── processed/       # Successfully processed files
unprocessed/: Files land here initially.

underprocess/: Files are moved here while being processed.

processed/: Once a file is successfully processed, it moves to this folder.

File Lifecycle:
Incoming Files: Files arrive in unprocessed/.

Processing: Files are moved to underprocess/ while being worked on.

Success: Once processing completes, files are moved to processed/.

Crash Recovery: If the system crashes, all files in underprocess/ are moved back to unprocessed/ on the next startup to resume processing.

File Handling:
Atomic Moves: Files are moved atomically using shutil.move() to ensure safe handling.

Resilient Processing: Files will be retried automatically if the system crashes or is restarted.

Live State Updates: The web dashboard continuously reflects the state of the files.

Setup and Installation
Requirements
Python 3.7+

Required Python packages: Install using the following command:

bash
Copy
Edit
pip install -r requirements.txt
Environment Variables
Create a .env file for environment-specific variables, such as:

ini
Copy
Edit
MODE=uppercase
Running the System
Start the File Monitoring System: This command starts the background process that continuously monitors the unprocessed/ folder and processes files as they appear.

bash
Copy
Edit
python main.py
Web Dashboard: After starting the monitoring system, the web dashboard will start automatically and provide real-time updates on the file processing progress.

Processing with CLI Arguments:

Specify input and output file paths and choose processing modes:

bash
Copy
Edit
python process.py --input input.txt --output output.txt --mode uppercase
Folder Structure
unprocessed/: Incoming files that need processing.

underprocess/: Files currently being processed.

processed/: Files that have been successfully processed.

System Behavior
Continuous Monitoring: The system continuously checks the unprocessed/ folder for new files. When new files appear, they are moved to underprocess/ and processed line-by-line.

Fault Recovery: If the system crashes, on the next startup, the files that were in underprocess/ are moved back to unprocessed/ for reprocessing.

Live Dashboard Updates: The web dashboard updates in real-time to show:

The number of files in unprocessed/, underprocess/, and processed/.

The name of the file currently being processed.

The last N processed files with their timestamps.

Design Considerations
Concurrency and Parallelism: Consider how to handle multiple instances of the system running concurrently. You can parallelize file processing across threads or nodes using a task queue (e.g., Celery or RQ) for improved scalability.

Partial Files: In case a file is partially written when picked up, ensure the system can either handle such files safely or ignore them until fully written. You may need to implement checks like file size or file-locking mechanisms to handle this situation effectively.

Reflection and Future Improvements
Parallel Processing: To scale the system for processing large volumes of files, you can introduce parallelism by splitting file processing across multiple threads or even distributed nodes.

Handling Partial Files: You need to ensure that the system doesn’t process files that are being written. This could involve checking file modification times or locking mechanisms to ensure that a file is fully written before processing it.

Improved Recovery: Add logging and status tracking to make recovery more granular (e.g., tracking where the system left off in a file).

License
This project is licensed under the MIT License - see the LICENSE file for details.