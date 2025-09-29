# Personal Wealth Management LLM Orchestration (FinTech Prompt Engineering)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Technology: Python](https://img.shields.io/badge/Python-3.10%2B-blue)]()
[![Methodology: FPF](https://img.shields.io/badge/Methodology-FPF%20%2B%20MultiLayer-orange)]()
[![Status: Internship Project](https://img.shields.io/badge/Status-Completed%20(ZeTheta)-informational)]()

# 🏦 Prompt Engineering Project – Personal Wealth Management App (Mint + Betterment)

## 📌 Executive Summary

- This repository contains my first **Prompt Engineering project**, developed during my internship at **ZeTheta Algorithm Private Limited**.  
- The project demonstrates the application of advanced prompt engineering methodologies to design a **personal wealth management system** that integrates
- **multi-bank account aggregation (Mint)** with **automated investment advice (Betterment)**
---

## 🔎 Repository Scope

- This repository is a condensed, portfolio-style version of the full "Personal Wealth Management App (Mint + Betterment)" project. Its goal is to showcase the architecture, prompt methodology (FPF + Multi-Layer), and key artifacts in a concise manner.

* Contents: curated excerpts, examples, and essential specifications.
* Full Content: detailed documentation, full prompts, end-to-end traceability, tests, and results.
* To review the full project documentation, visit:
[[Full Documentation](https://alearisteguieta.github.io/Prompt-Engineering-FinTech-FPF/)]
* Notes:
- This repository does not include sensitive data or credentials.
- Some sections have been simplified for space, privacy, and pedagogical clarity.


## 🎯 Objectives
- Apply the **Breakdown Problem Structure** to decompose a FinTech system into manageable components.
- Implement the **Financial Prompt Framework (FPF)** and the **Multilayer Prompt Strategy (MPF)** to ensure compliance, scalability, and traceability.
- Deliver a **complete and documented repository** as a professional and educational reference.  

---

## 🧩 Methodology
The project follows a strict **prompt architecture sequence**  
1. **Meta Prompt**  
2. **Financial Prompt Framework (FPF)**  
3. **Multilayer Prompt Strategy (MPF)**  

### Breakdown Problem Structure
- **Step 1 – Architecture**: secure design, APIs, DB schemas.  
- **Step 2 – Backend Logic**: categorization engine, budget, investment algorithms.  
- **Step 3 – Frontend/UI**: financial data visualization, mobile design.  
- **Step 4 – Integration/Security**: MFA, encryption, fraud detection.  

### Multilayer Prompt Strategy
- **Layer 1 – Strategic Prompts**: Define architecture, schemas, APIs.  
- **Layer 2 – Development Prompts**: Generate MPT, Categorization, Tax-Loss modules.  
- **Layer 3 – Refinement Prompts**: Implement security, generate tests, configure deployment.  

---

## 📚 Documentation
- [`/docs/introduction.md`](docs/introduction.md)  
- [`/docs/breakdown_problem_structure.md`](docs/breakdown_problem_structure.md)  
- [`/docs/multilayer_prompt_strategy.md`](docs/multilayer_prompt_strategy.md)  

---

## 🧪 Testing & Iterations
Validation and iterative improvements are documented in:  
- [`/testing_validation`](testing_validation/)  
- [`/iterations`](iterations/)  

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
```

## 📂 Repository Structure

```bash
📂 Prompt-Engineering-Project
┣ 📜 README.md
┣ 📂 docs
┃ ┣ 📜 introduction.md
┃ ┣ 📜 breakdown_problem_structure.md
┃ ┗ 📜 multilayer_prompt_strategy.md
┣ 📂 examples
┃ ┣ 📜 prompt_case1.md
┃ ┣ 📜 prompt_case2.md
┃ ┗ 📜 generated_outputs.md
┣ 📂 testing_validation
┃ ┣ 📜 test_plan.md
┃ ┣ 📜 validation_results.md
┃ ┗ 📜 unit_tests.py
┣ 📂 iterations
┃ ┣ 📜 v1_initial.md
┃ ┣ 📜 v2_refined.md
┃ ┗ 📜 scalability_notes.md
┗ 📂 assets
  ┗ 📜 diagrams.png
```
