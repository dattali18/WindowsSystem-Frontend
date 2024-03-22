from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem, QHeaderView
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
        self.window = view

        self.search_btn: QPushButton = self.view.search_btn
        self.create_btn: QPushButton = self.view.create_btn
        self.update_btn: QPushButton = self.view.update_btn

        self.search_action: QAction = self.view.actionSearch
        self.create_action: QAction = self.view.actionCreate
        self.update_action: QAction = self.view.actionUpdate

        self.search_btn.clicked.connect(self.handle_search)
        self.search_action.triggered.connect(self.handle_search)

        self.create_btn.clicked.connect(self.handle_create)
        self.create_action.triggered.connect(self.handle_create)

        self.update_btn.clicked.connect(self.handle_update)
        self.update_action.triggered.connect(self.handle_update)

        # self.view.libraries_table: QTableWidget = self.view.libraries_view.libraries_table

        self.populate_libraries_table()

    def handle_search(self):
        print("search")

    def handle_create(self):
        print("create")

    def handle_update(self):
        print("update")

    def populate_libraries_table(self):
        self.view.libraries_table.setColumnCount(3)
        self.view.libraries_table.setRowCount(11)

        self.view.libraries_table.setItem(0, 0, QTableWidgetItem("Header 1"))
        self.view.libraries_table.setItem(0, 1, QTableWidgetItem("Header 2"))
        self.view.libraries_table.setItem(0, 2, QTableWidgetItem("Header 3"))

        for i in range(3):
            for j in range(10):
                self.view.libraries_table.setItem(j + 1, i, QTableWidgetItem("Some text"))

        self.view.libraries_table.horizontalHeader().setStretchLastSection(True)
        self.view.libraries_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        self.view.libraries_table.verticalHeader().setStretchLastSection(True)
        self.view.libraries_table.verticalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
