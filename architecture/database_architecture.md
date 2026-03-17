# Astra Database Architecture

This diagram represents the relational database structure of the Astra safety platform.

## Core Tables

- users
- panic_alerts
- safety_checkins
- safety_circle_contacts

## Relationships

- Each user can trigger multiple panic alerts
- Each user can have multiple safety contacts
- Each user can create safety check-ins
- Safety contacts are linked via user_id

## Purpose

This database is designed to support:

- real-time emergency alerts
- trusted safety networks
- location-based incident tracking
- proactive safety monitoring

The architecture is implemented using Supabase (PostgreSQL).
