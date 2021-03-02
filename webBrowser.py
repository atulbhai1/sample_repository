from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
import sys
class MainWindow(QMainWindow):
    def __init__(self):
        # noinspection PyArgumentList
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        navbar = QToolBar()
        self.addToolBar(navbar)
        back_btn = QAction('⬅️', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        re_btn = QAction('🔄', self)
        re_btn.triggered.connect(self.browser.reload)
        navbar.addAction(re_btn)
        for_btn = QAction('➡️', self)
        for_btn.triggered.connect(self.browser.forward)
        navbar.addAction(for_btn)
        home_btn = QAction('🏠', self)
        home_btn.triggered.connect(lambda :self.browser.setUrl(QUrl('https://google.com')))
        navbar.addAction(home_btn)
        url_bar = QLineEdit()
        url_bar.returnPressed.connect(lambda :self.browser.setUrl(QUrl('https://' + url_bar.text())))
        navbar.addWidget(url_bar)
        self.browser.urlChanged.connect(lambda :url_bar.setText(self.browser.url().toString()))
app = QApplication(sys.argv)
QApplication.setApplicationName('Browser')
window = MainWindow()
app.exec()