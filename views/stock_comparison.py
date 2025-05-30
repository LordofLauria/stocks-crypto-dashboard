import yfinance as yf
import streamlit as st
import pandas as pd

st.title("Stock Performance Comparison Dashboard")

common_tickers = ('AAPL','SPY','QQQ','MSFT','BTC-USD','ETH-USD','TSLA','DJI','IWM')

selected = st.multiselect("Select from popular tickers:", common_tickers)
custom_input = st.text_input("Add custom tickers (comma-separated):")

custom_tickers = [t.strip().upper() for t in custom_input.split(",") if t.strip()]
all_selected = selected + custom_tickers

start = st.date_input('Start', value= pd.to_datetime('2021-01-01'))
end = st.date_input('End',value = pd.to_datetime('today'))

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

if len(all_selected) >0:
    #df = yf.download(dropdown,start,end)['Close'] --- needed to measure the daily % return to normalize the tickers (see below)
    df = relativeret(yf.download(all_selected,start,end)['Close'])
    st.header('Returns of {}'.format(all_selected))
    st.line_chart(df)