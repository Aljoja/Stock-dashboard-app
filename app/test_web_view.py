# import os
# os.environ["QTWEBENGINE_DISABLE_SANDBOX"] = "1"
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)
view = QWebEngineView()
view.setHtml("<h1>Hello from PyQt5 WebEngine!</h1>")

view.show()
sys.exit(app.exec())