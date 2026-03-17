# Astra AI Risk Detection – Pseudocode

## Goal
Detect unusual movement or safety-related anomalies using user activity and location data.

---

## Inputs

- GPS coordinates
- timestamp
- movement speed
- route history
- safety mode status
- check-in response status

---

## Output

- risk score
- safety prompt
- emergency alert trigger

---

## Logic

1. User activates Safety Mode

2. System collects periodic location updates

3. Compare current movement with expected route

4. Detect anomalies:
   - sudden stop
   - route deviation
   - inactivity
   - missed check-in

5. Increase risk score based on conditions

6. If risk score exceeds threshold:
   → trigger safety prompt ("Are you safe?")

7. If no response:
   → send alert to Safety Circle

IF risk_score > HIGH_THRESHOLD:
    trigger_panic()
    start_evidence_capture()
