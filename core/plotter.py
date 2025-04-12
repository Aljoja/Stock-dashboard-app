import matplotlib.pyplot as plt
import pandas as pd
import os

def plot_stock_data(data: pd.DataFrame, ticker: str) -> str:
    """
    Plot the stock's closing price history and save it as an image.

    Args:
        data (pd.DataFrame): Historical stock data.
        ticker (str): Stock ticker symbol.

    Returns:
        str: Path to the saved plot image.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], label="Close Price")
    plt.title(f"{ticker} Closing Price History")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)

    # Save plot to a file
    output_dir = "plots"
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f"{ticker}_plot.png")
    plt.savefig(file_path)
    plt.close()

    return file_path
