# Astra AI Model

This folder contains the AI risk detection framework for the Astra safety platform.

The purpose of this layer is to evaluate behavioral and contextual signals in order to detect potential safety risks before escalation.

## Included Files

- `ai_model_overview.md` — high-level overview of the Astra AI safety system
- `ai_model_logic.md` — scoring model, thresholds, and future ML roadmap
- `pseudocode.md` — step-by-step decision flow
- `pipeline_overview.md` — implementation-oriented pipeline summary
- `code/risk_scoring.py` — minimal Python prototype for rule-based risk scoring

## Role in the System

This AI layer complements the Astra backend by adding proactive risk evaluation on top of core safety features such as panic alerts, location sessions, and safety check-ins.
