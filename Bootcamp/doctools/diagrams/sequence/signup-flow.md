# Sign-Up + Email Verification Flow

```mermaid

sequenceDiagram

    participant User
    
    participant Frontend
    
    participant Backend
    
    participant EmailService

    User->>Frontend: Enter email & password
    
    Frontend->>Backend: POST /signup
    
    Backend->>Database: Store user info (status: pending)
    
    Backend->>EmailService: Send verification email
    
    EmailService->>User: Email with verification link
    
    User->>Frontend: Click verification link
    
    Frontend->>Backend: GET /verify-email?token=abc
    
    Backend->>Database: Update status to verified
    
    Backend-->>Frontend: Confirmation page
