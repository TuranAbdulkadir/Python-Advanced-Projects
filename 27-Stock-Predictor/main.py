import yfinance as yf
import matplotlib.pyplot as plt

ticker = input("Stock Symbol (e.g., AAPL, TSLA, BTC-USD): ")
print(f"Downloading data for {ticker}...")

data = yf.download(ticker, start="2024-01-01", end="2025-01-01")

plt.figure(figsize=(10, 5))
plt.plot(data['Close'], label='Close Price')
plt.title(f"{ticker} Stock Price History")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()