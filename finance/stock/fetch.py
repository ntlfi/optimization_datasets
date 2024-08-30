# Define the ticker list
import pandas as pd


# Fetch the data
import yfinance as yf


tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP', 'GOOG', 'MSFT']
data_list = []
for ticker in tickers_list:
    data = yf.download(ticker, period='1y')
    data["ticker"] = ticker
    # Save the data
    data_list.append(data)
data = pd.concat(data_list)

# Save the data
df = data

df.to_csv('data.csv')