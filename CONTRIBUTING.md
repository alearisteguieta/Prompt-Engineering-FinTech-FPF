# Contributing

Thanks for your interest in contributing! This repository is a portfolio‑style summary of a larger FinTech project. 
We welcome improvements that keep the scope concise, safe, and easy to review.

## How to propose changes

- Open an Issue describing the problem or proposal
- Fork the repo and create a feature branch: feature/<short‑name>
- Submit a Pull Request referencing the Issue and checklist below

## Scope guidelines

- Keep changes aligned with the portfolio focus:
    - Docs: clarity, alignment with FPF + Multi‑Layer methodology
    - Examples: small, self‑contained, easy to run
    - Tests: lightweight and deterministic
- No secrets, credentials, or sensitive data
- Avoid expanding beyond the summarized scope; link out to full docs if needed

## Code style

- Python: type hints where helpful, docstrings, black/flake8 style
- Markdown: wrap at ~100 chars, use headings and lists for scanability
- Filenames and links must match exactly (e.g., API_Specifications.yaml)

## Tests

- Add or update tests in testing_validation/ when relevant
- Ensure unit_[tests.py](http://tests.py) passes locally
- Prefer deterministic data and seeded randoms for examples

## Branching and commits

- Branches: feature/<name>, fix/<name>, docs/<name>
- Commits: clear, imperative mood; reference Issues if applicable

## PR checklist

- [ ]  Changes align with portfolio scope
- [ ]  Docs updated (if needed)
- [ ]  Tests added/updated and passing
- [ ]  No secrets or sensitive info introduced

## Security

If you discover a vulnerability, please do not open a public Issue. Email the maintainer (see repo profile) or follow [SECURITY.md](http://SECURITY.md).

## Code of Conduct

By participating, you agree to abide by our CODE_OF_[CONDUCT.md](http://CONDUCT.md).
