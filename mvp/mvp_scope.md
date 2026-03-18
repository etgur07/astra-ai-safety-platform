# Astra MVP Scope

Astra is a proactive personal safety platform designed to protect women and teenage girls through trusted safety networks, real-time monitoring, and AI-assisted risk detection.

This document defines the Minimum Viable Product (MVP) scope and core system capabilities.

---

# Core MVP Features

## 1. User Accounts

Users can create secure accounts and manage their personal profiles.

Capabilities:
- Email authentication
- Profile creation
- Role assignment (user, teen, guardian)

Database:
profiles

---

## 2. Safety Circle (Trusted Contacts)

Users can define trusted contacts who will receive emergency alerts.

Capabilities:
- Add safety contact
- Remove safety contact
- Mark contacts as emergency contacts
- Store phone and email information

Database:
safety_contacts

---

## 3. Panic Alerts

A one-tap emergency alert system that instantly notifies trusted contacts.

Capabilities:
- Create panic alert
- Capture GPS location
- Attach optional message
- Notify safety contacts

Database:
panic_alerts

Edge Function:
trigger-panic

---

## 4. Location Sharing

Users can temporarily share their real-time location with trusted contacts.

Capabilities:
- Start location session
- Update location in real time
- End location session
- Automatic session expiration

Database:
location_sessions

Realtime updates enabled.

---

## 5. Safety Check-ins

Users can schedule check-ins to confirm their safety status.

Capabilities:
- Create scheduled check-in
- Respond with:
  - safe
  - need_help
- Detect missed check-ins
- Trigger escalation if no response

Database:
check_ins

Edge Function:
check-in-monitor

---

## 6. AI Risk Detection (MVP Layer)

Astra includes a lightweight AI-based risk detection system implemented using rule-based logic.

Purpose:
To enable proactive safety detection without requiring manual user input.

Capabilities:
- evaluate missed check-ins
- detect inactivity or abnormal movement
- assess time-based risk (e.g., late-night activity)
- generate dynamic risk scores
- trigger escalation when thresholds are reached

Technology:
- Python-based risk scoring engine

Integration:
- AI evaluates behavioral data from backend
- supports proactive alerts and user prompts

---

## 7. Guardian Mode

Guardian users (e.g., parents or trusted adults) can monitor safety data.

Capabilities:
- View active panic alerts
- View real-time location sessions
- Monitor safety status

Logic:
is_guardian_of(user_id)

---

## 8. Emergency Evidence Capture

The system supports automatic and manual evidence collection during emergency situations.

Capabilities:

- audio recording
- video recording
- photo capture
- automatic trigger during high-risk detection
- secure cloud storage
- timestamp and location tagging


# Realtime Features

The system supports real-time updates for:

- panic alerts
- location sessions

Technology:
Supabase Realtime

---

# MVP Goal

The Astra MVP demonstrates the ability to:

- create a trusted safety network  
- enable instant emergency alerts  
- share location in real time  
- monitor user safety behavior  
- detect potential risk using AI  
- escalate alerts proactively  

---

# Future Enhancements

The following features are planned for future versions:

- SMS and push notification integration  
- machine learning-based anomaly detection  
- route deviation analysis  
- wearable device integration  
- predictive safety analytics  
