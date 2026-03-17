# Astra AI Model Logic

## Model Type

Hybrid system:

- Rule-based scoring (current MVP)
- Machine learning models (future phase)

---

## Phase 1: Rule-Based System

The system calculates a risk score based on predefined conditions:

- missed check-ins
- abnormal stop duration
- route deviation
- inactivity
- night-time movement

Each factor contributes to a cumulative score.

---

## Risk Scoring Example

| Condition | Score |
|----------|------:|
| Missed check-in | +40 |
| Low movement / inactivity | +20 |
| Late night activity | +15 |
| Safety mode active | +10 |
---

## Threshold Logic

- 0–30 → Low risk
- 31–60 → Medium risk
- 61+ → High risk
---

## Phase 2: Machine Learning (Future)

- classification models
- anomaly detection
- sequence modeling (user behavior patterns)

---

## Key Concept

The system evolves from:

Rule-based heuristics → Data-driven intelligence → Predictive safety system

---

## Importance

This approach allows Astra to:

- reduce response time
- detect hidden risks
- protect users without manual action
