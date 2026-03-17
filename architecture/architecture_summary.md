# Astra System Architecture

Astra is built as a cloud-based safety platform using a serverless architecture.

The system leverages Supabase for database management, authentication, and realtime updates.

---

# High Level Architecture

User Device (Mobile App)
↓
Frontend Application (React)
↓
Client API Layer
↓
Supabase Backend
↓
PostgreSQL Database + Edge Functions

---

# Core Backend Components

## Database Layer

PostgreSQL database managed by Supabase.

Tables:

profiles  
safety_contacts  
panic_alerts  
location_sessions  
check_ins  

---

## Authentication Layer

Supabase Auth manages user authentication.

Signup flow:

User registers  
↓  
Auth account created  
↓  
Trigger function creates profile row

Trigger:
handle_new_user()

---

## Security Layer

Row Level Security (RLS) ensures user data isolation.

Rules:

Users can access only their own records.

Guardian access allowed through function:

is_guardian_of(user_id)

---

## Edge Function Layer

Two serverless functions implement core system logic.

### trigger-panic

Responsibilities:
- create panic alert
- retrieve emergency contacts
- log notification intent

Future integration:
Twilio / SMS notifications

---

### check-in-monitor

Responsibilities:
- detect overdue check-ins
- retrieve emergency contacts
- expire location sessions

This function enables automated safety escalation.

---

# Realtime Infrastructure

Realtime subscriptions provide live updates for:

panic alerts  
location sessions

Technology:
Supabase Realtime

---

# Client API Layer

The API abstraction layer is implemented in:

src/lib/api.ts

Responsibilities:
- authentication requests
- safety contact management
- alert creation
- location updates
- realtime subscriptions

---

# Scalability

The architecture supports scaling through:

serverless edge functions  
managed database infrastructure  
realtime streaming updates

This allows Astra to support large numbers of concurrent users while maintaining low infrastructure complexity.

---

# Future Architecture Expansion

Planned improvements:

AI risk detection models  
automated SMS escalation  
wearable device integration  
predictive safety analytics
