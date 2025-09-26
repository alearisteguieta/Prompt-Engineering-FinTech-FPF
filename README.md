# Personal Wealth Management LLM Orchestration (FinTech Prompt Engineering)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Technology: Python](https://img.shields.io/badge/Python-3.10%2B-blue)]()
[![Methodology: FPF](https://img.shields.io/badge/Methodology-FPF%20%2B%20MultiLayer-orange)]()
[![Status: Internship Project](https://img.shields.io/badge/Status-Completed%20(ZeTheta)-informational)]()

## 📌 Executive Summary
This repository showcases my first **Prompt Engineering project** completed during my internship at **ZeTheta Algorithm Private Limited**.  
The project applies advanced **problem breakdown** and **multi-layer prompt strategy** methodologies to build a **personal wealth management application** combining features of Mint (account aggregation) and Betterment (automated investment advice).  

The goal is to demonstrate **best practices in Prompt Engineering** through structured documentation, practical examples, testing validation, and iterative refinement.

---

## 🎯 Objectives
- Apply **Breakdown Problem Structure** to decompose a complex FinTech system into manageable prompt-driven tasks:contentReference[oaicite:3]{index=3}.
- Implement a **Multi-Layer Prompt Framework** to ensure scalability, traceability, and compliance:contentReference[oaicite:4]{index=4}.
- Deliver a **complete, professional repository** that can serve both as a **portfolio piece** and as a **teaching example** in prompt engineering.

---

## 🧩 Methodology

### 1. Problem Breakdown
- Analysis of functional and technical requirements.
- Mapping dependencies across architecture, backend, frontend, and security layers.
- Application of the **Financial Prompt Framework (FPF)** for domain-specific compliance.

### 2. Multi-Layer Prompt Strategy
- **Layer 1 – Strategic Prompts**: Define architecture, database schemas, and APIs.
- **Layer 2 – Development Prompts**: Implement core financial logic (MPT, Tax-Loss Harvesting, Categorization Engine).
- **Layer 3 – Refinement Prompts**: Security, testing, compliance validation, and CI/CD integration.

📄 Full methodology documentation is available in:
- [`/docs/breakdown_problem_structure.md`](docs/breakdown_problem_structure.md)  
- [`/docs/multilayer_prompt_strategy.md`](docs/multilayer_prompt_strategy.md)  

---

## 🧪 Testing & Validation
Testing ensures correctness of prompt outputs and traceability in financial logic:
- [`/testing_validation/test_plan.md`](testing_validation/test_plan.md)  
- [`/testing_validation/validation_results.md`](testing_validation/validation_results.md)  
- Automated scripts (`unit_tests.py`) for reproducibility.

---

## 🌀 Iterations & Scalability
The repository documents project evolution:
- [`v1_initial.md`](iterations/v1_initial.md) → First draft prompts and raw outputs.
- [`v2_refined.md`](iterations/v2_refined.md) → Improved results after structured iterations.
- [`scalability_notes.md`](iterations/scalability_notes.md) → Future roadmap for larger deployments.

---

## 💡 Example: Layer 1 - Strategic Architecture Prompt

This is an excerpt of the initial, high-leverage prompt used to define the project's foundation. It mandates strict technical constraints and verifiable output formats.

```python
fintech_architecture_prompt = """
**ROLE:** Act as a Senior FinTech Architect, expert in building high-performance Robo-Advisory systems (Trading/ML) and strict regulatory compliance (PCI DSS, Zero Trust, OAuth 2.0).

**OBJECTIVE:** Design a complete, secure, and scalable Microservices architecture for a Personal Wealth Management application (Mint + Betterment).

## STRATEGIC REQUIREMENTS (FPF)
1. **Security/Availability Metric (SLA):** The architecture must guarantee **99.99% uptime** for the investment engine.
2. **Performance Metric (Latency):** The Expense Categorization Engine (ML) must process 95% of transactions in **less than 500 milliseconds**.
3. **Zero Trust Security:** Implement network segmentation, Hashicorp Vault/AWS Secrets Manager, and **AES-256** encryption for data at rest.

## TECHNICAL REQUIREMENTS AND OUTPUT
**Technologies:** Python (Backend/ML), Flask/Django, PostgreSQL, Redis, Plaid API.
**Output Format:** Document structured in Markdown (NO code).

The document must include:
1. Descriptive Microservices Architecture Diagram.
2. Key Database Schemas (User, Transaction, Recommendation), detailing hashing (Bcrypt) and encrypted fields (AES-256).
...
"""
