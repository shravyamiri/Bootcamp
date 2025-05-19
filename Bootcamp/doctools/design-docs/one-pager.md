# One-Pager Design Document

## Problem
Users currently register but never verify their email.

## Goals
- Ensure users verify email before accessing protected content.

## Non-Goals
- Password reset
- Multi-factor authentication

## Options
1. Send email with unique verification link (token-based).
2. OTP via mobile.
3. Use third-party OAuth.

## Decision
Option 1 — email with unique verification link for simplicity and coverage.

## Risks
- Email deliverability issues
- Token link could be intercepted if not using HTTPS
# System Architecture Map

## Components

- **Frontend**: React app
- **Backend**: Node.js + Express
- **Database**: PostgreSQL
- **Auth Service**: Handles user login and tokens

## Data Flow

1. User sends request from frontend.
2. Backend authenticates using JWT.
3. Backend talks to Database or Auth Service.
4. Data is returned to frontend for rendering.

## Constraints

- Backend must respond < 200ms
- User data is encrypted at rest
- Token expiration: 24h
