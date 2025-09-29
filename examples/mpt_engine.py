import numpy as np
import pandas as pd
from scipy.optimize import minimize

# --- Constantes y Configuración ---
RISK_FREE_RATE = 0.02  # Tasa de rendimiento libre de riesgo (ej. Letras del Tesoro a corto plazo)
NUM_PORTFOLIOS = 10000 # Número de simulaciones de Monte Carlo para la Frontera Eficiente

# --- 1. Generación de Datos Simulados ---

def generate_mock_data(tickers, periods=252 * 5):
    """
    Genera datos históricos de precios y calcula retornos diarios para simulación.
    
    Argumentos:
        tickers (list): Lista de tickers de activos (ej. ['AAPL', 'MSFT', 'BONO']).
        periods (int): Número de períodos (días) a simular.
        
    Retorna:
        pd.DataFrame: DataFrame con los retornos diarios.
    """
    print(f"Generando datos simulados para: {tickers} durante {periods} días...")
    
    # Simulación de retornos diarios aleatorios con un sesgo (drift) positivo para acciones.
    # Usamos una estructura de datos simple para mantener la trazabilidad.
    np.random.seed(42) 
    
    data = {}
    for i, ticker in enumerate(tickers):
        # Media de retorno diario (simulada)
        daily_mean = 0.0003 + (i * 0.0001) 
        # Volatilidad diaria (simulada)
        daily_vol = 0.01 + (i * 0.001) 
        
        # Generar retornos aleatorios (distribución normal)
        returns = np.random.normal(daily_mean, daily_vol, periods)
        # Convertir a precios (asumiendo precio inicial de 100)
        prices = 100 * np.exp(np.cumsum(returns)) 
        data[ticker] = prices
        
    prices_df = pd.DataFrame(data)
    # Calcular retornos diarios (cambio porcentual)
    daily_returns = prices_df.pct_change().dropna()
    
    return daily_returns

# --- 2. Funciones de Rendimiento y Riesgo ---

def calculate_annual_metrics(daily_returns, weights):
    """
    Calcula el rendimiento anual esperado, la volatilidad y el Sharpe Ratio
    para una cartera dada.
    
    Argumentos:
        daily_returns (pd.DataFrame): Retornos diarios de los activos.
        weights (np.array): Array de pesos de la cartera.
        
    Retorna:
        tuple: (retorno_anual, volatilidad_anual, sharpe_ratio)
    """
    # 252 días de negociación en un año
    annualization_factor = 252 
    
    # 1. Rendimiento Anual Esperado (Media de los retornos)
    mean_returns = daily_returns.mean()
    portfolio_return = np.sum(mean_returns * weights) * annualization_factor
    
    # 2. Matriz de Covarianza Anual
    cov_matrix = daily_returns.cov() * annualization_factor
    
    # 3. Volatilidad Anual (Desviación estándar de la cartera)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    
    # 4. Sharpe Ratio
    sharpe_ratio = (portfolio_return - RISK_FREE_RATE) / portfolio_volatility
    
    return portfolio_return, portfolio_volatility, sharpe_ratio, cov_matrix, mean_returns

# --- 3. Funciones de Optimización (MPT) ---

def neg_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate):
    """
    Función objetivo para MINIMIZAR.
    Se utiliza el negativo del Sharpe Ratio porque la biblioteca `minimize` de SciPy
    está diseñada para encontrar mínimos, no máximos.
    """
    p_ret = np.sum(mean_returns * weights) * 252
    p_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
    sharpe = (p_ret - risk_free_rate) / p_vol
    return -sharpe

def maximize_sharpe_ratio(mean_returns, cov_matrix, risk_free_rate):
    """
    Encuentra los pesos de la cartera que maximizan el Sharpe Ratio
    (la Cartera Tangente).
    """
    num_assets = len(mean_returns)
    args = (mean_returns, cov_matrix, risk_free_rate)
    
    # Restricciones: la suma de los pesos debe ser 1 (100%)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    
    # Límites: los pesos individuales deben estar entre 0 y 1 (no se permite apalancamiento ni ventas en corto)
    bounds = tuple((0, 1) for asset in range(num_assets))
    
    # Pesos iniciales: distribución equitativa
    initial_weights = np.array(num_assets * [1. / num_assets])
    
    # Ejecutar la optimización
    optimal_results = minimize(
        neg_sharpe_ratio, 
        initial_weights, 
        args=args, 
        method='SLSQP', 
        bounds=bounds, 
        constraints=constraints
    )
    
    return optimal_results.x # Retorna los pesos óptimos

def minimize_volatility(mean_returns, cov_matrix):
    """
    Encuentra los pesos de la cartera que minimizan la volatilidad total
    (la Cartera de Mínima Varianza Global).
    """
    num_assets = len(mean_returns)
    
    # Función objetivo: Volatilidad
    def portfolio_volatility(weights, cov_matrix):
        return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)

    args = (cov_matrix,)
    
    # Restricciones y límites son los mismos que en la optimización de Sharpe
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for asset in range(num_assets))
    initial_weights = np.array(num_assets * [1. / num_assets])

    optimal_results = minimize(
        portfolio_volatility, 
        initial_weights, 
        args=args, 
        method='SLSQP', 
        bounds=bounds, 
        constraints=constraints
    )
    
    return optimal_results.x # Retorna los pesos óptimos

