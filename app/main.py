import flet as ft
from core.stock_api import fetch_stock_data

def main(page: ft.Page):
    """
    Main function to initialize and run the Stock Dashboard App GUI.
    
    Args:
        page (flet.Page): The Flet page object representing the app window.
    """
        
    # Set page properties
    page.title = "📈 Stock Dashboard App"
    page.theme_mode = ft.ThemeMode.DARK  # or LIGHT
    page.window_width = 800
    page.window_height = 600
    page.padding = 20
    page.spacing = 20

    # App title
    title = ft.Text(
        value="Welcome to Stock Dashboard!",
        style="headlineMedium",
        text_align="center",
    )

    # Input field for stock ticker
    ticker_input = ft.TextField(
        label="Enter Stock Ticker (e.g., AAPL)",
        width=300,
        autofocus=True,
    )

    # Result text (to update later)
    result_text = ft.Text(
        value="",
        style="titleMedium",
        text_align="center",
    )

    def fetch_data_click(event):
        """
        Event handler for the 'Fetch Stock Data' button.
        Fetches stock data for the given ticker and updates the result text.

        Args:
            event (flet.ControlEvent): The event triggered by button click.
        """
        ticker = ticker_input.value.strip().upper()

        if not ticker:
            page.snack_bar = ft.SnackBar(ft.Text("Please enter a stock ticker!"))
            page.snack_bar.open()
            return
        
        try:
            # Fetch stock data
            data = fetch_stock_data(ticker)
            
            # Get the latest closing price
            latest_close = data["Close"].iloc[-1]
            
            # Update result text
            result_text.value = f"Latest closing price for {ticker}: ${latest_close:.2f}"
            page.update()

        except Exception as e:
            page.snack_bar = ft.SnackBar(ft.Text(f"Error: {e}"))
            page.snack_bar.open()


    # Button to fetch stock data
    fetch_button = ft.ElevatedButton(
        text="Fetch Stock Data",
        on_click = fetch_data_click
    )

    # Chart placeholder
    chart_placeholder = ft.Container(
        content=ft.Text(
            "📊 Chart will appear here...",
            text_align="center",
            style="bodyMedium",
        ),
        width=600,
        height=300,
        border=ft.border.all(1, ft.colors.GREY),
        alignment=ft.alignment.center,
    )

    # Add all elements to the page
    page.add(
        title,
        ft.Row([ticker_input, fetch_button], alignment="center"),
        chart_placeholder,
        result_text,
    )

# Run the app
if __name__ == "__main__":
    """
    Entry point for running the Flet application.
    """
    ft.app(target=main)