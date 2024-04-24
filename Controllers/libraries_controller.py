from typing import Optional

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox

# for creating a new library
from .create_library_controller import CreateLibraryController

# for updating a library, by adding & removing media from it
from .update_library_controller import UpdateLibraryController

# for seeing the content of a library
from .library_controller import LibraryController

from Views import LibrariesView, CreateLibraryView, UpdateLibraryView, LibraryView

from Models import LibrariesModel, Models
from Dto import GetLibraryDto


class LibrariesController:
    def __init__(self, view: LibrariesView, model: LibrariesModel):
        self.view = view
        self.model = model

        self.libraries: Optional[list[GetLibraryDto]] = []

        self.update_library_controller = UpdateLibraryController(
            view=UpdateLibraryView(),
            model=Models(),
            library_id=None,
        )

        self.create_library_controller = CreateLibraryController(
            view=CreateLibraryView(),
            model=LibrariesModel(),
        )

        self.library_controller = LibraryController(
            view=LibraryView(),
            model=LibrariesModel(),
        )

        self.view.search_button.clicked.connect(self.handle_search)
        self.view.add_button.clicked.connect(self.handle_create)
        self.view.update_button.clicked.connect(self.handle_update)
        self.view.delete_button.clicked.connect(self.handle_delete)

        self.view.table_widget.cellDoubleClicked.connect(self.handle_click)

        # self.create_random_data_for_debug()
        # self.populate_libraries_table()
        self.handle_search()

    def get_checked_keywords(self):
        keywords = []
        for checkbox in self.view.checkboxes.values():
            if checkbox.isChecked():
                keywords.append(checkbox.text())
        return keywords

    def handle_search(self):
        search_term: str = self.view.search_bar.text()
        # keywords = self.get_checked_keywords()

        if search_term == "":
            self.libraries = self.model.get_libraries()
        else:
            self.libraries = self.model.get_libraries_name(name=search_term)
        self.populate_libraries_table()

    def handle_delete(self):
        # TODO: ask the user with a dialog if they are sure they want to delete the library
        confirmation = QMessageBox.question(
            self.view,
            "Delete Library",
            "Are you sure you want to delete this library?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if confirmation != QMessageBox.Yes:
            return

        # User confirmed deletion, proceed with deleting the library
        selected_row: int = self.view.table_widget.currentRow()
        if selected_row == -1:
            print("No library selected")
            return
        library = self.libraries[selected_row]
        success: bool = self.model.delete_libraries_id(id=library.id)
        if not success:
            print("Error deleting library")
            return
        self.handle_search()

    def handle_create(self):
        # will create and show a new create library controller
        self.create_library_controller.view.show()

    def handle_update(self):
        # getting the selected library
        selected_row: int = self.view.table_widget.currentRow()
        if selected_row == -1:
            print("No library selected")
            return
        library = self.libraries[selected_row]
        # will create and show a new update library controller
        self.update_library_controller.library_id = library.id
        self.update_library_controller.show()

    def handle_click(self, row: int, column: int):
        # will create and show a new library controller
        library = self.libraries[row]

        self.library_controller.library_id = library.id
        self.library_controller.show()

        # self.view.close()

    def populate_libraries_table(self):
        # deleting all the old entries
        self.view.table_widget.setRowCount(0)

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
