# First, I created the correlation matrix
# I import what we need for the suite


import pandas as pd
import yfinance as yf
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows  # Importez la fonction dataframe_to_rows


# Recover share price data
tickers = ['MSFT', 'NMS', 'TTE', 'PYPL', 'BP', 'BABA', 'NVDA', 'WMT', 'AMZN', 'IBM', 'INTC', 'QCOM', 'DIS', 'AIR.PA', 'RI.PA', 'MC.PA', 'SU.PA', 'META', 'MDLZ', 'AI.PA', 'IBE.MC', 'BMW.DE', 'TSLA', 'BNP.PA', 'DBK.DE', 'COST', 'SHL.DE', 'DBK.DE', 'MDLZ', 'BABA', 'SHL.DE', 'BP', 'PYPL', 'IBM', 'META', 'NMS', 'TTE']

# Select the time period of interest for correlation calculations
start_date = '2000-01-01'
end_date = '2023-01-01'

data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

# Correlation calcul
correlation_matrix = data.corr()

# Creation of an excel doc
wb = Workbook()
ws = wb.active

df = pd.DataFrame(correlation_matrix)
for r in dataframe_to_rows(df, index=True, header=True):
    ws.append(r)

chemin_fichier_excel = r'C:\Users\antoi\OneDrive\Bureau\tickers_matrice_correlation.xlsx'
wb.save(chemin_fichier_excel)


# Calculation of yield for all tickers
import yfinance as yf
import pandas as pd

tickers = ['MSFT', 'NMS', 'TTE', 'PYPL', 'BP', 'BABA', 'NVDA', 'WMT', 'AMZN', 'IBM', 'INTC', 'QCOM', 'DIS', 'AIR.PA', 'RI.PA', 'MC.PA', 'SU.PA', 'META', 'MDLZ', 'AI.PA', 'IBE.MC', 'BMW.DE', 'TSLA', 'BNP.PA', 'DBK.DE', 'COST', 'SHL.DE']

start_date = '2000-01-01'
end_date = '2023-01-01'

# Dictionary to store profitability expectations for each ticker
expected_returns = {}

for ticker in tickers:
# Retrieve historical data for each ticker
    data = yf.download(ticker, start=start_date, end=end_date)['Adj Close']

# Daily yield calculation
    returns = data.pct_change()

# Calculation of expected annual profitability for each ticker
    expected_return = returns.mean() * 255

# Storing profitability expectations in the dictionary
    expected_returns[ticker] = expected_return

# DataFrame Creation à
df_expected_returns = pd.DataFrame(expected_returns.items(), columns=['Ticker', 'Expected Annual Return'])

chemin_fichier_excel = r'C:\Users\antoi\OneDrive\Bureau\esperance_rendement_tickers.xlsx'

df_expected_returns.to_excel(chemin_fichier_excel, index=False)

# Calculation of volatility and yield for all tickers

tickers = ['MSFT', 'NMS', 'TTE', 'PYPL', 'BP', 'BABA', 'NVDA', 'WMT', 'AMZN', 'IBM', 'INTC', 'QCOM', 'DIS', 'AIR.PA', 'RI.PA', 'MC.PA', 'SU.PA', 'META', 'MDLZ', 'AI.PA', 'IBE.MC', 'BMW.DE', 'TSLA', 'BNP.PA', 'DBK.DE', 'COST', 'SHL.DE']

start_date = '2000-01-01'
end_date = '2023-01-01'

volatilities = {}

for ticker in tickers:
    data = yf.download(ticker, start=start_date, end=end_date)['Adj Close']

    returns = data.pct_change()

    volatility = returns.std() * (252 ** 0.5)  # 252 jours de trading dans une année

    volatilities[ticker] = volatility

df_volatilities = pd.DataFrame(volatilities.items(), columns=['Ticker', 'Volatility'])

chemin_fichier_excel = r'C:\Users\antoi\OneDrive\Bureau\volatilite_tickers.xlsx'

df_volatilities.to_excel(chemin_fichier_excel, index=False)

# OPTIMIZATION SELECTION:

import yfinance as yf
import pandas as pd
import numpy as np
from scipy.optimize import minimize
from itertools import combinations

# Liste of tickers selected from the correlation matrix
tickers = ['BABA', 'BP', 'DBK.DE', 'IBM', 'MDLZ', 'META', 'NMS', 'PYPL', 'SHL.DE', 'TTE']

start_date = '2000-01-01'
end_date = '2023-01-01'

data = pd.DataFrame()
for ticker in tickers:
    data[ticker] = yf.download(ticker, start=start_date, end=end_date)['Adj Close'].pct_change()

data = data.dropna()


# Sharpe ratio calculation
def calculate_sharpe(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * 252
    portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    sharpe_ratio = portfolio_return / portfolio_std_dev
    return -sharpe_ratio  # Maximisation, donc négatif du ratio de Sharpe


# Number of combinations to generate and test
num_combinations = 2000

# Finding the best combination from a random sample
best_sharpe = -np.inf
best_portfolio = None
for _ in range(num_combinations):
    combination = np.random.choice(tickers, size=10, replace=False)
    selected_data = data[list(combination)]
    weights = np.random.uniform(low=0.005, high=0.25, size=10)
    weights /= np.sum(weights)

    optimized_weights = minimize(calculate_sharpe, weights, args=(selected_data,), method='SLSQP',
                                 bounds=[(0.005, 0.25)] * 10,
                                 constraints={'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})

    if optimized_weights.success:
        sharpe = -optimized_weights.fun
        if sharpe > best_sharpe:
            best_sharpe = sharpe
            best_portfolio = list(combination), optimized_weights.x

if best_portfolio:
    tickers_combination, portfolio_weights = best_portfolio
    result_df = pd.DataFrame({'Tickers': tickers_combination, 'Weights': portfolio_weights})
    result_excel = r'C:\Users\antoi\OneDrive\Bureau\top_10_tickers_correlation_in.xlsx'
    result_df.to_excel(result_excel, index=False)
    print(f"Combinaison optimale enregistrée dans '{result_excel}'")
else:
    print("Aucune combinaison optimale trouvée.")