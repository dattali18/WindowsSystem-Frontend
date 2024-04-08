from Views import *
from Models import LibrariesModel, MoviesModel, GetLibraryDto

from PySide6.QtWidgets import (
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QLineEdit,
)

from typing import Optional


class LibrariesController:
    def __init__(self, view: LibrariesView, model: LibrariesModel):
        self.view = view
        self.model = model

        self.libraries: Optional[list[GetLibraryDto]] = []

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
        if self.movie_controller.movie is not None:
            self.movie_controller.window.show()

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

    def create_random_data_for_debug(self):
        self.libraries = [
            GetLibraryDto(
                id=0,
                name="Star Wars",
                keywords=",".join(["Action", "Sci-Fi"]),
                media=[],
            ),
            GetLibraryDto(
                id=1,
                name="Lord of the Rings",
                keywords=",".join(["Action", "Fantasy"]),
                media=[],
            ),
            GetLibraryDto(
                id=2,
                name="Harry Potter",
                keywords=",".join(["Action", "Fantasy"]),
                media=[],
            ),
            GetLibraryDto(
                id=3,
                name="Game of Thrones",
                keywords=",".join(["Action", "Fantasy"]),
                media=[],
            ),
        ]
