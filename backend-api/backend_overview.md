# Astra Backend Overview

The Astra backend is built on Supabase and supports the core MVP functionality of the Astra personal safety platform.

## Core Backend Capabilities

- User authentication and profile creation
- Trusted safety contact management
- Panic alert creation and escalation workflow
- Real-time location session tracking
- Safety check-in creation and response monitoring
- Realtime subscriptions for alerts and location updates

## Core Backend Components

### Database Tables
- profiles
- safety_contacts
- panic_alerts
- location_sessions
- check_ins

### Edge Functions
- trigger-panic
- check-in-monitor

### Client API
The frontend/backend communication layer is implemented in:

- `src/lib/api.ts`

## Security
- Row Level Security (RLS) enabled on all tables
- Auto profile creation on signup
- Guardian access logic via `is_guardian_of(user_id)`
- Realtime enabled for panic alerts and location sessions

## AI Integration

The backend integrates with a Python-based risk detection engine that evaluates user behavior and supports proactive safety decisions.

## Status
This backend represents the Astra MVP architecture and serves as the technical foundation for future mobile app integration.
