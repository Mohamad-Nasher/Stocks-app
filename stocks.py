from email.mime import image
from math import floor
import pandas as pd 
import streamlit as st
import yfinance as yf
import cufflinks as cf
import datetime
from PIL import Image

### App Title 

st.markdown('''
#  Stocks Prices App
An App you can use to quickly examine a stock 

Built By  : Mohamad Nasher
In Python Using Streamlit , yfinance ,pandas, and cufflinks
''')
st.write('---')

### Sidebar 
st.sidebar.subheader("Query Parameters")

start_date = st.sidebar.date_input("Start date", datetime.date(2022 , 1 , 1))
end_date = st.sidebar.date_input("End Date" , datetime.date(2022,8,8))

### Ticker List 
ticker_list = pd.read_csv('tickers.csv')
ticker_symbol = st.sidebar.selectbox("Stock Ticker" , ticker_list)
ticker_data = yf.Ticker(ticker_symbol)

ticker_dataframe = ticker_data.history(period = "1D" , start = start_date , end = end_date)

### Ticker logo 
string_logo = '<img src=%s>' % ticker_data.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)
### Ticker Description
string_name = ticker_data.info['longName']
st.header('**%s**' % string_name)

string_summary = ticker_data.info['longBusinessSummary']
st.info(string_summary)

# Ticker data
st.header('**Stock data**')
st.write(ticker_dataframe)

### Chart 

qf=cf.QuantFig(ticker_dataframe,title='First Quant Figure',legend='top',name='Price')
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)


### Further Info 

#st.markdown("### Stock Return from Selected Start Date to End Date :")

### ROI Calculator
start_price = (ticker_dataframe.iloc[1]["Close"])


end_price = (ticker_dataframe.iloc[-1]["Close"])





ROI = int((end_price - start_price)*100/start_price)



st.markdown("### Return on Your Investment is :" )
st.markdown(f"# {ROI}% ")







