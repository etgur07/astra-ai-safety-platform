flowchart LR

A[Mobile App] --> B[API Layer]
B --> C[Supabase Backend]

C --> D[Database]
C --> E[AI Engine - Python]

D --> E

E --> F[Risk Scoring]
F --> G{Risk Level}

G -->|Low| H[Continue Monitoring]
G -->|Medium| I[Prompt User]
G -->|High| J[Trigger Alert]

J --> K[Notify Safety Contacts]
