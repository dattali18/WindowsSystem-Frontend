from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QLineEdit,
    QLabel,
    QComboBox,
)
from PySide6.QtGui import QAction
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader

import sys
from typing import Optional

from .form_ui import Ui_MainWindow
from .form_1_ui import Ui_MainWindow as Ui_frame_1
from Models import *


class MediaViewWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MediaViewWindow, self).__init__()
        self.ui = Ui_frame_1()
        self.ui.setupUi(self)


class LibrariesViewWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LibrariesViewWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class MediaController:
    def __init__(self, view: MediaViewWindow, model: MoviesModel):
        self.view = view.ui
        self.window = view
        self.model = model

        self.media: Optional[list[MediaDto]] = None

        # Defining the component
        self.search_btn: QPushButton = self.view.search_btn
        self.search_field: QLineEdit = self.view.search_field
        self.combo_box: QComboBox = self.view.combo_box
        self.media_table: QTableWidget = self.view.media_table

        self.add_random_data_for_debug()
        self.populate_media_table()

    def populate_media_table(self):
        # deleting all the old entries
        self.view.media_table.setRowCount(0)
        self.view.media_table.setColumnCount(5)

        self.view.media_table.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.view.media_table.setHorizontalHeaderItem(1, QTableWidgetItem("Title"))
        self.view.media_table.setHorizontalHeaderItem(2, QTableWidgetItem("Year"))
        self.view.media_table.setHorizontalHeaderItem(3, QTableWidgetItem("Type"))
        self.view.media_table.setHorizontalHeaderItem(4, QTableWidgetItem("Imdb ID"))

        if self.media is None:
            print("404 error please check backend")
            return

        self.view.media_table.setRowCount(len(self.media))

        for i, media in enumerate(self.media):
            self.view.media_table.setItem(i, 0, QTableWidgetItem(str(media.id)))
            self.view.media_table.setItem(i, 1, QTableWidgetItem(media.title))
            self.view.media_table.setItem(i, 2, QTableWidgetItem(media.year))
            self.view.media_table.setItem(i, 3, QTableWidgetItem(media.type))
            self.view.media_table.setItem(i, 4, QTableWidgetItem(media.imdbID))

        self.view.media_table.horizontalHeader().setStretchLastSection(True)
        self.view.media_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

    def add_random_data_for_debug(self):
        # create a list of MediaDto objects to test the ui
        self.media = [
            MediaDto(
                id=1,
                title="Test Title 1",
                year="2022",
                type="Movie",
                poster="",
                imdbID="tt1234567",
            ),
            MediaDto(
                id=2,
                title="Test Title 2",
                year="2022",
                type="Movie",
                poster="",
                imdbID="tt1234567",
            ),
            MediaDto(
                id=3,
                title="Test Title 3",
                year="2022",
                type="Movie",
                poster="",
                imdbID="tt1234567",
            ),
        ]


class LibrariesController:
    def __init__(self, view: LibrariesViewWindow, model: LibrariesModel):
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
