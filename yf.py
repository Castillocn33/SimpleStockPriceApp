import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and **volume** of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0deidf17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')
#Open High   Low Close   Volume Dividends    Stock Split

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
