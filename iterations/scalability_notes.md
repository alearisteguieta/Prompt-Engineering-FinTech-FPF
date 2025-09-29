# Scalability Notes — Portfolio View

Purpose

- Summarize practical avenues to scale the architecture described in docs/System_[Architecture.md](http://Architecture.md) for a production path, without exposing internal details.[[6]](https://raw.githubusercontent.com/alearisteguieta/Prompt-Engineering-FinTech-FPF/main/assets/diagrams.md)

Key focus areas

- Fraud detection evolution
    - Start with a statistical Z‑Score anomaly check, then consider Isolation Forest for robustness.
    - Centralize features and thresholds, log decisions for auditability.
- Real‑time API integrations
    - Idempotent ingestion for bank data.
    - Backpressure and retries with DLQs on transient failures.
- Terraform + CI/CD
    - Minimal modules for VPC, RDS (PostgreSQL), Secrets Manager/Vault.
    - CI pipeline: lint, unit tests, SAST, and artifact publishing.
- Observability and SLOs
    - Golden signals on gateway and ML service.
    - Budget latency: p95 < 500 ms for categorization paths.
    - Error budgets mapped to on‑call and rollout policies.

Notes

- This section reflects portfolio‑level direction, not a full infra blueprint. See the complete documentation link in the README for extended materials.
