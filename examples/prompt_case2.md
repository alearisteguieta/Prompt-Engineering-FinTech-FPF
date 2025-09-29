# Prompt Case 2 — Financial Logic (Layer 2 Development)

## Context and Purpose

This prompt drives Layer 2 (Financial Logic), generating the core investment engine capabilities based on Layer 1 outputs. It explicitly depends on:

- `docs/Base_DB_Schema.sql` for entities such as `portfolio_holdings` and `users` (risk_profile)
- `docs/API_Specifications.yaml` for endpoint contracts (e.g., `/portfolio/optimization`)

The execution order follows the project’s recommended sequence: Architecture and Data → Backend Logic (MPT → TLH) → Security → Testing.[[4]](https://www.notion.so/Breakdown-Structure-Task-279a56ae5817809fb32ac99177639cc1?pvs=21)

## The Financial Logic Prompt (MPT/TLH Module)

This prompt targets a Quantitative Asset Manager role to produce robust, well‑commented Python code.

```
ROLE
Act as a Senior Quantitative Asset Manager and Robo‑Advisory Expert with strong Python (NumPy/Pandas/SciPy) and portfolio optimization expertise.

OBJECTIVE
Generate a self‑contained Python module (mpt_[engine.py](http://engine.py)) that implements:
1) Modern Portfolio Theory (MPT): Max Sharpe and Min Vol portfolios
2) Tax‑Loss Harvesting (TLH): loss detection and compliant replacement suggestion

CRITICAL SEQUENTIAL INPUTS (from Layer 1)
- DB Schema: Use Base_DB_Schema.sql as the source of truth for inputs (portfolio_holdings for assets and cost basis; users for risk_profile).
- API Contract: Ensure outputs are compatible with /portfolio/optimization in API_Specifications.yaml (OptimizationRequest and OptimizationResult).

FINANCIAL LOGIC REQUIREMENTS
MPT
- Compute efficient frontier via convex optimization.
- Return both Maximum Sharpe and Minimum Volatility portfolios.
- Map risk_profile (Conservative, Moderate, Aggressive) to reasonable target allocations.

TLH
- Analyze cost_basis vs current price for each holding.
- Flag assets with loss > 5% and propose a replacement that is not "substantially identical" (wash‑sale compliant simulation).

TECHNICAL REQUIREMENTS AND OUTPUTS
- Language: Python 3.10+ with NumPy, Pandas, SciPy
- Deliverables:
  a) mpt_[engine.py](http://engine.py): Contains MPT optimization functions and TLH helper logic, with docstrings and input validation
  b) Sample JSON Output: Must conform to OptimizationResult schema (see below)
- Performance/Robustness:
  - Deterministic seeds for examples
  - Input validation and explicit error messages
  - Clear typing and comments for portfolio code review

CONFIRMATION MESSAGE
"Layer 2 Financial Logic implemented: ready for validation tests."
```

## Sample JSON Output (OptimizationResult‑compatible)

This example mirrors the structure referenced by `/portfolio/optimization` in `API_Specifications.yaml`.

```json
{
  "request_id": "req_12345",
  "status": "Complete",
  "optimal_weights": {
    "SPY": 0.42,
    "QQQ": 0.28,
    "GLD": 0.18,
    "BND": 0.12
  }
}
```

Notes

- The repository provides an executable example in `examples/mpt_[engine.py](http://engine.py)` implementing MPT (Max Sharpe and Min Vol) with consistent annualization and type hints. TLH can be implemented as a helper using cost basis and current price inputs.[[5]](https://raw.githubusercontent.com/alearisteguieta/Prompt-Engineering-FinTech-FPF/main/examples/mpt_engine.py)
- Testing for Layer 2 is summarized in `testing_validation` (weights sum to 1, no NaNs; contract checks; simulated latency for categorization).[[6]](https://github.com/alearisteguieta/Prompt-Engineering-FinTech-FPF.git)

## Deliverables (Layer 2)

- `examples/mpt_[engine.py](http://engine.py)` (MPT reference implementation)
- TLH helper outline integrated in the prompt and referenced for further extension
- Sample output aligned with `API_Specifications.json`
