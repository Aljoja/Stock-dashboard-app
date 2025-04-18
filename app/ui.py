from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from core.stock_api import fetch_stock_data
from core.plotter import plot_stock_data_html

class StockDashboard(QWidget):
    """
    Main dashboard widget for the stock visualization app.
    Allows user to enter a stock ticker, fetch historical data,
    and display an interactive Plotly chart inside a PyQt window.
    """
    def __init__(self):
        """
        Initializes the GUI components: input field, button, chart area, and layout.
        """
        super().__init__()
        self.setWindowTitle("📈 Stock Dashboard App")
        self.setMinimumSize(900, 600)

        # Main vertical layout
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Input field for stock ticker
        self.ticker_input = QLineEdit()
        self.ticker_input.setPlaceholderText("Enter stock ticker (e.g. AAPL)")
        self.layout.addWidget(self.ticker_input, 0, 0)

        # Fetch button
        self.fetch_button = QPushButton("Fetch Stock Data")
        self.fetch_button.clicked.connect(self.fetch_and_plot)
        self.layout.addWidget(self.fetch_button, 0, 1)

        # Error message display
        self.error_label = QLabel("")
        self.layout.addWidget(self.error_label, 0, 3)

        # Area to display interactive chart
        self.chart_view = QWebEngineView()
        self.layout.addWidget(self.chart_view, 1, 0)

    def fetch_and_plot(self):
        """
        Handles the button click event:
        - Fetches historical stock data from Yahoo Finance
        - Generates a Plotly chart
        - Renders the chart in the GUI's web view
        """
        ticker = self.ticker_input.text().strip().upper()

        if not ticker:
            self.error_label.setText("Please enter a stock ticker.")
            return

        try:
            # Fetch data
            data = fetch_stock_data(ticker)

            # Generate interactive chart HTML
            html = plot_stock_data_html(data, ticker)
            
            # Display chart in web view
            self.chart_view.setHtml(html)
            self.error_label.setText("")  # Clear any previous error

        except Exception as e:
            # Show error if something goes wrong
            self.error_label.setText(f"Error: {str(e)}")
