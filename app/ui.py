from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QLabel, QMenuBar, QAction, QHBoxLayout, QButtonGroup, QToolButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt
from core.stock_api import fetch_stock_data
from core.plotter import plot_stock_data_html

class StockDashboard(QMainWindow):
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

        # Initial settings
        self.setWindowTitle("📈 Stock Dashboard App")
        self.setMinimumSize(1000, 800)

        self.theme = "dark"  # default theme
        self.current_range = "1mo"  # default time range

        # Create central widget and grid layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        # Input field for stock ticker
        self.ticker_input = QLineEdit()
        self.ticker_input.setPlaceholderText("Enter stock ticker (e.g. AAPL)")
        self.ticker_input.setMinimumWidth(200)
        self.layout.addWidget(self.ticker_input, 0, 0)

        # Fetch button
        self.fetch_button = QPushButton("Fetch Stock Data")
        self.fetch_button.setFixedWidth(150)
        self.fetch_button.clicked.connect(self.fetch_and_plot)
        self.layout.addWidget(self.fetch_button, 0, 1, alignment=Qt.AlignLeft)

        # --- Row 1: Error Label ---

        # Error message display
        self.error_label = QLabel("")
        self.layout.addWidget(self.error_label, 0, 3, 1, 2)

        # --- Row 2: Time Range Buttons ---

        # Time range buttons layout
        self.range_button_layout = QHBoxLayout()

        # Range button group (only one selected at a time)
        self.range_buttons = QButtonGroup()
        self.range_buttons.setExclusive(True)

        # Define time range options
        self.range_options = {
            "1W": "7d",
            "1M": "1mo",
            "3M": "3mo",
            "1Y": "1y"
        }

        for i, (label, value) in enumerate(self.range_options.items()):
            btn = QToolButton()
            btn.setText(label)
            btn.setCheckable(True)
            btn.setMinimumWidth(60)
            btn.setStyleSheet("margin-right: 5px;")
            if value == self.current_range:
                btn.setChecked(True)
            self.range_buttons.addButton(btn, id=i)
            self.range_button_layout.addWidget(btn)

        # Connect selection signal
        self.range_buttons.buttonClicked[int].connect(self.on_range_selected)

        # Add time range button layout above chart
        self.layout.addLayout(self.range_button_layout, 1, 0, 1, 2, alignment=Qt.AlignLeft)

        # --- Row 3: Chart View ---

        # Area to display interactive chart
        self.chart_view = QWebEngineView()
        self.layout.addWidget(self.chart_view, 2, 0, 1, 2)



        # Grid spacing and margins
        self.layout.setColumnStretch(0, 1)  # Input takes 1x space
        self.layout.setColumnStretch(1, 1)  # Button takes 1x space
        self.layout.setHorizontalSpacing(10)
        self.layout.setVerticalSpacing(10)
        self.layout.setContentsMargins(20, 20, 20, 20)

        # Add the menu area (theme switcher)
        self.create_menu()

        # Load empty chart where the chart will be loaded
        self.load_empty_chart()

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
            data = fetch_stock_data(ticker, period=self.current_range)

            # Generate interactive chart HTML
            html = plot_stock_data_html(data, ticker, self.theme)
            
            # Display chart in web view
            self.chart_view.setHtml(html)
            self.error_label.setText("")  # Clear any previous error

        except Exception as e:
            # Show error if something goes wrong
            self.error_label.setText(f"Error: {str(e)}")

    def create_menu(self):
        """
        Creates the menu bar and theme switcher.
        """
        menu_bar = self.menuBar()

        theme_menu = menu_bar.addMenu("Theme")

        light_action = QAction("Light", self)
        light_action.triggered.connect(self.set_light_mode)

        dark_action = QAction("Dark", self)
        dark_action.triggered.connect(self.set_dark_mode)

        theme_menu.addAction(light_action)
        theme_menu.addAction(dark_action)

    def set_light_mode(self):
        """
        Apply light mode stylesheet.
        """
        self.setStyleSheet("")
        self.theme = "light"
        self.load_empty_chart()
        self.refresh_chart()

    def set_dark_mode(self):
        """
        Apply dark mode stylesheet.
        """
        self.setStyleSheet("""
            QWidget { background-color: #1e1e1e; color: #e0e0e0; }
            QPushButton { background-color: #333; color: #fff; border: 1px solid #555; padding: 5px; }
            QLineEdit { background-color: #2e2e2e; color: #fff; border: 1px solid #555; }
            QMenuBar, QMenu { background-color: #2e2e2e; color: #fff; }
            QToolButton {
                background-color: #2a2a2a;
                color: white;
                border: 1px solid #444;
                padding: 5px 10px;
                border-radius: 4px;
            }
            QToolButton:checked {
                background-color: #444;
                font-weight: bold;
            }
        """)
        self.theme = "dark"
        self.load_empty_chart()
        self.refresh_chart()

    def refresh_chart(self):
        ticker = self.ticker_input.text().strip().upper()
        if not ticker:
            return
        try:
            data = fetch_stock_data(ticker)
            html = plot_stock_data_html(data, ticker, self.theme)
            self.chart_view.setHtml(html)
        except Exception as e:
            self.error_label.setText(f"Error: {e}")

    def load_empty_chart(self):
        """
        Load a blank, theme-matching HTML placeholder into the chart view.
        """
        if self.theme == "dark":
            html = """
            <html>
            <head>
            <style>
                body {
                    background-color: #1e1e1e;
                    margin: 0;
                }
            </style>
            </head>
            <body></body>
            </html>
            """
        else:
            html = """
            <html>
            <head>
            <style>
                body {
                    background-color: white;
                    margin: 0;
                }
            </style>
            </head>
            <body></body>
            </html>
            """
        self.chart_view.setHtml(html)

    def on_range_selected(self, button_id):
        """
        Handle time range button click, update current range and refresh chart.
        """
        label = self.range_buttons.button(button_id).text()
        self.current_range = self.range_options[label]
        self.fetch_and_plot()