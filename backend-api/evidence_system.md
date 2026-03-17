# Evidence Storage System

Astra includes a secure evidence capture and storage system designed to preserve critical data during emergency situations.

---

## Features

- audio recording
- video recording
- photo capture
- automatic evidence capture
- timestamp tagging
- GPS location tagging

---

## Storage Architecture

All evidence is stored using Supabase Storage.

### Bucket:
- evidence-files (private)

### File Structure:

evidence-files/
  user_id/
    alert_id/
      audio_001.wav
      video_001.mp4
      photo_001.jpg

---

## Database Integration

Metadata is stored in the `evidence_records` table.

Fields include:
- user_id
- alert_id
- file_url
- file_type
- created_at
- latitude
- longitude

---

## Security

- private storage buckets
- signed URL access
- role-based access control
- encrypted data handling

---

## Purpose

This system ensures that users can preserve evidence during emergencies, which may support personal safety, reporting, and investigation processes.
