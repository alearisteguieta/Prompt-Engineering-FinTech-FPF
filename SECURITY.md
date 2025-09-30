# Security Policy

We take security seriously. Please follow these guidelines when reporting vulnerabilities.

Supported Scope (Portfolio Repo)

- This repository is a portfolio‑style summary. It contains documentation, examples, and lightweight tests. There are no production secrets, credentials, or live infrastructure here.
- Security reports should focus on: exposed secrets (if any), credential leaks, unsafe example patterns, or documentation that could lead to misuse.

Reporting a Vulnerability

- Please do not open a public Issue for security reports.
- Contact the maintainer privately:
    - Email: [aristeguieta88@gmail.com](mailto:aristeguieta88@gmail.com)
    - Or open a blank Issue titled “Security Report” asking for a private contact channel (no details in public).
- Include:
    - A clear description of the issue and potential impact
    - Repro steps or PoC (if applicable)
    - Suggested remediation (if you have one)

Response Expectations

- Acknowledge receipt within 72 hours
- Initial assessment within 7 days
- Coordinated disclosure if applicable (we’ll agree on timing)

Out of Scope (for this portfolio)

- Denial‑of‑service against this static repository
- Vulnerabilities in third‑party platforms (GitHub, GitHub Pages, etc.)
- Hypothetical flaws without a concrete scenario or impact

Secrets and Sensitive Data

- This repo must not contain credentials or sensitive data. If you find any, report immediately so we can revoke and rotate.

Remediation

- We will fix issues by updating code samples, docs, or removing unsafe patterns. Where needed, we’ll add notes clarifying secure usage in production contexts.

