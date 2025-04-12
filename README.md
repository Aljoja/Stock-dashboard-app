# 📈 Stock Dashboard App

A modern Stock Dashboard App built with Python — input stock tickers, fetch live data, visualize stock trends, and predict short-term prices using machine learning.  
Built with a sleek, professional GUI using [Flet](https://flet.dev/).

---

## ✨ Features

- Input one or multiple stock tickers (e.g., AAPL, TSLA, MSFT)
- Fetch live stock data (price and historical data) using Yahoo Finance API
- Visualize stock price trends with dynamic graphs
- Predict next day's stock price using a simple Linear Regression model
- Modern, responsive user interface with Flet
- Unit tested core logic with `pytest`
- Automated CI/CD pipeline with GitHub Actions
- Build standalone executable app (.exe or .app) using PyInstaller

---

## 📚 Tech Stack

| Area            | Technology                       |
|-----------------|-----------------------------------|
| Programming     | Python 3.11                       |
| GUI             | Flet                              |
| Data Fetching   | yfinance                           |
| Machine Learning| scikit-learn                      |
| Visualization   | matplotlib / plotly               |
| Testing         | pytest                            |
| CI/CD           | GitHub Actions                    |
| Packaging       | PyInstaller                       |
| Environment     | Conda (`environment.yml`)         |

---

## 🛠️ Project Structure

```plaintext
/stock-dashboard-app
├── app/
│   ├── main.py            # Entry point for Flet app
│   ├── views.py           # GUI layout
│   └── components.py      # Reusable GUI components
│
├── core/
│   ├── stock_api.py       # Fetch stock data
│   ├── predictor.py       # ML model for prediction
│   └── utils.py           # Utility functions
│
├── tests/
│   ├── test_stock_api.py
│   ├── test_predictor.py
│   └── test_utils.py
│
├── environment.yml        # Project environment setup
├── requirements.txt       # (Optional) pip dependencies
├── README.md               # Project documentation
├── .gitignore              # Files to ignore
└── .github/
    └── workflows/
        └── ci.yml         # GitHub Actions workflow
