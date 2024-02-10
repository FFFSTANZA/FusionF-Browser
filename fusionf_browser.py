import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import * 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        navbar = QToolBar(self)
        self.addToolBar(navbar)
        actions = [
            ('Back', self.browser.back),
            ('Forward', self.browser.forward),
            ('Reload', self.browser.reload),
            ('Home', self.navigate_home)
        ]

        for text, method in actions:
            action = QAction(text, self)
            action.triggered.connect(method)
            navbar.addAction(action)
      
        self.url_bar = QLineEdit(self)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
       
        spacer = QWidget(self)
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        navbar.addWidget(spacer)
      
        refresh_btn = QAction('Refresh', self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)
   
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        
        self.url_bar.setPlaceholderText("FusionF")

        # Styling
        self.setStyleSheet(
            "QToolBar { border: 1px solid #d4d4d4; background-color: #f8f8f8; }"
            "QLineEdit { padding: 5px; border: 1px solid #d4d4d4; border-radius: 3px; }"
        )

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName('FusionF Browser')
    # Set the application style (optional)
    app.setStyle("Fusion")
    window = MainWindow()
    sys.exit(app.exec_())
  
