# Define the ticker list
import pandas as pd


# Fetch the data
import yfinance as yf


tickers_list = ['AAPL', 'WMT', 'IBM', 'MU', 'BA', 'AXP', 'GOOG', 'MSFT', 'TSLA', 'AMZN', 'SOFI', 'PLTR', 'NIO', 'F', 'GM', 'T', 'VZ', 'NFLX', 'DIS', 'BABA', 'TCEHY', 'NVDA', 'AMD', 'INTC', 'QCOM', 'CSCO', 'ORCL', 'CRM', 'NOW', 'ZM', 'DOCU', 'UBER', 'LYFT', 'PINS', 'SNAP', 'META']
data_list = []

for ticker in tickers_list:
    data = yf.download(ticker, period='5y')
    data["ticker"] = ticker
    # Save the data
    data_list.append(data)
data = pd.concat(data_list)

# Reset the column names
data = data.reset_index(drop=False)
data = data.rename(columns={
    'Date': 'date',
    'Open': 'open',
    'High': 'high',
    'Low': 'low',
    'Close': 'close',
    'Adj Close': 'adj_close',
    'Volume': 'volume'
})

data = data[['ticker', 'date', 'open', 'high', 'low', 'close', 'adj_close', 'volume']]


# Save the data
df = data

df.to_csv('stock.csv')