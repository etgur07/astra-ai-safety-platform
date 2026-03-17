# Astra – AI-Powered Personal Safety Platform

Astra is an AI-driven personal safety platform designed to provide real-time protection, proactive risk detection, and emergency response support.

Inspired by systems like KADES, Astra extends safety beyond government-controlled environments by integrating artificial intelligence, real-time data, and trusted social networks into a unified safety ecosystem.

---

## 🌍 Vision

Astra aims to become a proactive safety intelligence system that protects individuals—especially women and teenagers—by detecting potential danger before it escalates and enabling rapid, intelligent response during emergencies.

---

## 🚨 Core Features

### 🔴 Panic Alert System
- One-tap emergency trigger
- Instantly notifies trusted contacts
- Sends live GPS location

### 📞 Call 911 Integration
- Direct emergency call access
- Suggested escalation during high-risk events

### 👥 Safety Circle (Trusted Contacts)
- Add and manage emergency contacts
- Multi-channel alert delivery (push, SMS, call)

### 📍 Real-Time Location Sharing
- Temporary live location sessions
- Share movement with trusted contacts
- Automatic expiration

### ⏱ Safety Check-In System
- Scheduled safety confirmations
- Missed check-ins trigger escalation

### 🛡 Guardian Mode
- Designed for teens and monitored users
- Guardian-level visibility and alerts

### 🔐 Identity Verification
- Selfie and optional ID verification
- Improves trust within safety network

---

## 🧠 AI-Powered Safety Layer

Astra integrates a Python-based AI risk detection engine.

### AI Capabilities:
- Detect unusual movement patterns
- Identify missed check-ins
- Analyze inactivity and time-based risk
- Evaluate behavioral anomalies

### Risk Levels:
- Low → continue monitoring
- Medium → safety prompt ("Are you safe?")
- High → emergency escalation

---

## 🎥 Evidence Capture System

Astra includes a built-in emergency evidence system:

- Audio recording
- Video recording
- Photo capture
- Automatic capture during high-risk events
- Timestamp and GPS tagging
- Secure cloud storage

This feature enables users to preserve critical evidence during emergency situations.

---

## 💬 Communication Layer

### Live Chat
- Real-time communication with trusted contacts

### AI Safety Assistant
- Chat + voice interaction
- Hands-free support in emergency scenarios

### Voice Input Support
- Users can interact without typing
- Critical for high-stress situations

---

## 🚨 Trusted Contact Alert System

When an emergency is triggered, trusted contacts receive:

- Emergency alert notification
- Live location access
- Risk level status
- Evidence capture indicators
- Missed check-in alerts

### Available Actions:
- View live location
- Call the user
- Call 911
- Open live chat

---

## 🧩 System Architecture

### Backend
- Supabase (PostgreSQL)
- Row Level Security (RLS)
- Auth system with user profiles

### Edge Functions (Deno)
- trigger-panic
- check-in-monitor

### AI Layer
- Python-based risk scoring engine
- FastAPI microservice (planned)

### Frontend
- React + TypeScript
- Mobile-first UI design

### Realtime
- Supabase Realtime subscriptions

---

## 🔔 Notification Architecture

Multi-channel alert system:

1. Push Notification
2. In-app alert
3. SMS fallback
4. Voice call escalation

Ensures delivery even in critical scenarios.

---

## 🔄 User Flows

### Panic Flow
User → Panic Button → Alert Created → Contacts Notified → AI Evaluates → Escalation

### Check-In Flow
Timer → No Response → Risk Increase → Alert Triggered

### AI Flow
Behavior Data → Risk Engine → Decision Output → System Action

---

## 📊 Database Structure

Core tables:

- profiles
- safety_contacts
- panic_alerts
- location_sessions
- check_ins

Additional:

- evidence_records
- alert_recipients
- verification_records

---

## 🎯 System Goals

Astra is designed to:

- Respond instantly to emergency events
- Detect risk proactively using AI
- Preserve critical evidence
- Protect user privacy
- Ensure reliable communication
- Support vulnerable populations

---

## 🔬 Future Development

- Machine learning-based anomaly detection
- Predictive safety modeling
- Route deviation analysis
- Safer route recommendations
- Integration with public safety systems (NG911)

---

## ⚖️ Ethical Considerations

Astra prioritizes:

- user privacy
- secure data handling
- consent-based data collection
- responsible AI usage

---

## 🚀 Positioning

Astra is not just a panic button app.

It is:

> An AI-powered personal safety intelligence platform designed for real-world risk detection and emergency response.

---

## 📁 Project Structure

├── mvp/              # product scope, features, flows
├── backend-api/      # API design, database, services
├── ai-model/         # AI risk detection logic
├── architecture/     # system diagrams and flows
├── research/         # papers, EB2 documentation
├── docs/             # supporting documentation

---

## 👩‍💻 Author

Developed as part of an advanced safety technology initiative combining AI, real-time systems, and human-centered design.

---

## 📌 Status

MVP + AI integration + system architecture complete  
Actively expanding toward research, deployment, and real-world applications
