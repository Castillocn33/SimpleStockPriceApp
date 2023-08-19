# SimpleStockPriceApp
Closing stock prices and volume of Google

This Python code uses the yfinance and streamlit libraries to build a simple web app that 
displays the closing price and trading volume of Google stock.

The key steps are:
1. Import required libraries: yfinance for fetching stock data, streamlit for building the web app.
2. Use yfinance to get historical price data for Google (ticker symbol GOOGL) from 2010-2020.
3. Use streamlit to create a header explaining the app.
4. Display a line chart of the closing prices over time using st.line_chart.
5. Display a line chart of the trading volume over time.
6. Host the app locally using Streamlit to view the resulting charts.

This demonstrates skills in:
Fetching financial data from external APIs
Cleaning and preparing data for analysis
Visualizing time series data using Python libraries
And building and deploying simple web apps with Streamlit

https://simplestockpriceapp-dmudegyrqkr4m54zbcbvzr.streamlit.app/
