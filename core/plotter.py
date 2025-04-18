import plotly.graph_objects as go
import pandas as pd
# import os

def plot_stock_data_html(data: pd.DataFrame, ticker: str) -> str:
    """
    Create a Plotly figure of stock closing prices.

    Args:
        data (pd.DataFrame): Historical stock data.
        ticker (str): Stock ticker symbol.

    Returns:
        str: Path to the saved HTML plot.
    """
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=data.index,
        y=data["Close"],
        mode="lines",
        name="Close Price"
        # line=dict(color="royalblue", width=2)
    ))

    fig.update_layout(
        title=f"{ticker} Closing Price History",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        template="plotly_white",
        hovermode="x unified",
        width=700,
        height=500
    )

    # Save plot to an HTML file
    # output_dir = "plots"
    # os.makedirs(output_dir, exist_ok=True)
    # file_path = os.path.join(output_dir, f"{ticker}_plot.png")
    # fig.write_image(file_path)

    return fig.to_html(include_plotlyjs = "cdn")
