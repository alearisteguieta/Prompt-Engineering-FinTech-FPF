# Breakdown Problem Structure

## Central Objective

Develop a system that combines account aggregation (Mint) with automated investment advisory (Betterment).[[5]](https://www.notion.so/Breakdown-Structure-Task-279a56ae5817809fb32ac99177639cc1?pvs=21)

---

## Decomposition

| Step | Component | Key Functional Requirements | Critical Technical/Financial Requirements | Prompt Methodology |
| --- | --- | --- | --- | --- |
| 1 | Architecture | Secure design, APIs, DB schemas | Plaid API, OAuth 2.0, Encryption, PCI DSS | Strategic Architecture Prompt |
| 2 | Backend (Logic) | Categorization engine, budget, investment algorithms | MPT, Tax-Loss Harvesting, inflation‑adjusted projections | Financial Logic Prompts |
| 3 | Frontend/UI | Data visualization (performance, expenses, goals) | React (responsive), notifications, state management | Frontend Prompts |
| 4 | Integration/Security | Security implementation | MFA/Biometrics, E2E Encryption, HSM, Fraud Detection | Security Implementation Prompts |

---

## Methodology Requirements

- Strict use of the Financial Prompt Framework (FPF).
- Application of the Multi‑Layer Prompt Strategy (MPF).
- Exhaustive documentation and modular organization for GitHub readiness.[[6]](https://www.notion.so/Breakdown-Structure-Task-279a56ae5817809fb32ac99177639cc1?pvs=21)

---

## Prompt Development Timeline (Recommended)

1–2. Architecture and Data

- Execute the Master Architecture Prompt (Layer 1) and the DB schema details first. Do not skip this step. These outputs are inputs for downstream prompts.

3–5. Backend Logic

- Run Layer 2 prompts for the financial algorithms.
- Order matters: MPT → Tax‑Loss Harvesting, because TLH depends on portfolio allocation.

6–7. Critical Security

- Execute the Security Implementation Prompt early (FinTech requires “security‑first”, not “at the end”).

8–9. QA and Frontend

- Generate tests for validation and then implement/adjust the UI components.
1. Deployment
- Infrastructure prompt for CI/CD and environment preparation.[[7]](https://www.notion.so/Breakdown-Structure-Task-279a56ae5817809fb32ac99177639cc1?pvs=21)

---

## Critical Sequential Processes

- Architectural Design → Financial Logic
    - The MPT and TLH modules depend on the data models from Layer 1. The output of Prompt 1 (architecture and schema) must be an explicit input for Prompt 2 (MPT algorithm).[[8]](https://www.notion.so/Breakdown-Structure-Task-279a56ae5817809fb32ac99177639cc1?pvs=21)
- Financial Logic → Validation and Stress Testing
    - Validation is as important as the algorithm itself. Immediately follow MPT with the Test Generator (Prompt 6) to produce unit and scenario tests for known cases.[[9]](https://www.notion.so/Breakdown-Structure-Task-279a56ae5817809fb32ac99177639cc1?pvs=21)
- Data Security → Compliance
    - After implementing MFA/encryption (Prompt 5), generate a PCI DSS audit checklist that maps implemented controls to evidence (logs, key handling, secrets storage).[[10]](https://www.notion.so/Breakdown-Structure-Task-279a56ae5817809fb32ac99177639cc1?pvs=21)

---

## Notes for the Portfolio Repository

- This document is a concise, public summary aligned with the full project documentation.
- For extended artifacts and end‑to‑end traceability, refer to the “Complete Documentation” link in the README.
