import yfinance as yf
import pandas as pd

tickers = ["USO","GLD","SPY","QQQ"]
data = {}

for t in tickers:
    obj = yf.Ticker(t)
    data[t] = obj.history(
        start="2018-01-01"
    )["Close"]

# 合并成一张大表
df = pd.DataFrame(data)
df.to_csv("market_data.csv")

print(f"共 {len(df)} 个交易日")