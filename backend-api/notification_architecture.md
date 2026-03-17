# Astra Notification Architecture

Astra uses a multi-channel emergency alert system.

## Notification Channels

- Push notification
- In-app alert
- SMS fallback
- Voice call escalation
- Live chat activation

## Trusted Contact Incoming Alert

When a high-risk event occurs, trusted contacts may receive:

- emergency title
- live location access
- risk level
- evidence status
- call user action
- call 911 action
- open chat action

## Escalation Logic

1. Push notification sent
2. If no response → SMS fallback
3. If high risk persists → voice call escalation
