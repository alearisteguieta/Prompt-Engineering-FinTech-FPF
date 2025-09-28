# Prompt Case 2 – Financial Logic (Layer 2 Development)

## 📌 Context and Purpose
This document contains the complete and exact prompt used for the **Layer 2: Financial Logic** phase, specifically targeting the core investment engine module. This prompt is executed sequentially, relying directly on the `Base_DB_Schema.sql` and `API_Specifications.yaml` output from **Prompt 1 (Layer 1)** to ensure data consistency and API integration readiness.

## 🧱 The Financial Logic Prompt (MPT/TLH Module)
This prompt targets a **Quantitative Asset Manager** role to generate production-ready financial algorithms in Python.

```bash
ROLE: Act as a Senior Quantitative Asset Manager and Robo-Advisory Expert, specialized in high-frequency trading mathematics and Python implementation (NumPy/Pandas/SciPy).

OBJECTIVE: Generate a complete, functional, and well-commented Python module (investment_engine.py) that implements the core financial logic: Modern Portfolio Theory (MPT) and Tax-Loss Harvesting (TLH).

CRITICAL SEQUENTIAL INPUTS (From Layer 1)
DB Schema: The module MUST utilize the schema defined in Base_DB_Schema.sql. Specifically, reference portfolio_holdings for assets and users for the risk_profile.

API Endpoint: The output MUST integrate the logic to be exposed via the /portfolio/optimization endpoint defined in API_Specifications.yaml.

FINANCIAL LOGIC REQUIREMENTS
Modern Portfolio Theory (MPT) Implementation:

Develop a function to calculate the Efficient Frontier using Monte Carlo simulation and/or convex optimization techniques.

Identify and return the Maximum Sharpe Ratio portfolio and the Minimum Volatility portfolio.

Generate the optimal asset weights for a given client based on their defined risk_profile (Conservative, Moderate, Aggressive).

Tax-Loss Harvesting (TLH) Implementation:

Create a function that analyzes the cost_basis in portfolio_holdings.

Identify assets with a significant loss (>5%) and propose a replacement asset that is not "substantially identical" (Wash Sale Rule compliant simulation).

TECHNICAL REQUIREMENTS AND OUTPUT
Language/Framework: Production-ready Python (using recommended libraries like Pandas, NumPy, or specialized FinTech packages).
Deliverables:

investment_engine.py: Complete, documented Python file containing MPT and TLH logic.

Sample Output: Provide an example JSON output matching the OptimizationResult schema from the API specification.

CONFIRMATION MESSAGE: "Layer 2 Financial Logic 95% implemented 🧪: Ready for Stress Testing."
```

## ✅ Deliverables Generated (Layer 2)

The execution of the prompt above resulted in the following functional code module:

* `investment_engine.py` (Functional MPT and TLH logic module)
```eof
