## AI Integration Layer

The Astra system includes a Python-based AI risk detection module.

This module is responsible for analyzing behavioral data and generating risk scores.

### Flow Integration

User Device
↓
API Layer
↓
Supabase Backend
↓
Database
↓
AI Risk Engine (Python)
↓
Risk Evaluation
↓
Decision Engine

- low risk → continue monitoring  
- medium risk → prompt user  
- high risk → trigger panic alert  

### Deployment Options

- Python microservice (FastAPI)
- serverless function (future)
- background worker process

### Purpose

This layer enables Astra to transition from reactive alerts to proactive safety detection.
