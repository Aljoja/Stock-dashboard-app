import plotly.graph_objects as go
import pandas as pd
# import os

def plot_stock_data_html(data: pd.DataFrame, ticker: str, theme: str) -> str:
    """
    Create a Plotly figure of stock closing prices.

    Args:
        data (pd.DataFrame): Historical stock data.
        ticker (str): Stock ticker symbol.

    Returns:
        str: Path to the saved HTML plot.
    """
    template = "plotly_white" if theme == "light" else "plotly_dark"

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
        template=template,
        hovermode="x unified",
        width=650,
        height=350
    )


    html = fig.to_html(include_plotlyjs = "cdn")

    # Add dark background to entire page when in dark mode
    if theme == "dark":
        html = f"""
        <html>
        <head>
        <style>
            body {{
                margin: 0;
                background-color: #1e1e1e;
                color: #e0e0e0;
            }}
        </style>
        </head>
        <body>
        {html}
        </body>
        </html>
        """
    else:
        # For light mode, remove margin as well
        html = f"""
        <html>
        <head>
        <style>
            body {{
                margin: 0;
                background-color: white;
                color: black;
            }}
        </style>
        </head>
        <body>
        {html}
        </body>
        </html>
        """

    # Save plot to an HTML file
    # output_dir = "plots"
    # os.makedirs(output_dir, exist_ok=True)
    # file_path = os.path.join(output_dir, f"{ticker}_plot.png")
    # fig.write_image(file_path)

    return html
