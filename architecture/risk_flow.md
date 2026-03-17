# Astra Risk Detection Flow

```mermaid
flowchart TD

A[User activates Safety Mode] --> B[Collect location & activity data]
B --> C[Analyze movement patterns]

C --> D{Anomaly detected?}

D -- No --> E[Continue monitoring]

D -- Yes --> F[Increase risk score]

F --> G{Risk threshold reached?}

G -- No --> E

G -- Yes --> H[Prompt user: Are you safe?]

H --> I{User responds?}

I -- Yes --> J[Mark as safe]

I -- No --> K[Trigger alert to Safety Circle]
