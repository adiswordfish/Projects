import streamlit as st
import yfinance as fn

st.write(""" # My first App with Streamlit """)
st.title("Stock Market App with Streamlit")

st.header("Simple Data Science Web App")
st.sidebar.header("Adi \n The first predict app ...")

def get_ticker(name):
    company = fn.Ticker(name)
    return company

c1 = get_ticker("AAPL")
c2 = get_ticker("MSFT")
c3 = get_ticker("TSLA")

apple = fn.download("AAPL", start="2021-11-11", end="2021-11-11")
microsoft = fn.download("MSFT", start="2021-11-11", end="2021-11-11")
tesla = fn.download("TSLA", start="2021-11-11", end="2021-11-11")

data1 = c1.history(period="3mo")
data2 = c2.history(period="3mo")
data3 = c2.history(period="3mo")

st.write("""### Apple""")
st.write(c1.info['longBusinessSummary'])
st.write(apple)
st.line_chart(data1.values)