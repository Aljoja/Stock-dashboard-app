import streamlit as st
from core.stock_api import fetch_stock_data, fetch_current_price
from core.plotter import plot_stock_data
import plotly.graph_objects as go

# Streamlit page config
st.set_page_config(page_title="📈 Stock Dashboard", layout="wide")

st.title("📊 Stock Dashboard App")

# Sidebar: inputs
ticker = st.text_input("Enter Stock Ticker", value="AAPL")
period = st.selectbox("Select Time Range", ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"])
interval = st.selectbox("Select Data Interval", ["1d", "1h", "15m", "1wk"])

if st.button("Fetch Data"):
    try:
        # Fetch data
        data = fetch_stock_data(ticker, period=period, interval=interval)

        # Display current price
        current_price = fetch_current_price(ticker)
        st.subheader(f"Current {ticker} price: ${current_price:.2f}")

        # Plot interactive chart
        fig = plot_stock_data(data, ticker)
        st.plotly_chart(fig, use_container_width=True)

        # Show data table
        with st.expander("Show raw data"):
            st.dataframe(data.tail())

    except Exception as e:
        st.error(f"Error: {e}")
