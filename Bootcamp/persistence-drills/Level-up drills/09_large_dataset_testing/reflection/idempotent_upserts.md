Idempotent Upserts Reflection
Why are idempotent upserts important?
Idempotent upserts ensure that repeated operations produce the same result without unintended side effects, which is critical for:

Reliability: Systems handling repeated updates (e.g., product price feeds) avoid duplicates or inconsistent data.
Concurrency: In high-concurrency scenarios, idempotent operations prevent race conditions, as seen in Challenge 5.
Retrying Failed Operations: Failed requests can be retried safely without creating multiple records.
Data Consistency: Ensures the database reflects the intended state, even with partial failures.

Challenges in implementing upserts

Database Differences:
PostgreSQL’s ON CONFLICT (in upsert_product.py) is atomic and flexible, allowing precise conflict resolution.
SQLite’s INSERT OR REPLACE is less granular, replacing the entire row, which may overwrite unintended fields.


Concurrency Risks: Without proper constraints (e.g., uq_products_name), concurrent upserts could create duplicates.
Performance: Upserts can be slower than simple inserts due to conflict checks, especially for large datasets (relevant to Challenge 9).
Schema Evolution: Adding fields requires updating upsert logic to avoid overwriting new columns.

The solution uses database-specific syntax to ensure idempotency, with unique constraints and Pydantic schemas for consistency.
