# Return-Risk calculation for all
import yfinance as yf
import pandas as pd

# Ticker's list
tickers = ['AI.PA', 'AIR.PA', 'ALO.PA', 'MT.AS', 'CS.PA', 'BNP.PA', 'ENGI.PA', 'CAP.PA', 'CA.PA', 'DSY.PA', 'KER.PA', 'OR.PA', 'LR.PA', 'MC.PA', 'ML.PA', 'ORA.PA', 'RI.PA', 'PUB.PA', 'RNO.PA', 'SAF.PA', 'SGO.PA', 'SAN.PA', 'SU.PA', 'GLE.PA', 'SW.PA', 'HO.PA', 'DG.PA', 'AAPL', 'MSFT', 'AMZN', 'NMS', 'META', 'TSLA', 'NVDA', 'ADBE', 'PYPL', 'INTC', 'JNJ', 'BABA', 'PG', 'HD', 'V', 'DIS', 'UNH', 'MA', 'CRM', 'NKE']

# Date for data
start_date = '2000-01-01'
end_date = '2023-11-01'

data = pd.DataFrame()
for ticker in tickers:
    try:
        data[ticker] = yf.download(ticker, start=start_date, end=end_date)['Adj Close']
    except Exception as e:
        print(f"Erreur lors de la récupération des données pour {ticker}: {e}")

# Calculating returns and volatility
returns = data.pct_change().dropna()
mean_returns = returns.mean() * 255  # Annual return (255 days of trade)
volatility = returns.std() * np.sqrt(255)  # Annual risk


results_df = pd.DataFrame({'Ticker': tickers, 'Rendement': mean_returns, 'Volatilite': volatility})

result_excel = r'C:\Users\antoi\OneDrive\Bureau\tickers_rendement_risque.xlsx'
results_df.to_excel(result_excel, index=False)



# Corrlation matrix
import pandas as pd
import yfinance as yf
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows  # Importez la fonction dataframe_to_rows

tickers = ['AI.PA', 'AIR.PA', 'ALO.PA', 'MT.AS', 'CS.PA', 'BNP.PA', 'ENGI.PA', 'CAP.PA', 'CA.PA', 'DSY.PA', 'KER.PA', 'OR.PA', 'LR.PA', 'MC.PA', 'ML.PA', 'ORA.PA', 'RI.PA', 'PUB.PA', 'RNO.PA', 'SAF.PA', 'SGO.PA', 'SAN.PA', 'SU.PA', 'GLE.PA', 'SW.PA', 'HO.PA', 'DG.PA', 'AAPL', 'MSFT', 'AMZN', 'NMS', 'META', 'TSLA', 'NVDA', 'ADBE', 'PYPL', 'INTC', 'JNJ', 'BABA', 'PG', 'HD', 'V', 'DIS', 'UNH', 'MA', 'CRM', 'NKE']
start_date = '2000-01-01'
end_date = '2023-01-01'

data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

correlation_matrix = data.corr()

wb = Workbook()
ws = wb.active

df = pd.DataFrame(correlation_matrix)
for r in dataframe_to_rows(df, index=True, header=True):
    ws.append(r)
chemin_fichier_excel = r'C:\Users\antoi\OneDrive\Bureau\tickers_matrice_correlation.xlsx'

# Enregistrer le fichier Excel
wb.save(chemin_fichier_excel)



# MARKOWITZ GRAPHICS
import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

tickers = ['AI.PA', 'AIR.PA', 'ALO.PA', 'MT.AS', 'CS.PA', 'BNP.PA', 'ENGI.PA', 'CAP.PA', 'CA.PA', 'DSY.PA', 'KER.PA', 'OR.PA', 'LR.PA', 'MC.PA', 'ML.PA', 'ORA.PA', 'RI.PA', 'PUB.PA', 'RNO.PA', 'SAF.PA', 'SGO.PA', 'SAN.PA', 'SU.PA', 'GLE.PA', 'SW.PA', 'HO.PA', 'DG.PA', 'AAPL', 'MSFT', 'AMZN', 'NMS', 'META', 'TSLA', 'NVDA', 'ADBE', 'PYPL', 'INTC', 'JNJ', 'BABA', 'PG', 'HD', 'V', 'DIS', 'UNH', 'MA', 'CRM', 'NKE']

