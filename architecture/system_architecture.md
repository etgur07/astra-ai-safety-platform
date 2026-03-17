Astra System Architecture
              ┌────────────────────────┐
              │     Mobile App         │
              │   (React / UI Layer)   │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │    Client API Layer    │
              │     src/lib/api.ts     │
              └───────────┬────────────┘
                          │
                          ▼
            ┌─────────────────────────────┐
            │        Supabase Backend     │
            │                             │
            │  Auth  │  Realtime  │ Edge  │
            └───────┬─────────────┬───────┘
                    │             │
                    ▼             ▼
         ┌─────────────────┐  ┌────────────────────┐
         │ PostgreSQL DB   │  │   Edge Functions   │
         │                 │  │                    │
         │ profiles        │  │ trigger-panic      │
         │ safety_contacts │  │ check-in-monitor   │
         │ panic_alerts    │  │                    │
         │ location_sessions│ └────────────────────┘
         │ check_ins       │
         └─────────────────┘
