# Welcome to My Documentation

- [About](/about/)
- [Contact](/contact/)

## Login Flow Diagram

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant DB

    User->>Frontend: Submit Login Form
    Frontend->>Backend: Send Credentials
    Backend->>DB: Query User Credentials
    DB->>Backend: Return User Data
    Backend->>Frontend: Return Authentication Token
    Frontend->>User: Show Logged In Page
