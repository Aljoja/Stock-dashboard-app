from core.stock_api import fetch_stock_data, fetch_current_price

def test_fetch_stock_data_valid():
    data = fetch_stock_data("AAPL")
    assert not data.empty
    assert "Close" in data.columns

def test_fetch_current_price_valid():
    price = fetch_current_price("AAPL")
    assert isinstance(price, float)
    assert price > 0