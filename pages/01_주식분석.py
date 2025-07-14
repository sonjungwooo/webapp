import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

st.title("📈 최근 상승세 종목 추천기")

# S&P 500 일부 티커 목록 예시 (직접 늘릴 수 있음)
tickers = ["AAPL", "MSFT", "NVDA", "GOOGL", "TSLA", "META", "AMZN", "NFLX", "AMD", "INTC", "PEP", "JNJ", "XOM"]

# 최근 7일간 수익률 계산
price_data = {}
returns = {}

with st.spinner("📡 종목 분석 중..."):
    for ticker in tickers:
        data = yf.Ticker(ticker).history(period="10d")
        if len(data) >= 2:
            pct = (data['Close'][-1] - data['Close'][0]) / data['Close'][0]
            returns[ticker] = round(pct * 100, 2)
            price_data[ticker] = data

# 상위 3개 종목 선택
top_tickers = sorted(returns.items(), key=lambda x: x[1], reverse=True)[:3]

st.subheader("🚀 최근 상승률 상위 종목")
for ticker, pct in top_tickers:
    st.markdown(f"**{ticker}**: 최근 7일간 수익률 **{pct}%**")
    data = price_data[ticker]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))

    # 단순 예측선 (20일 평균 기준 0.5% 일별 상승 가정)
    ma = data['Close'].rolling(20).mean().dropna()
    if not ma.empty:
        last_avg = ma.iloc[-1]
        future_dates = [data.index[-1] + pd.Timedelta(days=i) for i in range(1, 31)]
        future = [last_avg * (1 + 0.005 * i) for i in range(1, 31)]
        fig.add_trace(go.Scatter(x=future_dates, y=future, name="예상 상승", line=dict(dash="dot")))

    st.plotly_chart(fig, use_container_width=True)
