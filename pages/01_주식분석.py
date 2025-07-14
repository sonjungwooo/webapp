import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("📈 상위 종목 + 미래 주가 예측")

# 분석 대상 종목 리스트
tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "TSLA"]

# 수익률 상위 1~3 종목 선별
returns = {}
price_data = {}

for ticker in tickers:
    data = yf.Ticker(ticker).history(period="30d")
    if len(data) >= 2:
        ret = (data['Close'][-1] - data['Close'][0]) / data['Close'][0]
        returns[ticker] = round(ret * 100, 2)
        price_data[ticker] = data

# 수익률 기준 상위 종목 3개
top3 = sorted(returns.items(), key=lambda x: x[1], reverse=True)[:3]

for ticker, pct in top3:
    st.subheader(f"🚀 {ticker} (최근 30일 수익률: {pct}%)")

    data = price_data[ticker].copy()
    data.reset_index(inplace=True)
    data['Day'] = (data['Date'] - data['Date'].min()).dt.days
    X = data['Day'].values.reshape(-1, 1)
    y = data['Close'].values

    # 선형 회귀 모델로 예측
    model = LinearRegression()
    model.fit(X, y)

    # 향후 30일 예측
    last_day = X[-1][0]
    future_days = np.array([last_day + i for i in range(1, 31)]).reshape(-1, 1)
    future_prices = model.predict(future_days)

    future_dates = pd.date_range(start=data['Date'].iloc[-1] + pd.Timedelta(days=1), periods=30)

    # 그래프
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'],
                             mode='lines', name='실제 주가'))
    fig.add_trace(go.Scatter(x=future_dates, y=future_prices,
                             mode='lines', name='예측 주가', line=dict(dash='dot')))
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)
