import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, period: str = "1mo", interval: str = "1d") -> pd.DataFrame:
    """
    Fetch historical stock data for a given ticker.
    
    Args:
        ticker (str): The stock symbol (e.g., "AAPL", "TSLA").
        period (str): How much historical data to fetch (e.g., "1mo", "3mo", "6mo", "1y").
        interval (str): Data interval (e.g., "1d" = daily, "1h" = hourly).
        
    Returns:
        pd.DataFrame: Stock historical data with datetime index.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=period, interval=interval)

        if hist.empty:
            raise ValueError(f"No data found for ticker '{ticker}'")

        return hist

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        raise

def fetch_current_price(ticker: str) -> float:
    """
    Fetch the current stock price for a given ticker.
    
    Args:
        ticker (str): The stock symbol.
        
    Returns:
        float: Latest stock price.
    """
    try:
        stock = yf.Ticker(ticker)
        price = stock.info.get("regularMarketPrice", None)

        if price is None:
            raise ValueError(f"Could not fetch current price for ticker '{ticker}'")

        return price

    except Exception as e:
        print(f"Error fetching current price for {ticker}: {e}")
        raise
