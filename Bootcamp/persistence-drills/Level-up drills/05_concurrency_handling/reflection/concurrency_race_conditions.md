Concurrency and Race Condition Management Reflection
How did you break the system in step 1?
The naive transfer in naive_transfer.py breaks the system by:

Race Conditions: Without transactions, concurrent transfers read and write balances independently. For example, two transfers of $100 from Account 1 (balance $1000) may both read the initial balance, each subtract $100, and commit, resulting in a final balance of $900 instead of $800, effectively losing $100.
Data Inconsistency: The lack of atomicity allows interleaved reads and writes, violating the invariant that total balance (Account 1 + Account 2) remains constant.
No Locking: Without SELECT FOR UPDATE, concurrent sessions overwrite each other’s updates, leading to incorrect balances, as demonstrated in transfer_money.py.

Why is locking tricky in high-concurrency environments?
Locking, as used in safe_transfer.py, is challenging because:

Deadlocks: If transactions lock rows in different orders (e.g., Account 1 then 2 vs. 2 then 1), they can deadlock. The solution sorts account IDs to ensure consistent locking order.
Performance Bottlenecks: SELECT FOR UPDATE blocks other transactions accessing the same rows, reducing throughput in high-concurrency systems (e.g., banking apps).
Scalability Limits: Locks increase contention, especially for hot rows (e.g., popular accounts), slowing down the system.
Database Differences: SQLite lacks SELECT FOR UPDATE, relying on serialized transactions, which may not scale as well as PostgreSQL’s row-level locking.
Timeout Risks: Long-running transactions holding locks can timeout, causing failures, requiring retry logic or shorter transactions.
Alternatives: Optimistic locking or queue-based systems may reduce locking needs but introduce complexity, as seen in Challenge 3’s upserts.

The safe transfer uses SELECT FOR UPDATE (PostgreSQL) and transactions (SQLite) to ensure atomicity, with Pydantic schemas for API consistency.
