# Astra Database Schema

## profiles
Stores authenticated user profile data.

Fields:
- id (uuid, primary key)
- full_name (text)
- phone (text)
- role (enum: user / teen / guardian)
- avatar_url (text, optional)
- updated_at (timestamptz)

---

## safety_contacts
Stores trusted contacts for each user.

Fields:
- id (uuid, primary key)
- user_id (uuid, foreign key to profiles)
- contact_name (text)
- contact_phone (text)
- contact_email (text, optional)
- relationship (text, optional)
- is_emergency_contact (boolean, default true)
- created_at (timestamptz)

---

## panic_alerts
Stores panic alert events triggered by the user.

Fields:
- id (uuid, primary key)
- user_id (uuid, foreign key to profiles)
- latitude (float8)
- longitude (float8)
- message (text, optional)
- status (enum: active / resolved / false_alarm)
- resolved_at (timestamptz, optional)
- created_at (timestamptz)

---

## location_sessions
Stores temporary real-time location sharing sessions.

Fields:
- id (uuid, primary key)
- user_id (uuid, foreign key to profiles)
- current_lat (float8)
- current_lng (float8)
- is_active (boolean, default true)
- expires_at (timestamptz)
- created_at (timestamptz)

---

## check_ins
Stores scheduled safety check-ins and their outcomes.

Fields:
- id (uuid, primary key)
- user_id (uuid, foreign key to profiles)
- due_at (timestamptz)
- status (enum: safe / need_help / no_response)
- notes (text, optional)
- completed_at (timestamptz, optional)
- created_at (timestamptz)

---

## verification_records
Stores identity verification data.

Suggested fields:
- id
- user_id
- verification_type
- status
- created_at

---

## evidence_records
Stores metadata for captured evidence.

Suggested fields:
- id
- user_id
- evidence_type
- file_url
- latitude
- longitude
- created_at

---

## alert_recipients
Stores emergency delivery records for trusted contacts.

Suggested fields:
- id
- alert_id
- contact_id
- channel
- status
- sent_at
  
---

## Relationships

- `profiles.id` → parent user record
- `safety_contacts.user_id` → linked to `profiles.id`
- `panic_alerts.user_id` → linked to `profiles.id`
- `location_sessions.user_id` → linked to `profiles.id`
- `check_ins.user_id` → linked to `profiles.id`
