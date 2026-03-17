# Astra MVP Backend API

## Authentication / Profile
- signUp
- signIn
- signOut
- getProfile
- updateProfile

## Safety Contacts
- getSafetyContacts
- addSafetyContact
- deleteSafetyContact

## Panic Alerts
- triggerPanic
- getActiveAlerts
- resolveAlert

## Location Sessions
- startLocationSession
- updateLocation
- endLocationSession

## Safety Check-Ins
- createCheckIn
- respondToCheckIn
- getPendingCheckIns

## Realtime
- subscribeToAlerts
- subscribeToLocationUpdates

---

## Edge Functions

### trigger-panic
Purpose:
- creates a panic alert
- fetches emergency contacts
- fetches profile data
- logs notification intent

### check-in-monitor
Purpose:
- finds overdue check-ins
- identifies contacts to notify
- expires stale location sessions
