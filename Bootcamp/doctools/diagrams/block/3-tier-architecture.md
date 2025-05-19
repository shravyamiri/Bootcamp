# 3-Tier Architecture (Client → Backend → Database)

This document describes a simple **3-tier architecture** used in modern web applications. It clearly separates responsibilities across three main layers:

---

## 🧱 Architecture Layers

### 1. **Client (Web browser, Mobile app)**
- The presentation layer.
- This is what the user interacts with.
- Examples: Chrome, Safari, Android/iOS apps.
- Responsibilities:
  - Display UI
  - Capture user inputs
  - Communicate with backend via API calls (typically using HTTP)

### 2. **Backend (REST API)**
- The application/business logic layer.
- Acts as a middleman between the client and the database.
- Examples: Express.js, Django, Spring Boot, Flask.
- Responsibilities:
  - Receive requests from the client
  - Validate, process and implement logic
  - Interact with the database
  - Send back responses to the client

### 3. **Database (MySQL)**
- The data layer (persistence).
- Stores and retrieves data upon request by the backend.
- Example: MySQL (RDBMS).
- Responsibilities:
  - Execute SQL queries from backend
  - Return requested data
  - Ensure data integrity and security

---

## 🔁 Data Flow

```text
Client (UI)
   ⇅
Backend (REST API)
   ⇅
Database (MySQL)
