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
|----------|------|
| Missed check-in | +2 |
| Panic history | +3 |
| Late night activity | +1 |
| Route deviation | +2 |

---

## Threshold Logic

- 0–2 → Low risk
- 3–4 → Medium risk
- 5+ → High risk

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
