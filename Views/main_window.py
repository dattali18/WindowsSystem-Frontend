from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QAction
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
import sys

from .form_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class Controller:
    def __init__(self, view: MainWindow):
        self.view = view.ui

        self.search_btn: QPushButton = self.view.search_btn
        self.search_btn.clicked.connect(self.handle_search_btn_click)
        self.search_action: QAction = self.view.actionSearch
        self.search_action.triggered.connect(self.handle_search_btn_click)

    def handle_search_btn_click(self):
        print("Search Btn Clicked")
