from typing import Optional

from PySide6.QtWidgets import QTableWidgetItem, QHeaderView

from Views import LibrariesView
from Models import LibrariesModel
from Dto import MediaDto, GetLibraryDto


class LibrariesController:
    def __init__(self, view: LibrariesView, model: LibrariesModel):
        self.view = view
        self.model = model

        self.libraries: Optional[list[GetLibraryDto]] = []

        self.view.search_button.clicked.connect(self.handle_search)
        self.view.add_button.clicked.connect(self.handle_create)
        self.view.update_button.clicked.connect(self.handle_update)

        self.view.table_widget.cellClicked.connect(self.handle_click)

        self.create_random_data_for_debug()
        self.populate_libraries_table()

    def get_checked_keywords(self):
        keywords = []
        for checkbox in self.view.checkboxes.values():
            if checkbox.isChecked():
                keywords.append(checkbox.text())
        return keywords

    def handle_search(self):
        search_term: str = self.view.search_bar.text()
        keywords = self.get_checked_keywords()

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
        self.view.table_widget.setRowCount(1)

        if self.libraries is None:
            print("404 error please check backend")
            return

        self.view.table_widget.setRowCount(len(self.libraries))

        for i, library in enumerate(self.libraries):
            self.view.table_widget.setItem(i, 0, QTableWidgetItem(library.name))
            self.view.table_widget.setItem(
                i, 1, QTableWidgetItem(", ".join(library.keywords))
            )
            self.view.table_widget.setItem(
                i, 2, QTableWidgetItem(f"{len(library.media)}")
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
