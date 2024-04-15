from PySide6.QtWidgets import QTableWidgetItem, QMessageBox

from typing import Optional


from Views import UpdateLibraryView
from Models import Models, MediaDto, GetLibraryDto


class UpdateLibraryController:
    def __init__(
        self, view: UpdateLibraryView, model: Models, library_id: Optional[int]
    ) -> None:
        self.view = view
        self.model = model
        self.library_id = library_id

        self.library: Optional[GetLibraryDto] = None
        self.media: Optional[list[MediaDto]] = []
        self.search_results: Optional[list[MediaDto]] = []

        # 1. handle signals
        self.view.search_button.clicked.connect(self.handle_search)
        self.view.add_button.clicked.connect(self.handle_add)
        self.view.remove_button.clicked.connect(self.handle_remove)
        self.view.media_table.cellDoubleClicked.connect(self.handle_media_click)
        self.view.search_media_table.cellDoubleClicked.connect(self.handle_search_click)
        self.view.update_button.clicked.connect(self.handle_update)

    def show(self) -> None:
        self.fetch_library()
        self.set_up_ui()
        self.view.show()

    def fetch_library(self) -> None:
        if not self.library_id:
            print("No Library Id found")
            return

        self.library = self.model.libraries.get_library_id(id=self.library_id)

        if self.library is None:
            print("404 error - library not found")
            # close the window
            self.view.close()

        self.media = [MediaDto(**media) for media in self.library.media]

    def set_up_ui(self) -> None:
        self.view.title_label.setText(self.library.name)

        self.populate_tables()

    def populate_tables(self) -> None:
        self.populate_search_table()
        self.populate_media_table()

    def populate_search_table(self):
        self.view.search_media_table.setRowCount(0)

        if self.search_results is None:
            print("404 error please check backend")
            return

        self.view.search_media_table.setRowCount(len(self.search_results))

        for i, media in enumerate(self.search_results):
            self.view.search_media_table.setItem(i, 0, QTableWidgetItem(media.title))
            self.view.search_media_table.setItem(i, 1, QTableWidgetItem(media.year))
            self.view.search_media_table.setItem(i, 2, QTableWidgetItem(media.type))
            self.view.search_media_table.setItem(i, 3, QTableWidgetItem(media.imdbID))

    def populate_media_table(self):
        self.view.media_table.setRowCount(0)

        if self.media is None:
            print("404 error please check backend")
            return

        self.view.media_table.setRowCount(len(self.media))

        for i, media in enumerate(self.media):
            self.view.media_table.setItem(i, 0, QTableWidgetItem(media.title))
            self.view.media_table.setItem(i, 1, QTableWidgetItem(media.year))
            self.view.media_table.setItem(i, 2, QTableWidgetItem(media.type))
            self.view.media_table.setItem(i, 3, QTableWidgetItem(media.imdbID))

    def handle_search(self):
        search_text = self.view.search_bar.text()

        if search_text == "":
            QMessageBox.information(self, "Error", "Need to input search text!")
            return

        media_type = self.view.filter_combo.currentText()

        print(f"Searching for {search_text} in {media_type}")

        if media_type == "Movies":
            self.search_results = self.model.movies.get_movies_search(search_text)
        else:
            self.search_results = self.model.tvseries.get_tv_series_search(search_text)

        self.populate_search_table()

    def handle_add(self):
        # get the current selected row on search media table
        selected_row: int = self.view.search_media_table.currentRow()

        # handle if no row is selected
        if selected_row == -1:
            QMessageBox.information(self, "Error", "Need to select Media to add!")
            return

        # get imdbID and type of the selected row

        selected_imdbID = self.search_results[selected_row].imdbID
        selected_type = self.search_results[selected_row].type

        dto: Optional[MediaDto] = None

        if selected_type == "Movies":
            dto = self.model.libraries.post_libraries_movies(
                library_id=self.library_id, imdbID=selected_imdbID
            )
        else:
            dto = self.model.libraries.post_libraries_tvseries(
                library_id=self.library_id, imdbID=selected_imdbID
            )

        if dto is None:
            print("404 error please check backend")
            return

        # recall the media from the backend
        self.fetch_library()
        self.populate_media_table()

    def handle_remove(self):
        # get the selected row
        selected_row: int = self.view.media_table.currentRow()

        # handle if no row is selected
        if selected_row == -1:
            QMessageBox.information(self, "Error", "Need to select Media to remove!")
            return

        selected_imdbID = self.media[selected_row].imdbID
        selected_type = self.media[selected_row].type

        success: bool = False

        if selected_type == "Movies":
            success = self.model.libraries.delete_libraries_movies(
                library_id=self.library_id, imdbID=selected_imdbID
            )
        else:
            success = self.model.libraries.delete_libraries_tvseries(
                library_id=self.library_id, imdbID=selected_imdbID
            )

        if not success:
            print("404 error please check backend")
            return

        # recall the fetch methods
        self.fetch_library()
        self.populate_media_table()

    def handle_media_click(self, row, col):
        # get the selected row
        selected_row: int = self.view.media_table.currentRow()

        # handle if no row is selected
        if selected_row == -1:
            QMessageBox.information(self, "Error", "Need to select Media to remove!")
            return

        selected_imdbID = self.media[selected_row].imdbID
        selected_type = self.media[selected_row].type

        success: bool = False

        if selected_type == "Movies":
            success = self.model.libraries.delete_libraries_movies(
                library_id=self.library_id, imdbID=selected_imdbID
            )
        else:
            success = self.model.libraries.delete_libraries_tvseries(
                library_id=self.library_id, imdbID=selected_imdbID
            )

        if not success:
            print("404 error please check backend")
            return

        # recall the fetch methods
        self.fetch_library()
        self.populate_media_table()

    def handle_search_click(self, row, col):
        # get imdbID and type of the selected row
        selected_imdbID = self.search_results[row].imdbID
        selected_type = self.search_results[row].type

        print(f"{selected_imdbID=} {selected_type=}")

        dto: Optional[MediaDto] = None

        if selected_type == "movie":
            dto = self.model.libraries.post_libraries_movies(
                library_id=self.library_id, imdbID=selected_imdbID
            )
        else:
            dto = self.model.libraries.post_libraries_tvseries(
                library_id=self.library_id, imdbID=selected_imdbID
            )

        if dto is None:
            print("404 error please check backend")
            return

        # recall the media from the backend
        self.fetch_library()
        self.populate_media_table()

    def handle_update(self):
        self.view.close()
