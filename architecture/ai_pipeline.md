# Astra AI Pipeline

```mermaid
flowchart TD

A[User Device] --> B[Location & Activity Data]
B --> C[Data Processing Layer]

C --> D[Feature Extraction]
D --> E[Risk Scoring Engine]

E --> F{Risk Level}

F -->|Low| G[Continue Monitoring]
F -->|Medium| H[Prompt User: Are you safe?]
F -->|High| I[Trigger Emergency Alert]

I --> J[Notify Safety Circle]
