from core.plotter import plot_stock_data
import pandas as pd

def test_plot_stock_data_creates_file(tmp_path):
    # Fake data
    data = pd.DataFrame({
        "Close": [150, 152, 155],
    }, index=pd.date_range(start="2024-01-01", periods=3))
    
    plot_path = plot_stock_data(data, "FAKE")
    assert plot_path.endswith(".png")
