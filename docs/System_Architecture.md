# System Architecture Design (Layer 1 Deliverable)

## 📌 Context and Vision

This document details the secure, scalable, and compliant Microservices architecture for the Personal Wealth Management Application ("Mint + Betterment" type). This design is the direct output of the **Strategic Architecture Prompt (Layer 1)**, establishing the foundational requirements for all subsequent generated code modules (Layer 2).

The core philosophy of this architecture is **Security-by-Design**, adhering to FinTech best practices, including **PCI DSS** standards and **Zero Trust** principles.

---

## 🏗️ Architectural Pattern: Microservices

The application is decomposed into loosely coupled services communicating via an **API Gateway**, ensuring modularity, independent deployment, and fault tolerance.

| Microservice | Core Functionality | Key Technology |
| :--- | :--- | :--- |
| **API Gateway** | Authentication (OAuth 2.0), Rate Limiting, Request Routing, MFA enforcement. | Flask / Django |
| **User Service** | User registration, profile management, credentials (using Bcrypt hashing). | PostgreSQL |
| **Account Aggregation Service** | Secure integration with **Plaid API** for multi-bank data fetching and token management. | Python |
| **Transaction Service** | CRUD operations for financial transactions, linking to the ML Categorization Engine. | PostgreSQL / Redis |
| **Investment Portfolio Service** | Executes core financial logic (MPT Engine, Tax-Loss Harvesting, Projections). | Python (NumPy/Pandas) |
| **Recommendation Engine** | Generates personalized investment and budget advice. | Python / ML |
| **Notification Service** | Handles alerts via Email/SMS/Push for critical events (e.g., fraud, SLA breach). | Python |

---

## 🔒 Security and Compliance Implementation

Security is a primary focus, reflecting the **Financial Prompt Framework (FPF)** requirements.

### Data Security
* **Encryption at Rest:** Sensitive data (passwords, social security data, full transaction details) must be stored using **AES-256 encryption**. Database fields containing critical data must be explicitly marked for encryption.
* **Key Management:** Cryptographic master keys are stored securely in a dedicated **Secrets Manager (HashiCorp Vault/AWS HSM)**, ensuring separation of concerns from the application server.
* **Hashing:** User passwords and API keys are stored using **Bcrypt** for one-way hashing.

### Access Control
* **Zero Trust Networking:** Network segmentation (VPC) is mandated, ensuring that services can only communicate with required dependencies (e.g., the Investment Service cannot directly access the User Service's full database tables).
* **Authentication:** **OAuth 2.0** for client authorization and **Multi-Factor Authentication (MFA)** enforced for all critical requests.

---

## 🚀 Non-Functional Requirements (NFRs)

The architecture is designed to meet strict FinTech operational metrics:

| Metric | Requirement | Component Focus |
| :--- | :--- | :--- |
| **Availability (SLA)** | **99.99% Uptime** (main backend) | Load Balancing, redundancy across core Microservices, and database clustering. |
| **Performance (Latency)** | **< 500 ms** (95% of transactions) | Expense Categorization Engine (ML). Use of **Redis Cache** for frequently accessed data (e.g., market prices). |
| **Scalability** | Horizontal scaling via containerization (Docker/Kubernetes). Stateless design for most services. | Load Balancers, PostgreSQL Read Replicas. |

---

## 🔗 Technology Stack Summary

| Layer | Technologies | Purpose |
| :--- | :--- | :--- |
| **Backend** | Python (3.10+), Flask/Django, NumPy, Pandas | Core logic, MPT, Tax-Loss Harvesting, API serving. |
| **Database** | PostgreSQL | Primary data store, chosen for ACID compliance and geospatial/JSON support. |
| **Caching/Messaging** | Redis | Session management, rate limiting, and temporary data caching. |
| **ML/Data** | Scikit-learn / TensorFlow, AWS S3 | Expense Categorization Model and artifact storage. |
| **Integration** | Plaid API | Bank account and transaction aggregation. |

For the visual representation, please refer to the image: **`assets/diagrams.png`**.
