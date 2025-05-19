Model Boundary Enforcement Reflection
Why is it risky to return raw ORM objects directly?

Leaking Implementation Details: SQLAlchemy models include internal attributes (e.g., _sa_instance_state) that can expose database-specific metadata or sensitive information, breaking API contracts.
Security Risks: Raw models may include unfiltered fields (e.g., passwords) or lazy-loaded relationships, risking unintended data exposure or performance issues from excessive queries.
Tight Coupling: Exposing ORM objects ties the API to the database schema, making it harder to evolve the schema without breaking clients.
Validation Gaps: ORM objects bypass Pydantic’s validation, potentially sending invalid or inconsistent data to clients.

What happens if database schema evolves but external APIs do not?

API Inconsistency: If the schema adds fields (e.g., created_at from Challenge 1), but the Pydantic schema (UserResponseSchema) isn’t updated, clients miss new data, leading to incomplete functionality.
Breaking Changes: Removing or renaming columns (e.g., email) can cause ORM queries to fail if the API doesn’t adapt, resulting in errors or crashes.
Data Mismatch: Clients may receive unexpected data types or formats, causing parsing errors or incorrect behavior.
Maintenance Overhead: Developers must manually sync API schemas with database changes, increasing the risk of errors.

Using Pydantic models, as in update_profile.py, ensures strict separation, validated responses, and flexibility for schema evolution, mitigating these risks.
