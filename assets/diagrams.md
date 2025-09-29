# Architecture Diagram (Mermaid, Portfolio View)

This diagram summarizes the Master FPF Architecture described in the documentation, emphasizing security-by-design, Zero Trust, and the non-functional targets defined for this project. It is intentionally concise for a portfolio repository; the full version and extended annotations are available in the complete documentation link in the README.[[4]](https://www.notion.so/Multi-Layer-Prompt-Structure-ZeTheta-Inter-279a56ae581780feba1aeea55bbace5b?pvs=21)[[5]](https://www.notion.so/Breakdown-Structure-Task-279a56ae5817809fb32ac99177639cc1?pvs=21)

Key Notes

- Non-functional targets:
    - SLA: 99.99% uptime for core backend services
    - Expense Categorization ML: p95 latency under 500 ms
- Security and compliance:
    - OAuth 2.0 on the gateway with MFA enforcement for sensitive actions
    - AES‑256 at rest for sensitive fields
    - Secrets in AWS Secrets Manager or HashiCorp Vault, with HSM-backed keys
    - Zero Trust network segmentation (VPC, SGs)
- Reference endpoints (summary):
    - POST /users/register
    - POST /accounts/link
    - GET /transactions
    - POST /portfolio/optimization
    - GET /recommendations

```mermaid
flowchart TD

%% === Clients and Edge ===
Client["Clients\n(Web / Mobile)"] -->|HTTPS| APIGW["API Gateway\nOAuth 2.0 + MFA\nRate Limit"]

%% === Core Microservices ===
subgraph Core["Microservices Layer"]
  direction TB
  UserSvc["User Service\n(Bcrypt, PII ops)"]
  AccountAgg["Account Aggregation\n(Plaid Link)"]
  TxSvc["Transaction Service\n(CRUD, ML hook)"]
  InvestSvc["Investment Portfolio\n(MPT, TLH)"]
  RecoSvc["Recommendation Engine"]
  NotifSvc["Notification Service"]
end

APIGW --> Core

%% === ML Service ===
subgraph ML["ML Service"]
  ExpenseML["Expense Categorization Engine\n(p95 < 500 ms)"]
end

TxSvc -->|categorize| ExpenseML
ExpenseML -->|category| TxSvc

%% === Data Stores ===
subgraph Data["Data Stores"]
  PG["PostgreSQL Cluster\n(AES-256 for sensitive fields)"]
  Redis["Redis Cache / Rate Limiter"]
  S3["Object Storage (S3)\nPlaid raw, models, audit logs"]
end

Core --> PG
Core --> Redis
AccountAgg --> S3

%% === Core Financial Logic (logical subcomponents) ===
subgraph Quant["Core Financial Logic"]
  MPT["Modern Portfolio Theory\n(Max Sharpe, Min Vol)"]
  TLH["Tax-Loss Harvesting\n(Cost basis aware)"]
end

InvestSvc --> Quant
Quant --> PG

%% === External Integrations ===
subgraph Ext["External Integrations"]
  Plaid["Plaid API"]
  Mkt["Market Data Providers"]
  EmailSMS["Email / SMS Provider"]
end

AccountAgg -->|Link Flow| Plaid
InvestSvc --> Mkt
NotifSvc --> EmailSMS

%% === Security & Infrastructure ===
subgraph Sec["Security & Infrastructure (Zero Trust)"]
  LB["Load Balancers"]
  VPC["VPC / Segmentation"]
  Secrets["Secrets Manager / Vault"]
  Obs["Observability\n(Logs / Metrics / Traces)"]
  HSM["HSM / KMS-backed keys"]
end

APIGW --> LB
LB --> Core
Core --> VPC

Secrets -->|DB creds, Plaid tokens| Core
Secrets --> PG
Secrets --> AccountAgg
HSM --> Secrets
Obs --> Core

%% === Endpoint Annotations (reference only) ===
subgraph API["API (reference endpoints)"]
  E1["POST /users/register"]
  E2["POST /accounts/link"]
  E3["GET /transactions"]
  E4["POST /portfolio/optimization"]
  E5["GET /recommendations"]
end

APIGW -.-> API

%% === Non-functional targets ===
SLA[/"SLA: 99.99% uptime"/]
LAT[/"p95: Categorization < 500 ms"/]
SLA -.-> APIGW
LAT -.-> ExpenseML
```

Export tip

- To include a static image in docs/System_[Architecture.md](http://Architecture.md), export this Mermaid diagram as PNG and save it as assets/diagrams.png. Then link to it from System_[Architecture.md](http://Architecture.md) so readers can see the visual without Mermaid rendering support.[[6]](https://raw.githubusercontent.com/alearisteguieta/Prompt-Engineering-FinTech-FPF/main/docs/System_Architecture.md)
