import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from app.ui import StockDashboard

def main():
    """
    Entry point for the Stock Dashboard application.

    Initializes the PyQt application, creates the main window,
    and starts the event loop.
    """

    app = QApplication(sys.argv)          # Create the application instance
    window = StockDashboard()             # Create the main dashboard window
    window.show()                         # Show the window
    sys.exit(app.exec_())                 # Start the event loop

if __name__ == "__main__":
    main()
