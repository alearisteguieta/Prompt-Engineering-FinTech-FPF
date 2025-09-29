from future import annotations
from typing import Dict, Tuple
import numpy as np
import pandas as pd
from scipy.optimize import minimize
--- Configuration Constants ---
ANNUALIZATION_FACTOR = 252  # trading days/year
RISK_FREE_RATE = 0.02       # annual risk-free rate (2%)
def _annualize(mu_daily: pd.Series, cov_daily: pd.DataFrame) -> Tuple[pd.Series, pd.DataFrame]:
"""
Annualize daily mean returns and covariance.
"""
mu_annual = mu_daily * ANNUALIZATION_FACTOR
cov_annual = cov_daily * ANNUALIZATION_FACTOR
return mu_annual, cov_annual
def portfolio_metrics(
weights: np.ndarray,
mu_daily: pd.Series,
cov_daily: pd.DataFrame,
) -> Tuple[float, float, float]:
"""
Returns (annual_return, annual_volatility, sharpe_ratio) for given weights,
using daily stats and annualizing internally.
"""
w = np.asarray(weights, dtype=float)
mu_a, cov_a = _annualize(mu_daily, cov_daily)
annual_return = float(np.sum(mu_a * w))
annual_volatility = float(np.sqrt(w.T @ cov_a @ w))
sharpe_ratio = (annual_return - RISK_FREE_RATE) / (annual_volatility + 1e-12)
return annual_return, annual_volatility, sharpe_ratio
def _neg_sharpe(
weights: np.ndarray,
mu_daily: pd.Series,
cov_daily: pd.DataFrame,
) -> float:
return -portfolio_metrics(weights, mu_daily, cov_daily)[2]
def _port_vol(
weights: np.ndarray,
mu_daily: pd.Series,
cov_daily: pd.DataFrame,
) -> float:
return portfolio_metrics(weights, mu_daily, cov_daily)[1]
def optimize_portfolio(returns_df: pd.DataFrame) -> Dict[str, Dict[str, object]]:
"""
Modern Portfolio Theory optimization (Max Sharpe and Min Vol).
Input: daily returns for each asset (DataFrame with columns as tickers).
Output: dict with metrics and weights for both portfolios.
"""
if returns_df.empty:
raise ValueError("Input returns DataFrame cannot be empty.")
num_assets = returns_df.shape[1]
mu_daily = returns_df.mean()
cov_daily = returns_df.cov()
constraints = ({"type": "eq", "fun": lambda w: np.sum(w) - 1.0},)
bounds = tuple((0.0, 1.0) for _ in range(num_assets))
w0 = np.full(shape=(num_assets,), fill_value=1.0 / num_assets, dtype=float)
1) Max Sharpe
res_max = minimize(
_neg_sharpe,
w0,
args=(mu_daily, cov_daily),
method="SLSQP",
bounds=bounds,
constraints=constraints,
)
2) Min Vol
res_min = minimize(
_port_vol,
w0,
args=(mu_daily, cov_daily),
method="SLSQP",
bounds=bounds,
constraints=constraints,
)
w_max = res_max.x
w_min = res_min.x
m_max = portfolio_metrics(w_max, mu_daily, cov_daily)
m_min = portfolio_metrics(w_min, mu_daily, cov_daily)
assets = returns_df.columns.tolist()
return {
"max_sharpe": {
"return": m_max[0],
"volatility": m_max[1],
"sharpe_ratio": m_max[2],
"weights": dict(zip(assets, np.round(w_max, 4))),
},
"min_volatility": {
"return": m_min[0],
"volatility": m_min[1],
"sharpe_ratio": m_min[2],
"weights": dict(zip(assets, np.round(w_min, 4))),
},
}
def run_mpt_example(seed: int = 42) -> None:
"""
Generates mock daily returns for 4 assets and runs the optimizer.
Keeps output human-readable for the portfolio repo.
"""
np.random.seed(seed)
assets = ["SPY", "QQQ", "GLD", "BND"]
data = {
a: np.random.normal(loc=0.0005, scale=0.015, size=100)
for a in assets
}
returns_df = pd.DataFrame(data)
print("--- Mock Daily Returns Data (head) ---")
print(returns_df.head())
try:
results = optimize_portfolio(returns_df)
print("n✅ Optimization Complete.")
print("n--- Max Sharpe Ratio Portfolio ---")
max_s = results["max_sharpe"]
print(f"Annualized Return: {max_s['return']:.2%}")
print(f"Annualized Volatility: {max_s['volatility']:.2%}")
print(f"Sharpe Ratio: {max_s['sharpe_ratio']:.4f}")
print("Asset Weights:")
for a, w in max_s["weights"].items():
print(f"  {a}: {w:.2%}")
print("n--- Minimum Volatility Portfolio ---")
min_v = results["min_volatility"]
print(f"Annualized Return: {min_v['return']:.2%}")
print(f"Annualized Volatility: {min_v['volatility']:.2%}")
print(f"Sharpe Ratio: {min_v['sharpe_ratio']:.4f}")
print("Asset Weights:")
for a, w in min_v["weights"].items():
print(f"  {a}: {w:.2%}")
except ValueError as e:
print(f"Error during optimization: {e}")
if name == "main":
run_mpt_example()
