import yfinance as yf
import streamlit as st
import pandas as pd

st.title("Stock Performance Comparison Dashboard")
tickers = ('TSLA','AAPL','MSFT','BTC-USD','ETH-USD')

dropdown=st.multiselect('Pick your assets', tickers)

start = st.date_input('Start', value= pd.to_datetime('2021-01-01'))
end = st.date_input('End',value = pd.to_datetime('today'))

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

if len(dropdown) >0:
    #df = yf.download(dropdown,start,end)['Close'] --- needed to measure the daily % return to normalize the tickers (see below)
    df = relativeret(yf.download(dropdown,start,end)['Close'])
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(df)