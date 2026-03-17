# Astra AI Risk Detection – Pseudocode

Goal:
Detect unusual movement or safety-related anomalies using mobile location and activity data.

Inputs:
- GPS coordinates
- Timestamp
- Movement speed
- Route history
- Safety mode status
- Check-in response status

Output:
- risk score
- safety prompt
- contact alert trigger

Example logic:
1. User enables Safety Mode
2. App collects periodic location updates
3. System compares live movement to expected route
4. If user stops unexpectedly or misses a check-in:
   - risk score increases
5. If risk score crosses threshold:
   - Astra asks: "Are you safe?"
6. If no response:
   - Astra sends an alert to Safety Circle
