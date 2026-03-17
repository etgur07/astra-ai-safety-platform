# Astra MVP API Design

This document defines the minimum backend API required for the Astra MVP.

The Astra MVP backend is designed to support emergency alerts, trusted safety contacts, temporary location sharing, and safety check-ins.

---

## 1. Authentication / Profile

### POST /auth/signup
Creates a new user account.

Request body:
- full_name
- email
- password
- phone
- role

Response:
- user id
- auth session
- profile created confirmation

---

### POST /auth/signin
Signs in an existing user.

Request body:
- email
- password

Response:
- auth session
- profile data

---

### POST /auth/signout
Ends the current user session.

---

### GET /profile
Returns the current authenticated user profile.

Response fields:
- id
- full_name
- phone
- role
- avatar_url
- updated_at

---

### PATCH /profile
Updates the user profile.

Request body:
- full_name (optional)
- phone (optional)
- avatar_url (optional)

---

## 2. Safety Contacts

### GET /contacts
Returns all safety contacts for the authenticated user.

Response fields:
- id
- contact_name
- contact_phone
- contact_email
- relationship
- is_emergency_contact

---

### POST /contacts
Adds a new safety contact.

Request body:
- contact_name
- contact_phone
- contact_email (optional)
- relationship (optional)
- is_emergency_contact

Response:
- new contact record

---

### DELETE /contacts/{id}
Deletes a safety contact by id.

Response:
- success status

---

## 3. Panic Alerts

### POST /panic-alert
Creates a panic alert and starts emergency escalation.

Request body:
- user_id
- latitude
- longitude
- message (optional)

Response:
- alert_id
- success
- contacts_notified

Notes:
This endpoint may be implemented through an edge function such as `trigger-panic`.

---

### GET /panic-alerts/active
Returns active panic alerts for the authenticated user.

Response:
- alert list
- alert status
- location
- created_at

---

### PATCH /panic-alerts/{id}/resolve
Resolves an active panic alert.

Request body:
- status (resolved or false_alarm)

Response:
- updated alert record

---

## 4. Location Sessions

### POST /location-sessions/start
Starts a real-time location sharing session.

Request body:
- current_lat
- current_lng
- expires_at

Response:
- session_id
- is_active
- created_at

---

### PATCH /location-sessions/{id}
Updates the user’s current location during an active session.

Request body:
- current_lat
- current_lng

Response:
- updated session record

---

### POST /location-sessions/{id}/end
Ends an active location sharing session.

Response:
- session closed confirmation

---

### GET /location-sessions/active
Returns active location sessions for the authenticated user.

---

## 5. Safety Check-Ins

### POST /check-ins
Creates a scheduled safety check-in.

Request body:
- due_at
- notes (optional)

Response:
- check_in_id
- due_at
- status

---

### PATCH /check-ins/{id}/respond
Responds to a safety check-in.

Request body:
- status (safe, need_help, no_response)
- notes (optional)

Response:
- updated check-in record

---

### GET /check-ins/pending
Returns pending and incomplete check-ins.

Response:
- check-in list
- due_at
- status

---

## 6. Realtime Subscriptions

### subscribeToAlerts
Realtime subscription for panic alerts.

### subscribeToLocationUpdates
Realtime subscription for location session updates.

---

## 7. Edge Functions

### trigger-panic
Purpose:
- create panic alert
- fetch emergency contacts
- fetch profile data
- log notification intent

### check-in-monitor
Purpose:
- detect overdue check-ins
- identify contacts to notify
- expire stale location sessions

---

## MVP API Goal

The Astra MVP API is designed to support the minimum functional workflow required to validate the product:

- user account creation
- trusted contact management
- emergency alert creation
- temporary location sharing
- scheduled safety check-ins
