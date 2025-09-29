import numpy as np
import pandas as pd
from scipy.optimize import minimize

# --- Configuration Constants ---
ANNUALIZATION_FACTOR = 252  # Trading days in a year for daily data
RISK_FREE_RATE = 0.02       # Example risk-free rate (2%)

def calculate_portfolio_performance(weights: np.ndarray, mean_returns: pd.Series, cov_matrix: pd.DataFrame) -> tuple[float, float, float]:
    """
    Calculates the expected annual return, volatility, and Sharpe Ratio for a given portfolio.

    Args:
        weights: A NumPy array of asset weights in the portfolio.
        mean_returns: Pandas Series of annualized mean historical returns for assets.
        cov_matrix: Pandas DataFrame of annualized covariance matrix of asset returns.

    Returns:
        A tuple containing (annual_return, annual_volatility, sharpe_ratio).
    """
    # Ensure weights are a NumPy array
    weights = np.array(weights)
    
    # 1. Annualized Portfolio Return
    annual_return = np.sum(mean_returns * weights) * ANNUALIZATION_FACTOR
    
    # 2. Annualized Portfolio Volatility (Standard Deviation)
    annual_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * ANNUALIZATION_FACTOR, weights)))
    
    # 3. Sharpe Ratio
    sharpe_ratio = (annual_return - RISK_FREE_RATE) / annual_volatility
    
    return annual_return, annual_volatility, sharpe_ratio

def negative_sharpe_ratio(weights: np.ndarray, mean_returns: pd.Series, cov_matrix: pd.DataFrame) -> float:
    """
    Optimization function: We minimize the negative Sharpe Ratio to maximize the positive Sharpe Ratio.
    """
    # Note: Only the negative of the Sharpe Ratio is returned for minimization.
    return -calculate_portfolio_performance(weights, mean_returns, cov_matrix)[2]

def portfolio_volatility(weights: np.ndarray, mean_returns: pd.Series, cov_matrix: pd.DataFrame) -> float:
    """
    Optimization function: Returns the portfolio volatility for minimization.
    """
    # Note: Returns the volatility (the second element in the tuple) for minimization.
    return calculate_portfolio_performance(weights, mean_returns, cov_matrix)[1]

def optimize_portfolio(returns_df: pd.DataFrame) -> dict:
    """
    Implements the Modern Portfolio Theory optimization to find the Max Sharpe and Min Volatility portfolios.

    Args:
        returns_df: DataFrame of historical daily returns for all assets.

    Returns:
        A dictionary containing the results for the optimized portfolios.
    """
    if returns_df.empty:
        raise ValueError("Input returns DataFrame cannot be empty.")
        
    num_assets = len(returns_df.columns)
    
    # Pre-calculate annualized mean returns and covariance matrix
    # Note: We use daily statistics for the optimization function.
    mean_returns = returns_df.mean()
    cov_matrix = returns_df.cov()
    
    # Constraints: sum of weights equals 1
    constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
    
    # Bounds: individual weights must be between 0 and 1 (no short selling)
    bounds = tuple((0, 1) for _ in range(num_assets))
    
    # Initial guess for weights (equal distribution)
    initial_weights = np.array(num_assets * [1. / num_assets])
    
    # --- 1. Find the Maximum Sharpe Ratio Portfolio ---
    max_sharpe_result = minimize(
        negative_sharpe_ratio, 
        initial_weights, 
        args=(mean_returns, cov_matrix), 
        method='SLSQP', 
        bounds=bounds, 
        constraints=constraints
    )
    
    # --- 2. Find the Minimum Volatility Portfolio ---
    min_volatility_result = minimize(
        portfolio_volatility, 
        initial_weights, 
        args=(mean_returns, cov_matrix), 
        method='SLSQP', 
        bounds=bounds, 
        constraints=constraints
    )
    
    # --- Format Results ---
    
    # Max Sharpe Portfolio Metrics
    max_sharpe_weights = max_sharpe_result.x
    max_sharpe_metrics = calculate_portfolio_performance(max_sharpe_weights, mean_returns, cov_matrix)
    
    # Min Volatility Portfolio Metrics
    min_vol_weights = min_volatility_result.x
    min_vol_metrics = calculate_portfolio_performance(min_vol_weights, mean_returns, cov_matrix)
    
    asset_names = returns_df.columns.tolist()
    
    results = {
        "max_sharpe": {
            "return": max_sharpe_metrics[0],
            "volatility": max_sharpe_metrics[1],
            "sharpe_ratio": max_sharpe_metrics[2],
            "weights": dict(zip(asset_names, max_sharpe_weights.round(4)))
        },
        "min_volatility": {
            "return": min_vol_metrics[0],
            "volatility": min_vol_metrics[1],
            "sharpe_ratio": min_vol_metrics[2],
            "weights": dict(zip(asset_names, min_vol_weights.round(4)))
        }
    }
    
    return results

# --- Example Usage (Demonstration) ---

def run_mpt_example():
    """
    Generates mock financial data and runs the MPT optimizer for demonstration.
    """
    # Mock data generation for 4 assets over 100 days
    np.random.seed(42)
    assets = ['SPY', 'QQQ', 'GLD', 'BND']
    
    # Create mock daily returns (simulating different risk/return profiles)
    data = {}
    for asset in assets:
        # Generate random daily returns around a small mean, representing daily % change
        daily_returns = np.random.normal(loc=0.0005, scale=0.015, size=100) 
        data[asset] = daily_returns
        
    returns_df = pd.DataFrame(data)
    
    print("--- Mock Daily Returns Data (Head) ---")
    print(returns_df.head())
    
    print("\n--- Running Portfolio Optimization ---")
    try:
        optimization_results = optimize_portfolio(returns_df)
        
        print("\n✅ Optimization Complete.")
        
        print("\n--- Max Sharpe Ratio Portfolio ---")
        max_sharpe = optimization_results['max_sharpe']
        print(f"Annualized Return: {max_sharpe['return']:.2%}")
        print(f"Annualized Volatility: {max_sharpe['volatility']:.2%}")
        print(f"Sharpe Ratio: {max_sharpe['sharpe_ratio']:.4f}")
        print("Asset Weights:")
        for asset, weight in max_sharpe['weights'].items():
            print(f"  {asset}: {weight:.2%}")
            
        print("\n--- Minimum Volatility Portfolio ---")
        min_vol = optimization_results['min_volatility']
        print(f"Annualized Return: {min_vol['return']:.2%}")
        print(f"Annualized Volatility: {min_vol['volatility']:.2%}")
        print(f"Sharpe Ratio: {min_vol['sharpe_ratio']:.4f}")
        print("Asset Weights:")
        for asset, weight in min_vol['weights'].items():
            print(f"  {asset}: {weight:.2%}")
            
    except ValueError as e:
        print(f"Error during optimization: {e}")

if __name__ == '__main__':
    run_mpt_example()
