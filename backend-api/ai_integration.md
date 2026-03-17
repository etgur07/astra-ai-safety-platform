# AI Integration Layer

The Astra system includes a Python-based AI risk detection module.

This module is designed to integrate with the backend system and enhance safety decision-making.

## Integration Flow

Mobile App  
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
Decision Output  

- low risk → continue monitoring  
- medium risk → prompt user  
- high risk → trigger panic alert  

## Integration Options

### Option 1 — Python Microservice
- built with FastAPI
- API endpoint: /risk-evaluation
- backend sends user data → receives risk score

### Option 2 — Background Worker
- scheduled process
- scans check-ins and location data
- updates risk level

### Option 3 — Edge Function Trigger
- edge function calls Python service
- used during panic or check-in events

## Purpose

This integration enables Astra to move from reactive safety alerts to proactive risk detection.
