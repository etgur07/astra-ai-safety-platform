# Astra MVP Scope

Astra is a personal safety platform designed to help protect women and teenage girls through trusted safety networks, real-time location sharing, and emergency alert systems.

This document defines the Minimum Viable Product (MVP) feature scope.

---

# Core MVP Features

## 1. User Accounts
Users can create secure accounts and manage personal profile information.

Capabilities:
- Email authentication
- Profile creation
- Role assignment (user, teen, guardian)

Database:
profiles

---

## 2. Safety Circle (Trusted Contacts)

Users can add trusted contacts who will be notified during emergencies.

Capabilities:
- Add emergency contact
- Remove contact
- Mark contacts as emergency contacts
- Store phone/email

Database:
safety_contacts

---

## 3. Panic Alerts

A one-tap emergency alert system.

Capabilities:
- Create panic alert
- Send GPS coordinates
- Attach optional message
- Notify safety contacts

Database:
panic_alerts

Edge Function:
trigger-panic

---

## 4. Location Sharing

Users can temporarily share their location with trusted contacts.

Capabilities:
- Start location session
- Update location
- End location session
- Automatic expiration

Database:
location_sessions

Realtime updates enabled.

---

## 5. Safety Check-ins

Scheduled safety check-ins ensure users confirm their safety.

Capabilities:
- Create scheduled check-in
- Respond safe / need help
- Detect missed check-ins

Database:
check_ins

Edge Function:
check-in-monitor

---

# Guardian Mode

Guardian users (such as parents or trusted adults) can monitor alerts and location sessions for users they are responsible for.

Logic:
is_guardian_of(user_id)

Capabilities:
- View active panic alerts
- View location sessions

---

# Realtime Features

The following data streams support realtime updates:

- panic_alerts
- location_sessions

Technology:
Supabase Realtime

---

# MVP Goal

The MVP demonstrates that Astra can:

- create a safety network
- detect emergency events
- share location in real time
- escalate alerts to trusted contacts

Future versions may include:

- SMS notification integration
- AI-based risk detection
- wearable device integration
- predictive safety analytics