start_date = '2000-01-01'
end_date = '2023-01-01'

data = pd.DataFrame()
for ticker in tickers:
    try:
        data[ticker] = yf.download(ticker, start=start_date, end=end_date)['Adj Close']
    except Exception as e:
        print(f"Erreur lors de la récupération des données pour {ticker}: {e}")

# Return calculation and volatility
returns = data.pct_change().dropna()

mean_returns = returns.mean() * 255
volatility = returns.std() * np.sqrt(255)

risk_free_rate = 0.03

portfolio = pd.DataFrame({'Rendement': mean_returns, 'Volatilité': volatility})

# Sharpe Ratio
portfolio['Ratio de Sharpe'] = (portfolio['Rendement'] - risk_free_rate) / portfolio['Volatilité']

plt.figure(figsize=(10, 6))
plt.scatter(portfolio['Volatilité'], portfolio['Rendement'], c=portfolio['Ratio de Sharpe'], cmap='viridis')
plt.title('Frontière efficiente (Courbe de Markowitz)')
plt.xlabel('Volatilité')
plt.ylabel('Rendement')
plt.colorbar(label='Ratio de Sharpe')
plt.grid(True)
plt.tight_layout()

for i, ticker in enumerate(portfolio.index):
    plt.annotate(ticker, (portfolio['Volatilité'][i], portfolio['Rendement'][i]), xytext=(5, -5),
                 textcoords='offset points', ha='left', va='center', fontsize=8, color='black')

plt.grid(True)
plt.tight_layout()


file_path = r'C:\Users\antoi\OneDrive\Bureau\markowitz_curve3.png'
plt.savefig(file_path)
plt.show()


# Distribution optimization
import pandas as pd

# Load yield, volatility and Sharpe data from Excel file
file_path_rendement_risque = r'C:\Users\antoi\OneDrive\Bureau\tickers_rendement_risque.xlsx'
df_rendement_risque = pd.read_excel(file_path_rendement_risque)

# Load correlation matrix from other Excel file
file_path_correlation = r'C:\Users\antoi\OneDrive\Bureau\tickers_matrice_correlation.xlsx'
df_correlation = pd.read_excel(file_path_correlation, index_col=0)  # Mettre la première colonne en index

# Select tickers with a correlation of less than 0.4
tickers_corr_lt_04 = df_correlation[df_correlation < 0.4].dropna(how='all').dropna(axis=1, how='all').index

# Filter returns, volatility and Sharpe data for tickers with a correlation of less than 0.4
df_filtered = df_rendement_risque[df_rendement_risque['Ticker'].isin(tickers_corr_lt_04)]

# Sort Sharpe ratios in order to get the best selection
df_sorted_filtered = df_filtered.sort_values(by='Sharpe', ascending=False)

top_10_tickers = df_sorted_filtered.head(10)['Ticker'].tolist()

print("Les 10 meilleurs tickers avec une corrélation inférieure à 0.4 et le ratio de Sharpe le plus élevé :")
print(top_10_tickers)

import yfinance as yf
import pandas as pd
import numpy as np
from scipy.optimize import minimize
from itertools import combinations

tickers = ['NVDA', 'MSFT', 'AAPL', 'UNH', 'ADBE', 'MC.PA', 'AMZN', 'TSLA', 'MA', 'V']

start_date = '2000-01-01'
end_date = '2023-01-01'

data = pd.DataFrame()
for ticker in tickers:
    data[ticker] = yf.download(ticker, start=start_date, end=end_date)['Adj Close'].pct_change()

data = data.dropna()

def calculate_sharpe(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * 252
    portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    sharpe_ratio = portfolio_return / portfolio_std_dev
    return -sharpe_ratio  # Maximisation, donc négatif du ratio de Sharpe


num_combinations = 2000

# Finding the best combination
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
    result_excel = r'C:\Users\antoi\OneDrive\Bureau\top_10_tickers_FINAL.xlsx'
    result_df.to_excel(result_excel, index=False)
    print(f"Combinaison optimale enregistrée dans '{result_excel}'")
else:
    print("Aucune combinaison optimale trouvée.")