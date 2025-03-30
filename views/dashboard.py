import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# Page Title
st.title("Stock Data - Dashboard")

# Sidebar inputs
st.sidebar.header("Shauny B's Stock Inputs")
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, MSFT)", value="MSFT")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date",value=pd.to_datetime("2025-12-31"))
ma_window = st.sidebar.slider("Moving Average Window", min_value=5, max_value=50, value=20)

# Fetching Data
st.write(f"Fetching data for **(ticker symbol)** from (start_date) to (end_date)...")
data=yf.download(ticker_symbol, start=start_date, end=end_date)

if data.empty:
    st.error("No data found. Please check the ticker symbol or date range....dumbfuck")
    st.stop()

data['MA'] = data ['Close'].rolling(window=ma_window).mean()

#Initialize Tabs
tabs = st.tabs(["Raw Data","Price Chart","Volume Chart","Moving Averages","Dividends & Splits","Stock Comparison"])

#Tab 1:Raw Data
with tabs[0]:
    st.subheader(f"Raw Data for. (ticker_symbol)")
    st.write(data.tail())
    st.download_button("Download Data as csv",data.to_csv(),file_name=f"(ticker_symbol)_data.csv")

# Tab 2: Closing Price Chart
with tabs[1]:
    if "Close" in data:
        st.subheader("Closing Price Over Time")
        st.line_chart(data['Close'])
    else:
        st.warning("Closing price data is not available for this stock.")

# Tab 3: Volume Chart
with tabs[2]:
    if "Volume" in data:
        st.subheader("Volume Over Time")
        st.bar_chart(data['Volume'])
    else:
        st.warning("Volume data is not available for this stock.")

# Tab 4: Moving Averages
with tabs[3]:
    st.subheader(f"Closing Price with (ma_window)-Day Moving Average")
    fig, ax=plt.subplots(figsize=(10,5))
    ax.plot(data.index, data['Close'], label = "Closing Price", color = 'blue')
    ax.plot(data.index, data['MA'], label=f"(ma_window)-Day Moving Average", color='orange')
    ax.set_title(f"Closing Price with (ma_window)-Day Moving Average")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    st.pyplot(fig)

    # Tab 5: Dividends & Splits
with tabs[4]:
    st.subheader("Dividends & Splits")
    ticker = yf.Ticker(ticker_symbol)
    dividends = ticker.dividends
    splits = ticker.splits

    st.write("**Dividends:**")
    st.write(dividends if not dividends.empty else "No dividends found during this period.")
    st.write("**Splits:**")
    st.write(splits if not splits.empty else "No splits found during this period.")

# Tab 6: Stock Performance Comparisons. Note - can't figure out how to add a multiselector that doesn't rely on the overall streamlit sidebar
with tabs[5]:
    st.subheader("Stock Performance Comparison")
    ticker = yf.Ticker(ticker_symbol)

    st.write(data)



#To run: Need to be in Terminal (pycharm terminal below) and enter:
#streamlit run stocks.py
#To Close the Program: In the Terminal Press "Control + C"




