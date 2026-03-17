# Astra Product Specification

Astra is a personal safety platform focused on providing rapid emergency communication and safety monitoring tools.

The system combines mobile interaction, realtime location sharing, and safety escalation workflows.

---

# Product Vision

To create a scalable digital safety network that enables individuals to instantly alert trusted contacts during dangerous situations.

Primary target users:
- women
- teenage girls
- parents monitoring teen safety

---

# Key System Components

## User Identity Layer

Authentication system that links user accounts to safety networks.

Technology:
Supabase Auth

Functions:
- signUp
- signIn
- signOut
- profile creation

---

## Safety Network Layer

Users define trusted contacts who will receive emergency notifications.

Functions:
- addSafetyContact
- deleteSafetyContact
- getSafetyContacts

Database:
safety_contacts

---

## Emergency Alert System

The panic alert system allows users to immediately signal distress.

Trigger:
User presses panic button.

System actions:
1. Create panic_alert record
2. Fetch emergency contacts
3. Log notification event

Edge Function:
trigger-panic

---

## Location Tracking System

Users can share temporary real-time location.

Functions:
- startLocationSession
- updateLocation
- endLocationSession

Database:
location_sessions

Realtime subscription:
subscribeToLocationUpdates

---

## Safety Check-in System

Users schedule check-ins to confirm safety.

If a user does not respond before the deadline, the system flags the event.

Edge Function:
check-in-monitor

Database:
check_ins

Status values:
- safe
- need_help
- no_response

---

# Security Architecture

Security model uses:

- Supabase Auth
- Row Level Security
- Guardian access control

Policies:
Users can only modify their own records.

Guardian users can read safety data for monitored users.

---
## AI and Risk Detection Layer

The Astra system includes an AI-driven risk detection component implemented in Python.

This layer is responsible for analyzing behavioral patterns and detecting potential safety risks.

### Technology
- Python
- Data processing (NumPy / Pandas - optional)
- Rule-based scoring system (MVP)
- Future: Machine Learning models

### Inputs
- GPS coordinates
- timestamp
- movement speed
- route history
- safety mode status
- check-in response status

### Outputs
- risk score
- anomaly detection flag
- safety prompt trigger
- emergency alert trigger

### Responsibilities
- detect abnormal movement patterns
- evaluate missed check-ins
- calculate risk score
- trigger escalation logic

### Integration

The AI layer can be integrated with the backend via:

- API endpoint (Python microservice)
OR
- Edge function trigger
OR
- scheduled background process

This allows Astra to evolve from rule-based logic into a machine learning-driven system.

---

## Technology Stack

Backend: Supabase (PostgreSQL)  
Edge Functions: Deno serverless functions  
AI Layer: Python (risk detection & scoring engine)  
Frontend: React + TypeScript  
Realtime: Supabase Realtime  
UI: shadcn components  
---

# System Goals

The product must:

- respond instantly to emergency events
- protect user privacy
- maintain secure data access
- provide reliable location updates
