# Astra API Endpoints

## Health
GET /health

## Users
POST /users
GET /users/{id}

## Safety Circle
POST /contacts
GET /contacts/{user_id}
DELETE /contacts/{id}

## Panic Alerts
POST /panic-alert
GET /panic-alerts/{user_id}

## Location Sharing
POST /share-location
GET /location-session/{id}
POST /end-location-session

## Safety Check-Ins
POST /safety-checkin
GET /safety-checkins/{user_id}
