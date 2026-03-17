# Astra Data Flow

```mermaid
flowchart LR

A[Mobile App] --> B[API Layer]
B --> C[Backend System]

C --> D[Database]
C --> E[AI Engine]

E --> F[Risk Evaluation]

F --> G[User Notification]
F --> H[Emergency Contacts]

D --> E
