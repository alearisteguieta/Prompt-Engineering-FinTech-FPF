# Architecture Diagram (Mermaid)

The diagram below represents the **Master FPF Architecture** described in the project documents:
- Microservices architecture (API Gateway, core services)
- ML service for expense categorization
- Data stores (Postgres, Redis, Object Storage)
- External integrations (Plaid, market data, email/SMS)
- Security & infrastructure components (Load Balancers, VPC, Secrets Manager, Observability)
- Core financial logic components (MPT, Tax-Loss Harvesting)

> Notes: SLA and performance targets are documented in the project materials:
> - **99.99% uptime** for main backend services.
> - Expense Categorization ML: **95% of transactions < 500 ms** inference goal.

```mermaid
flowchart TD
  %% Clients and Edge
  Clients["Clients\n(Web / Mobile App)"] -->|HTTPS| APIGW["API Gateway\n(Auth, Rate Limit)"]

  %% Core Microservices
  subgraph CoreServices [Microservices Layer]
    direction TB
    UserSvc["User Service"]
    AccountAgg["Account Aggregation Service\n(Plaid)"]
    TransactionSvc["Transaction Service"]
    InvestmentSvc["Investment Portfolio Service"]
    RecommendationSvc["Recommendation Engine"]
    NotificationSvc["Notification Service"]
  end

  APIGW --> CoreServices

  %% ML Service
  subgraph MLService [Machine Learning Service]
    ExpenseML["Expense Categorization Engine\n(ML)"]
  end

  TransactionSvc -->|categorization request| ExpenseML
  ExpenseML -->|category result| TransactionSvc

  %% Data Stores
  subgraph DataStores [Data Stores]
    Postgres["PostgreSQL Cluster\n(AES-256 for sensitive fields)"]
    Redis["Redis Cache / Rate Limiter"]
    S3["Object Storage (S3)\nPlaid raw data, model artifacts, audit logs"]
  end

  CoreServices --> Postgres
  CoreServices --> Redis
  AccountAgg --> S3

  %% Core Financial Logic (logical components inside Investment Service)
  subgraph CoreFinancial [Core Financial Logic]
    MPT["Modern Portfolio Theory\nEngine"]
    TLH["Tax-Loss Harvesting\nEngine"]
  end

  InvestmentSvc --> CoreFinancial
  CoreFinancial --> Postgres

  %% External Integrations
  subgraph External [External Integrations]
    Plaid["Plaid API"]
    MarketData["Market Data Providers"]
    EmailSMS["Email / SMS Provider"]
  end

  AccountAgg -->|Plaid Link Flow| Plaid
  InvestmentSvc --> MarketData
  NotificationSvc --> EmailSMS

  %% Security & Infra
  subgraph SecurityInfra [Security & Infrastructure]
    LB["Load Balancers"]
    VPC["VPC / Network Segmentation"]
    Secrets["Secrets Manager / HashiCorp Vault"]
    Observability["Observability\n(Logging / Monitoring / Tracing)"]
    HSM["HSM / Key Management"]
  end

  APIGW --> LB
  LB --> CoreServices
  CoreServices --> VPC
  Secrets -->|stores: Plaid tokens, DB creds| CoreServices
  Secrets --> Postgres
  Secrets --> AccountAgg
  Observability --> CoreServices
  HSM --> Secrets

  %% Annotations
  SLA[/"SLA: 99.99% uptime for main backend services"/]
  LAT[/"Latency goal: Expense Categorization — 95% < 500 ms"/]

  SLA -.-> APIGW
  LAT -.-> ExpenseML
