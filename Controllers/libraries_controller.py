from PySide6.QtWidgets import QTableWidgetItem, QLineEdit, QHeaderView
from typing import Optional

from Models import GetLibraryDto, MediaDto, MovieDto, MoviesModel, LibrariesModel


class Frame1Controller:
    def __init__(
        self, libraries_model: LibrariesModel, movies_model: MoviesModel, frame_view
    ):
        self.libraries_model = libraries_model
        self.movies_model = movies_model
        self.frame_view = frame_view

        # Connect signals from the view to controller methods
        self.frame_view.back_btn.clicked.connect(self.handle_back_btn_clicked)
        self.frame_view.forward_btn.clicked.connect(self.handle_forward_btn_clicked)
        self.frame_view.search_btn.clicked.connect(self.handle_search_btn_clicked)
        self.frame_view.create_btn.clicked.connect(self.handle_create_btn_clicked)
        self.frame_view.update_btn.clicked.connect(self.handle_update_btn_clicked)

        self.search_field: QLineEdit = self.frame_view.search_field

    def populate_table_with_Libraries(self, libraries: list[GetLibraryDto]):
        self.frame_view.playlist_table.setRowCount(len(libraries) + 1)
        self.frame_view.playlist_table.setColumnCount(2)

        self.frame_view.playlist_table.setItem(0, 0, QTableWidgetItem("Title"))
        self.frame_view.playlist_table.setItem(0, 1, QTableWidgetItem("keywords"))

        # Populate the table with movies data
        for row, library in enumerate(libraries):
            self.frame_view.playlist_table.setItem(
                row + 1, 0, QTableWidgetItem(library.name)
            )
            self.frame_view.playlist_table.setItem(
                row + 1, 1, QTableWidgetItem(", ".join(library.keywords))
            )

        self.frame_view.playlist_table.horizontalHeader().setStretchLastSection(True)
        self.frame_view.playlist_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

    def handle_back_btn_clicked(self):
        # Handle back button click
        print("back button clicked")

    def handle_forward_btn_clicked(self):
        # Handle forward button click
        print("forward button clicked")

    def handle_search_btn_clicked(self):
        search_term: str = self.search_field.text()
        print(search_term)
        libraries: Optional[list[GetLibraryDto]] = (
            self.libraries_model.get_libraries_name(name=search_term)
        )
        if libraries is None:
            return
        self.populate_table_with_Libraries(libraries=libraries)

        self.populate_table_with_Libraries(libraries=libraries)
        # Handle search button click
        print("search button clicked")

    def handle_create_btn_clicked(self):
        # Handle create button click
        print("create button clicked")

    def handle_update_btn_clicked(self):
        # Handle update button click
        print("update button clicked")
