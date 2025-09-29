# Design Evolution — v2 (Refined)

What changed

- Compliance and security
    - PCI DSS scope minimization clarified.
    - OAuth 2.0 on gateway with MFA enforcement for sensitive flows.
    - AES‑256 at rest for sensitive fields; secrets in Vault/KMS with HSM‑backed keys.
- Financial logic validation
    - MPT example plus TLH criteria outlined.
    - Unit tests and simulated latency checks added in testing_validation/.
- Structure and artifacts
    - docs/ now includes System_[Architecture.md](http://Architecture.md), API_Specifications.yaml, Base_DB_Schema.sql.
    - examples/ demonstrates MPT and Categorization Engine with sub‑500 ms p95 focus.

Outcome

- The portfolio now shows a coherent path from initial concept to a refined, security‑aware design with lightweight validation.
