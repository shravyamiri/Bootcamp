### Persistence-drills

````markdown
# SQLite with Python — A Practical Guide

This repository serves as a practical reference for working with SQLite using Python. It covers setup, integration, and best practices for working with relational databases in lightweight applications.

---

## Table of Contents
- [SQLite](#sqlite)
- [Preparation of the System](#preparation-of-the-system)
- [Installation and Testing](#installation-and-testing)
- [Using `sqlite3` with Python](#using-sqlite3-with-python)
- [Advanced Python Usage](#advanced-python-usage)
- [Recommended Reading](#recommended-reading)
- [Database Fundamentals & Self-Assessment](#database-fundamentals--self-assessment)
  - [Transactions and ACID Properties](#transactions-and-acid-properties)
  - [File System vs Database Properties](#file-system-vs-database-properties)
  - [Impact of Missing ACID Components](#impact-of-missing-acid-components)

---

## SQLite

SQLite is a compact, self-contained, high-reliability, and full-featured SQL database engine. It is built into Python and is perfect for applications that need a local database without the overhead of a server.

- Use **SQLite** when your application is the only one accessing the database (e.g., local tools, mobile apps, prototyping).
- Use **PostgreSQL** when multiple applications or distributed access is required.
- For simple key-value data storage, consider **Redis** for its minimal interface and high performance.

---

## Preparation of the System

1. Ensure you have Python 3.7 or later installed.
2. SQLite is bundled with Python, so no separate installation is needed.
3. Optionally, set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
````

---

## Installation and Testing

Run the following Python snippet to verify SQLite setup:

```python
import sqlite3
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("SELECT sqlite_version();")
print(cursor.fetchone())
```

You should see the installed SQLite version.

---

## Using `sqlite3` with Python

Example: Creating a database and table, inserting and retrieving data.

```python
import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

# Insert a record
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))

# Query the table
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.commit()
conn.close()
```

---

## Advanced Python Usage

* Use **parameterized queries** to avoid SQL injection.
* Set `row_factory` to `sqlite3.Row` for dict-like access.
* Wrap DB connections in context managers for better resource handling.
* For larger applications, consider using an ORM like **SQLAlchemy** or **Peewee**.

---



---

## Database Fundamentals & Self-Assessment

### Transactions and ACID Properties

#### What are Transactions?

A **transaction** is a sequence of one or more SQL operations executed as a single logical unit of work. Either all operations in a transaction are committed (applied permanently), or none are (rolled back).

#### Why are Transactions Critical?

They ensure:

* Data **integrity**: Prevents half-finished changes from corrupting data.
* **Error recovery**: If an error occurs, the database can return to a consistent state.
* **Concurrency safety**: Isolates operations from others in multi-user environments.

---

### What Are the ACID Properties?

| Property            | Description                                                                         |
| ------------------- | ----------------------------------------------------------------------------------- |
| **A - Atomicity**   | Ensures all parts of a transaction are completed successfully, or none are.         |
| **C - Consistency** | Guarantees the database remains in a valid state before and after the transaction.  |
| **I - Isolation**   | Ensures concurrent transactions do not interfere with each other.                   |
| **D - Durability**  | Once a transaction is committed, its effects are permanent—even in case of a crash. |

---

### Suppose Transactions Aren’t Supported — Is the System Still Useful?

A system without transactions **might be usable** in simple, non-critical scenarios. However, it risks:

* **Partial writes**, leading to data corruption
* **Inconsistent states**, especially in concurrent access
* **Poor reliability**, with no rollback or recovery on failure

**Use case where it might be acceptable:** Logging systems where losing or duplicating entries is tolerable.

---

### File System vs Database Properties

Modern file systems offer some guarantees (e.g., journaling for durability), but **do not ensure full ACID compliance**:

* **Atomicity**: File writes are often not atomic.
* **Consistency**: Left to application logic.
* **Isolation**: Not enforced unless explicitly managed via locks.
* **Durability**: Depends on disk hardware and OS caching.

Thus, databases are more suitable for structured, reliable, and concurrent data operations.

---

## Impact of Missing ACID Components

### If Atomicity is Missing

* **Risk**: Partial transactions may leave data in an unusable state.
* **Acceptable Scenario**: Append-only logs or telemetry where exactness isn’t critical.

### If Consistency is Missing

* **Risk**: Violated constraints (e.g., foreign keys, business rules).
* **Acceptable Scenario**: During temporary states in ETL pipelines or caching layers where consistency is eventually achieved.

### If Isolation is Missing

* **Risk**: Race conditions, dirty reads, phantom reads.
* **Acceptable Scenario**: Analytics workloads where precise consistency isn’t required immediately.

### If Durability is Missing

* **Risk**: Data loss on crashes or power failure.
* **Acceptable Scenario**: Caching systems or ephemeral data (e.g., session tokens).

---

## License

This project is licensed under the MIT License.

---



## Author

Maintained by Shravya Miriyanam

```

---
