from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QLineEdit,
    QLabel
)
from PySide6.QtGui import QAction
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader

import sys
from typing import Optional

from .form_ui import Ui_MainWindow
from .form_1_ui import Ui_MainWindow as Ui_frame_1
from Models import *

class Frame1Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Frame1Window, self).__init__()
        self.ui = Ui_frame_1()
        self.ui.setupUi(self)

        label = QLabel("<font color=red size=40>Hello World!</font>")
        self.ui.frame_1 = label
        button = QPushButton("Click me")
        self.ui.frame_2 = button


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class Controller:
    def __init__(self, view: MainWindow, model: LibrariesModel):
        self.view = view.ui
        self.window = view
        self.model = model

        self.search_field: QLineEdit = self.view.search_field

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

        self.view.libraries_table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        self.view.libraries_table.cellClicked.connect(self.handle_click)

        self.libraries: Optional[list[GetLibraryDto]] = self.model.get_libraries()
        self.populate_libraries_table()

    def handle_search(self):
        search_term: str = self.search_field.text()
        if search_term == "":
            self.libraries = self.model.get_libraries()
        else:
            self.libraries = self.model.get_libraries_name(name=search_term)
        self.populate_libraries_table()

    def handle_create(self):
        print("create")

    def handle_update(self):
        print("update")

    def handle_click(self, row: int, column: int):
        print(f"item clicked at {row=}, {column=}")

    def populate_libraries_table(self):
        # deleting all the old entries
        self.view.libraries_table.setRowCount(0)

        if self.libraries is None:
            print("404 error please check backend")
            return

        self.view.libraries_table.setColumnCount(3)
        self.view.libraries_table.setRowCount(len(self.libraries))

        self.view.libraries_table.setHorizontalHeaderItem(0, QTableWidgetItem("Title"))
        self.view.libraries_table.setHorizontalHeaderItem(
            1, QTableWidgetItem("Keywords")
        )
        self.view.libraries_table.setHorizontalHeaderItem(2, QTableWidgetItem("Media"))

        for i, library in enumerate(self.libraries):
            self.view.libraries_table.setItem(i, 0, QTableWidgetItem(library.name))
            self.view.libraries_table.setItem(
                i, 1, QTableWidgetItem(", ".join(library.keywords))
            )
            self.view.libraries_table.setItem(
                i, 2, QTableWidgetItem(f"{len(library.media)}")
            )

        self.view.libraries_table.horizontalHeader().setStretchLastSection(True)
        self.view.libraries_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )
        # self.view.libraries_table.verticalHeader().setStretchLastSection(True)
        # self.view.libraries_table.verticalHeader().setSectionResizeMode(
        #     QHeaderView.Stretch
        # )
