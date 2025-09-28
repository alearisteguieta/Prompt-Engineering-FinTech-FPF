# Prompt Case 1 – Strategic Architecture (Layer 1 Master FPF)

## 📌 Context and Purpose
This document contains the complete and exact Master FPF Architecture Prompt used to generate the project's key structural deliverables (Database Schema, API Specification, and System Architecture). This prompt is the foundation of the Multilayer Prompt Strategy (Layer 1), establishing all non-functional requirements (SLA, Security, Compliance) for the FinTech application. 

## 🧱 The Strategic Architecture Prompt
This prompt was executed to act as the "Master" prompt, orchestrating the initial design and ensuring strict adherence to the principles of the Financial Prompt Framework (FPF).

```bash
**ROLE:** Act as a Senior FinTech Architect, expert in building high-performance Robo-Advisory systems (Trading/ML) and strict regulatory compliance (PCI DSS, Zero Trust, OAuth 2.0).

**OBJECTIVE:** Design a complete, secure, and scalable Microservices architecture for a Personal Wealth Management application (Mint + Betterment).

---

## STRATEGIC REQUIREMENTS (FPF)

1. **Security/Availability Metric (SLA):** The architecture must guarantee **99.99% uptime** for the main backend service (investment engine and data aggregation).
2. **Performance Metric (Latency):** The Expense Categorization Engine (ML) must process 95% of incoming transactions in **less than 500 milliseconds**.
3. **Zero Trust Security:** Implement strict network segmentation, with secrets management via **Hashicorp Vault** or **AWS Secrets Manager**, and **AES-256** encryption for data at rest.
4. **Core Financial Logic:** Must include separate modules for **Modern Portfolio Theory (MPT)** and **Tax-Loss Harvesting**.

---

## TECHNICAL REQUIREMENTS AND OUTPUT

**Technologies:** Python (Backend/ML), Flask/Django, PostgreSQL (Main Database), Redis (Cache/Rate Limiting), Plaid API.
**Output Format:** Document structured in **Markdown** (NO code).

The document must include:

1. **Descriptive Microservices Architecture Diagram** (including Gateway, Core Finance Services, ML Service, and Data Store).
2. **Key Database Schemas** (User, Transaction, Recommendation), detailing the *hashing* method (e.g., **Bcrypt**) and encrypted field (**AES-256**) for sensitive fields.
3. **5 Critical RESTful API Endpoints** (Method, URL, Function) for data orchestration.
4. **Compliance Justification (PCI DSS and OAuth 2.0):** Explain the segregation of data responsibilities and how the design avoids the complete *scope* of PCI DSS (Critical justification in FinTech).

**CONFIRMATION MESSAGE:** "Master FPF Architecture 99.99% designed 🛠️: Ready for Layer 2."
```

## ✅ Generated Deliverables (Layer 1)
The execution of the prompt above led to the creation of the following key documents (which should be in the docs/ folder or similar):

* System_Architecture.md

* API_Specifications.yaml (or .json)

* Base_DB_Schema.sql
