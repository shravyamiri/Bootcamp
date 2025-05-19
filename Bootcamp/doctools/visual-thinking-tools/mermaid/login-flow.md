```mermaid
sequenceDiagram
  participant User
  participant Frontend
  participant Backend
  participant DB

  User->>Frontend: Login form
  Frontend->>Backend: POST /login
  Backend->>DB: Query user
  DB-->>Backend: User data
  Backend-->>Frontend: Success token
  Frontend-->>User: Redirect to dashboard