# --- 4. Motor Principal de MPT (Punto de entrada de la Capa de Negocio) ---

def run_mpt_engine(daily_returns, risk_free_rate=RISK_FREE_RATE, num_portfolios=NUM_PORTFOLIOS):
    """
    Función principal que ejecuta la simulación de Monte Carlo y las
    optimizaciones MPT.
    
    Retorna:
        dict: Diccionario con los resultados clave (Frontera Eficiente, Cartera Óptima).
    """
    # 1. Preparación de datos (Cálculo de retornos medios y matriz de covarianza)
    # Se utiliza la función de cálculo de métricas con pesos iguales para obtener
    # los valores anualizados de retorno y covarianza para la optimización.
    num_assets = len(daily_returns.columns)
    weights_eq = np.array(num_assets * [1. / num_assets])
    _, _, _, cov_matrix_ann, mean_returns_ann = calculate_annual_metrics(daily_returns, weights_eq)
    
    # 2. Simulación de Monte Carlo para trazar la Frontera Eficiente
    
    # Arrays para almacenar los resultados de la simulación
    portfolio_results = np.zeros((4, num_portfolios)) # [Retorno, Volatilidad, Sharpe, Pesos]
    
    print(f"Iniciando simulación de Monte Carlo con {num_portfolios} carteras...")
    
    for i in range(num_portfolios):
        # 1. Generar pesos aleatorios
        weights = np.array(np.random.random(num_assets))
        weights /= np.sum(weights) # Normalizar para que sumen 1
        
        # 2. Calcular métricas anualizadas
        p_return, p_volatility, p_sharpe, _, _ = calculate_annual_metrics(daily_returns, weights)
        
        # 3. Almacenar resultados
        portfolio_results[0, i] = p_return
        portfolio_results[1, i] = p_volatility
        portfolio_results[2, i] = p_sharpe
        
    # Crear un DataFrame con los resultados de la simulación
    all_portfolios = pd.DataFrame({
        'Volatility': portfolio_results[1],
        'Return': portfolio_results[0],
        'Sharpe Ratio': portfolio_results[2],
    })
    
    # 3. Optimización para Cartera de Máximo Sharpe (Cartera Tangente)
    optimal_sharpe_weights = maximize_sharpe_ratio(mean_returns_ann, cov_matrix_ann, risk_free_rate)
    ret_s, vol_s, sharpe_s, _, _ = calculate_annual_metrics(daily_returns, optimal_sharpe_weights)
    
    # 4. Optimización para Cartera de Mínima Varianza Global
    optimal_min_vol_weights = minimize_volatility(mean_returns_ann, cov_matrix_ann)
    ret_v, vol_v, sharpe_v, _, _ = calculate_annual_metrics(daily_returns, optimal_min_vol_weights)

    # 5. Formato de resultados para la Capa de Presentación
    assets = daily_returns.columns
    
    max_sharpe_portfolio = {
        'Return': ret_s,
        'Volatility': vol_s,
        'Sharpe Ratio': sharpe_s,
        'Weights': dict(zip(assets, optimal_sharpe_weights.round(4)))
    }

    min_volatility_portfolio = {
        'Return': ret_v,
        'Volatility': vol_v,
        'Sharpe Ratio': sharpe_v,
        'Weights': dict(zip(assets, optimal_min_vol_weights.round(4)))
    }
    
    print("\n--- Resultados de la Optimización MPT ---")
    print(f"Cartera de Máximo Sharpe (Tangente):")
    print(f"  Retorno Esperado: {ret_s:.2%}")
    print(f"  Volatilidad: {vol_s:.2%}")
    print(f"  Sharpe Ratio: {sharpe_s:.2f}")
    print(f"  Pesos de Activos: {max_sharpe_portfolio['Weights']}")

    print(f"\nCartera de Mínima Volatilidad:")
    print(f"  Retorno Esperado: {ret_v:.2%}")
    print(f"  Volatilidad: {vol_v:.2%}")
    print(f"  Sharpe Ratio: {sharpe_v:.2f}")
    print(f"  Pesos de Activos: {min_volatility_portfolio['Weights']}")
    
    return {
        'frontier_data': all_portfolios,
        'max_sharpe_portfolio': max_sharpe_portfolio,
        'min_volatility_portfolio': min_volatility_portfolio,
        'assets': assets.tolist()
    }


# --- Bloque de Ejecución (Para demostración y pruebas) ---
if __name__ == '__main__':
    
    # Definición de activos (tomado del contexto de FinTech/Inversión)
    ASSET_TICKERS = ['SPY', 'QQQ', 'GLD', 'BND'] # S&P 500, Nasdaq 100, Oro, Bonos
    
    # Generar los retornos de datos
    returns_df = generate_mock_data(ASSET_TICKERS)
    
    # Ejecutar el motor MPT
    results = run_mpt_engine(returns_df)
    
    # Opcional: Mostrar los primeros resultados simulados para verificación
    # print("\nPrimeros 5 carteras simuladas (Frontera Eficiente):")
    # print(results['frontier_data'].head())
    
    # El diccionario 'results' se enviaría a una capa superior (ej. API/Frontend)
    # para ser visualizado en el dashboard (Prompt 3).
    
    print("\nEl módulo MPT ha finalizado la optimización con datos simulados.")
    print("Este módulo está listo para ser integrado con datos reales (Plaid/Market Data).")
