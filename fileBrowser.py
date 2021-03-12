import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout
from PyQt5.QtCore import QModelIndex
class FileBrowser(QWidget):
    def __init__(self, dirPath):
        super(FileBrowser, self).__init__()
        appWidth = 800
        appHeight = 800
        self.setWindowTitle('File Browser')
        self.setGeometry(300, 300, appWidth, appHeight)
        self.model = QFileSystemModel()
        self.model.setRootPath(dirPath)
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(dirPath))
        self.tree.setColumnWidth(0, 250)
        self.tree.setAlternatingRowColors(True)
        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        self.setLayout(layout)
app = QApplication(sys.argv)
path = '/Users/srinivasansrinivasan'
fileBrowser = FileBrowser(path)
fileBrowser.show()
app.exec_()