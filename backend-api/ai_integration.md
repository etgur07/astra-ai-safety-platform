# AI Integration Layer

The Astra platform incorporates a Python-based AI risk detection system designed to enhance real-time safety decision-making.

This system transforms Astra from a reactive emergency alert application into a proactive safety intelligence platform.

---

## System Integration Flow

Mobile Application  
↓  
API Layer  
↓  
Supabase Backend (PostgreSQL)  
↓  
Data Storage & Event Logs  
↓  
AI Risk Engine (Python Service)  
↓  
Risk Evaluation & Scoring  
↓  
Decision Engine  

---

## AI Risk Evaluation Logic

The AI module evaluates user safety based on behavioral and contextual signals, including:

- GPS movement patterns
- inactivity duration
- missed check-ins
- time-of-day risk factors
- deviation from expected routes
- safety mode activation status

---

## Risk Scoring Output

The system generates a dynamic risk score and classification:

- Low Risk → continue monitoring
- Medium Risk → trigger safety prompt ("Are you safe?")
- High Risk → initiate emergency escalation

---

## Emergency Escalation Behavior

When high risk is detected:

- panic alert may be triggered automatically
- trusted contacts are notified
- live location sharing is activated
- evidence capture may begin (audio/video)
- escalation to emergency services is suggested

---

## Integration Architecture Options

### Option 1 — Python Microservice (Recommended)

- Built with FastAPI
- Dedicated AI service endpoint
- Endpoint example: `/risk-evaluation`

Flow:
Backend sends user behavioral data → AI returns risk score and recommended action

---

### Option 2 — Background Worker

- Scheduled or event-driven worker
- Continuously scans:
  - check-in status
  - location sessions
- Updates risk level in database

---

### Option 3 — Edge Function Trigger

- Triggered during:
  - panic alerts
  - missed check-ins
- Calls AI service for real-time evaluation

---

## Decision Engine

The AI output feeds into a decision engine that determines:

- whether to notify contacts
- whether to escalate communication channels (push → SMS → call)
- whether to activate evidence capture
- whether to prompt the user for confirmation

---

## Purpose & Impact

This AI integration enables Astra to:

- detect danger before it escalates
- reduce response time in emergencies
- assist vulnerable users (women, teens, individuals at risk)
- provide intelligent safety interventions

---

## Research & Future Development

Future versions of the AI system may include:

- machine learning-based anomaly detection models
- predictive risk modeling using historical data
- real-time route risk scoring
- integration with public safety infrastructure (e.g., emergency dispatch systems)

---

## Positioning

The AI layer positions Astra as:

> A proactive personal safety intelligence system, rather than a simple emergency alert application.
