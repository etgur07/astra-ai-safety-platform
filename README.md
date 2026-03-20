# ASTRA – AI-Enabled Personal Safety Platform

ASTRA is an AI-enabled personal safety platform designed to support real-time protection, proactive risk awareness, and emergency-response coordination through a mobile-first safety architecture.

Unlike conventional panic-button applications that depend only on manual activation, ASTRA combines **user-initiated emergency alerting** with **AI-assisted behavioral and contextual risk assessment**. The platform is intended to function both in immediate emergency situations and in scenarios where risk may build gradually through missed check-ins, abnormal inactivity, route deviation, or unusual behavioral patterns.

ASTRA is designed as a hybrid safety system that integrates emergency response workflows, trusted-contact communication, evidence capture, contextual safety monitoring, and a future-facing anomaly detection layer into a unified ecosystem.

---

## Vision

ASTRA aims to become a proactive safety intelligence platform that helps protect individuals—especially women, teenagers, and other vulnerable users—through faster emergency response, contextual risk awareness, and intelligent escalation support.

---

## Core Safety Philosophy

ASTRA is built around two complementary safety modes:

1. **Manual emergency activation**, where users can trigger immediate assistance through a panic alert or safety action.
2. **AI-assisted risk detection**, where the system evaluates contextual, temporal, and behavioral signals to identify elevated concern and support adaptive escalation.

This hybrid structure reflects the practical reality that safety systems should not rely exclusively on either manual input or full automation. Instead, ASTRA is designed to combine both approaches in a user-centered and operationally realistic way.

---

## Core Features

### Panic Alert System
- One-tap emergency trigger
- Instant alert creation
- Trusted-contact notification
- Live GPS location sharing

### Emergency Escalation Support
- Direct emergency-call access
- Suggested escalation during high-risk situations
- Future interoperability path toward NG911-style integration

### Safety Circle (Trusted Contacts)
- Add and manage emergency contacts
- Multi-channel alert delivery
- Real-time visibility during emergencies

### Real-Time Location Sharing
- Temporary live location sessions
- Movement visibility for trusted contacts
- Automatic expiration for privacy protection

### Safety Check-In System
- Scheduled safety confirmations
- Missed check-ins increase concern level
- Escalation if no user response is received

### Guardian Mode
- Designed for teens and monitored users
- Guardian-level safety visibility
- Alert escalation for missed confirmation or abnormal conditions

### Identity Verification
- Selfie verification
- Optional ID verification
- Added trust within the safety network

---

## AI-Powered Safety Layer

ASTRA includes a planned and evolving AI-based safety intelligence layer designed to complement emergency alert workflows.

This layer is intended to support:

- missed check-in detection
- unusual inactivity analysis
- time-based risk evaluation
- route deviation awareness
- behavioral anomaly detection
- adaptive risk scoring

Rather than replacing manual emergency input, the AI layer is designed to **support earlier interpretation of elevated concern** and improve the platform’s ability to respond when users are unable to act immediately.

### Risk Levels
- **Low Risk** → continue background monitoring
- **Medium Risk** → prompt user verification
- **High Risk** → trigger emergency escalation workflow

---

## Evidence Capture System

ASTRA includes a built-in emergency evidence subsystem to support documentation during critical events.

Features include:
- audio recording
- video recording
- photo capture
- timestamping
- GPS tagging
- secure cloud storage

This subsystem is intended to preserve safety-relevant evidence under emergency conditions and support trusted-contact or emergency-response workflows.

---

## Communication Layer

### Live Chat
- Real-time communication with trusted contacts

### Voice and Hands-Free Safety Support
- Voice-enabled interaction
- Reduced dependency on typing under stress
- Future AI safety assistant support

### Multi-Channel Notification
- Push notification
- In-app alert
- SMS fallback
- Voice-call escalation

This layered communication design is intended to improve delivery reliability in urgent situations.

---

## Trusted Contact Alert System

When an emergency is triggered or the system identifies elevated concern, trusted contacts may receive:

- emergency alert notification
- live location access
- risk-level information
- missed check-in notification
- evidence-capture status indicators

Available response actions may include:
- viewing live location
- calling the user
- opening live chat
- contacting emergency services

---

## System Architecture

### Frontend
- React + TypeScript
- Mobile-first UI

### Backend
- Supabase
- PostgreSQL
- Row Level Security (RLS)
- Authentication and user-profile layer
- Edge Functions for operational workflows

### AI Layer
- Python-based risk scoring engine
- Anomaly detection and escalation logic
- FastAPI microservice planned

### Realtime
- Supabase Realtime subscriptions
- Live alert state updates
- Contact notification workflows

---

## User Flows

### Panic Flow
User → Panic Button → Alert Created → Contacts Notified → Risk Context Updated → Escalation Workflow

### Check-In Flow
Timer → No Response → Risk Increase → User Prompt → Alert Triggered

### AI-Assisted Flow
Behavioral / contextual signals → Risk engine → Decision output → System action

---

## Database Structure

### Core Tables
- `profiles`
- `safety_contacts`
- `panic_alerts`
- `location_sessions`
- `check_ins`

### Additional Tables
- `evidence_records`
- `alert_recipients`
- `verification_records`

---

## System Goals

ASTRA is designed to:
- respond quickly to emergency events
- support proactive risk interpretation
- preserve safety-relevant evidence
- protect user privacy
- ensure reliable communication
- support vulnerable populations through adaptive safety workflows

---

## Ethical Commitments

ASTRA prioritizes:
- consent-based data collection
- secure data handling
- privacy-aware design
- responsible AI use
- proportional escalation
- user autonomy

---

## Research and Development Direction

Future development includes:
- machine-learning-based anomaly detection
- route deviation modeling
- contextual safety scoring
- predictive safety modeling
- safer-route recommendations
- deeper wearable integration
- emergency-system interoperability

---

## Positioning

ASTRA is not only a panic button application.

It is a hybrid personal safety platform that combines:
- emergency alerting
- contextual risk awareness
- behavioral anomaly detection
- trusted-contact coordination
- intelligent escalation logic

---

## Project Structure

```text
astra-ai-safety-platform/
│
├── mvp/
├── backend-api/
├── ai-model/
├── architecture/
├── research/
├── docs/
└── README.md
