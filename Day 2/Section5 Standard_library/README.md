Standard Library Mastery
This repository is a hands-on guide to mastering the most powerful modules in Python’s Standard Library. It covers real-world use cases, examples, and best practices for five essential areas:

📚 Section 1: collections
Master high-performance data structures from the collections module:

defaultdict for Grouping – Group words by their first letter.

Counter Basics – Count frequencies of characters in a string.

Most Common Elements – Find the top 2 most frequent elements in a list.

deque as Stack & Queue – Use appendleft() and pop() for queue/stack behavior.

Rotate a deque – Efficiently rotate elements in a deque.

OrderedDict Iteration – Iterate while preserving insertion order.

defaultdict with lambda – Handle missing keys with default values.

Nested defaultdict – Create hierarchical data structures.

🗂 Section 2: Filesystem & Path Handling
Work with files and directories using pathlib, os, shutil, and tempfile:

Read/Write Files – Use Path.read_text() and open(..., "w").

List Files – Use Path.glob() to list Python files.

Create/Delete Directories – Safely use os.makedirs() and shutil.rmtree().

Temporary Files – Create and write to temp files using tempfile.

Copy Files – Use shutil.copy() to copy file contents.

Path Resolution – Get absolute paths using Path.resolve().

Check File Existence – Use .exists() and .is_file().

🕒 Section 3: Date and Time
Perform date and time manipulation with datetime and calendar:

Current Time – Get system time using datetime.now().

Date Arithmetic – Add days using timedelta.

Format/Parse Dates – Convert to/from string with strftime()/strptime().

Get Weekday Name – Use calendar.day_name.

Compare Dates – Determine which date comes first.

Generate Calendar – Print a month calendar.

Round to Nearest Hour – Clean up timestamps.

🧾 Section 4: Serialization – json, csv, pickle
Learn how to serialize and deserialize data:

JSON Load/Dump – Convert between Python objects and JSON strings.

Pretty Print JSON – Improve readability with indentation.

CSV Read/Write – Use csv.DictReader and csv.DictWriter.

Pickling Objects – Save/load objects with pickle.

Security Note on Pickle – Understand risks; prefer JSON when possible.

Custom JSON Encoder – Serialize complex types like datetime.

Read CSV as NamedTuples – Improve data structure readability.

⚙️ Section 5: Subprocess & Concurrency
Run external commands and implement parallelism:

Run Shell Commands – Use subprocess.run() with arguments.

Capture Output – Use capture_output=True to store stdout/stderr.

Check Exit Codes – Handle failures via .returncode.

Start Threads & Processes – Use threading.Thread and multiprocessing.Process.

Thread Locking – Protect shared data with threading.Lock.

ThreadPoolExecutor – Parallelize function execution with concurrent.futures.

Kill Subprocess – Start and terminate subprocesses safely.

✅ Prerequisites
Python 3.8+

Basic knowledge of Python syntax

IDE or code editor  PyCharm

📌 License
This project is open-source and available under the MIT License.
