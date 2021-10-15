#!/usr/bin/env python
# coding: utf-8

# In[5]:


import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")


#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf1 = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf1.Close)
st.line_chart(tickerDf1.Volume)

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Facebook!
""")


#define the ticker symbol
tickerSymbol = 'FB'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf2 = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf2.Close)
st.line_chart(tickerDf2.Volume)

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Amazon!
""")



#define the ticker symbol
tickerSymbol = 'AMZN'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf3 = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf3.Close)
st.line_chart(tickerDf3.Volume)

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Apple!
""")



#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf4 = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf4.Close)
st.line_chart(tickerDf4.Volume)

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Netflix!
""")



#define the ticker symbol
tickerSymbol = 'NFLX'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf5 = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf5.Close)
st.line_chart(tickerDf5.Volume)


# In[ ]:




