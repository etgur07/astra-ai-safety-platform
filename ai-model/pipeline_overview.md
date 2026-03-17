# AI Pipeline Overview

## Step-by-Step Flow

1. User activates Safety Mode  
2. Mobile app continuously collects:
   - GPS location  
   - movement speed  
   - route history  
   - check-in status  
   - inactivity signals  

3. Data is sent to backend (Supabase)

4. Backend forwards relevant data to AI Risk Engine (Python)

5. AI Risk Engine evaluates:
   - missed check-ins  
   - inactivity duration  
   - time-of-day risk  
   - abnormal movement patterns  
   - deviation from expected route  

6. Risk score is calculated

---

## Decision Engine

Based on the risk score:

### Low Risk
- continue monitoring  
- no action required  

### Medium Risk
- trigger safety prompt  
  → "Are you safe?"  
- wait for user response  

### High Risk
- trigger panic alert  
- notify Safety Circle  
- activate real-time location sharing  
- initiate evidence capture (audio/video/photo)  
- prepare escalation  

---

## Escalation Logic

If no user response:

1. Send push notification to contacts  
2. Send SMS fallback  
3. Trigger voice call alert (optional)  
4. Suggest or trigger 911 call  

---

## Evidence Capture Integration

During high-risk scenarios:

- audio recording starts  
- video capture may activate  
- photos may be taken  
- files are uploaded to secure cloud storage  
- metadata (time + location) is stored  

---

## Trusted Contact Flow

Trusted contacts receive:

- emergency alert  
- live location  
- risk level  
- evidence status  

They can:
- call the user  
- call 911  
- open live chat  

---

## Output

The system produces:

- risk_score  
- risk_level  
- alert_status  
- escalation_status  

---

## Purpose

This pipeline enables Astra to:

- detect risk proactively  
- respond intelligently  
- preserve emergency evidence  
- ensure reliable communication  

---

## Future Expansion

- machine learning-based anomaly detection  
- predictive safety modeling  
- route-based risk scoring  
- public safety integration (NG911)
