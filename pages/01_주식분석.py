import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import numpy as np
import pandas as pd

st.title("🎲 몬테카를로 시뮬레이션으로 미래 주가 예측")

ticker = st.text_input("분석할 종목 티커 입력 (예: AAPL)", value="AAPL").upper()

if ticker:
    data = yf.Ticker(ticker).history(period="1y")['Close']
    st.write(f"최근 1년간 종가 데이터 (총 {len(data)}일)")

    # 일별 수익률 계산
    returns = data.pct_change().dropna()

    # 몬테카를로 시뮬레이션 파라미터
    last_price = data[-1]
    num_simulations = 100
    num_days = 30

    # 시뮬레이션 결과 저장
    simulation_df = pd.DataFrame()

    np.random.seed(42)
    for i in range(num_simulations):
        prices = [last_price]
        for _ in range(num_days):
            shock = np.random.normal(loc=returns.mean(), scale=returns.std())
            price = prices[-1] * (1 + shock)
            prices.append(price)
        simulation_df[i] = prices

    # 그래프 그리기
    fig = go.Figure()

    # 과거 실제 종가
    fig.add_trace(go.Scatter(x=data.index, y=data.values,
                             mode='lines', name='실제 종가'))

    # 시뮬레이션 결과들 (미래 예측)
    future_dates = pd.date_range(start=data.index[-1], periods=num_days + 1)
    for i in range(num_simulations):
        fig.add_trace(go.Scatter(x=future_dates, y=simulation_df[i],
                                 mode='lines', line=dict(color='rgba(0,100,80,0.1)'),
                                 showlegend=False))

    fig.update_layout(title=f"{ticker} 미래 주가 몬테카를로 시뮬레이션 (30일 전망)",
                      xaxis_title="날짜", yaxis_title="주가",
                      height=500)

    st.plotly_chart(fig, use_container_width=True)
