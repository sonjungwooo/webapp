import streamlit as st
import yfinance as yf
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly
import plotly.graph_objs as go

st.title("📈 여러 종목 Prophet 미래 주가 예측")

tickers_input = st.text_input("분석할 종목 티커 여러 개 입력 (쉼표로 구분)", "AAPL,MSFT,NVDA")

tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]

if tickers:
    periods = 30  # 예측 기간(일)
    for ticker in tickers:
        st.header(f"{ticker} 주가 예측")
        try:
            data = yf.Ticker(ticker).history(period="2y")[['Close']].reset_index()
            data.rename(columns={'Date':'ds', 'Close':'y'}, inplace=True)

            # Prophet 모델 학습
            m = Prophet(daily_seasonality=True)
            m.fit(data)

            # 미래 데이터프레임 생성 및 예측
            future = m.make_future_dataframe(periods=periods)
            forecast = m.predict(future)

            # Plotly 그래프 생성
            fig = plot_plotly(m, forecast)
            st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"{ticker} 데이터 처리 중 오류 발생: {e}")
