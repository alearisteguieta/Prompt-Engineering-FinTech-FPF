# Multilayer Prompt Strategy

This document summarizes the layered prompt methodology used to design and validate the Personal Wealth Management system (Mint + Betterment), aligned with the Financial Prompt Framework (FPF) and the portfolio scope of this repository.[^]

## Layer 1 — Strategic (Master)
**Objective**: Define scope, high‑level architecture, and technology stack.  
**Prompt Example**: Master Architecture (FPF).  
**Deliverables**: `System_Architecture.md`, `API_Specifications.yaml`, `Base_DB_Schema.sql`

Scope
- Microservices blueprint with API Gateway and core services
- Key database schemas and security posture (AES‑256 at rest, secrets via Vault/KMS)
- Compliance framing (PCI DSS scope minimization, OAuth 2.0 + MFA)
- Non‑functional targets: SLA 99.99% uptime, ML categorization p95 < 500 ms

## Layer 2 — Development (Intermediate)
**Objective**: Generate coherent financial logic modules based on Layer 1 outputs.  
**Prompts**:
- MPT module (Max Sharpe / Min Vol)
- Expense Categorization Engine (low‑latency focus)
- Tax‑Loss Harvesting module (depends on portfolio allocation)
**Deliverables**: Functional example modules (Python), contracts aligned with API specs

Notes
- MPT precedes TLH to ensure allocation‑aware tax optimization
- Use synthetic datasets and deterministic checks for portfolio examples

## Layer 3 — Refinement (Detail)
**Objective**: Ensure quality, security, testing, and documentation.  
**Prompts**:
- Security Implementation (MFA/WebAuthn, encryption at rest, secrets)
- Test Generation (unit/scenario tests and contract checks)
- AWS/Terraform configuration (portfolio‑level outline)
**Deliverables**: Test scripts, validation results summary, security functions outline

Evidence (portfolio)
- `/testing_validation`: test_plan.md, unit_tests.py, validation_results.md
- Simulated p95 latency checks for categorization path

## Timeline (Recommended Execution Order)
1–2. Architecture and Data  
- Run Master Architecture (Layer 1) and DB schema prompts first. These outputs are inputs for the backend prompts.

3–5. Backend Logic  
- Execute MPT → then TLH (TLH depends on MPT allocation). Add categorization engine.

6–7. Critical Security  
- Implement security early (OAuth 2.0 + MFA, AES‑256, secrets). FinTech is security‑first, not security‑last.

8–9. QA and Frontend  
- Generate tests and then implement/adjust UI components.

10. Deployment  
- CI/CD and environment preparation (outline via Terraform/AWS).

## Portfolio Scope Notes
- This is a condensed, public summary aligned with the full documentation.  
- For extended prompts, end‑to‑end traceability, and complete artifacts, see the “Complete Documentation” link in the repository README.
