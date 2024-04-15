from typing import Optional

from PySide6.QtWidgets import QTableWidgetItem

from .media_controller import MediaController
from Views import LibraryView, MediaView
from Models import Models, MediaDto, GetLibraryDto


class LibraryController:
    """
    The LibraryController class is responsible for managing the operations of the library window.

    This includes tasks such as adding, removing, or updating books in the library, managing user accounts,
    and handling book checkouts and returns.

    Attributes:
        view: LibraryView
        model: Models
        library_id: Optional[int]
        library: Optional[GetLibraryDto]
        media: Optional[list[MediaDto]]
        media_controller: MediaController

    Methods:
        To be defined.
    """

    def __init__(
        self,
        view: LibraryView,
        model: Models,
    ):
        self.view = view
        self.model = model
        self.library_id: Optional[int] = None

        self.library: Optional[GetLibraryDto] = None
        self.media: Optional[list[MediaDto]] = None

        self.media_controller = MediaController(view=MediaView())

        # connecting to signal
        self.view.search_button.clicked.connect(self.handle_search)
        self.view.media_table.cellDoubleClicked.connect(
            self.handle_media_click)

    def show(self):
        self.fetch_library()
        self.setUpWidgets()
        self.view.show()

    def fetch_library(self):
        if not self.library_id:
            print("No Library Id found")
            return

        self.library = self.model.libraries.get_library_id(self.library_id)

        if self.library is None:
            print("404 error - library not found")
            # close the window
            self.view.close()

        self.media = self.library.media

    def setUpWidgets(self):
        if self.library is None:
            return

        self.view.title_label.setText(self.library.name)
        self.populate_media_table()

    def populate_media_table(self):
        self.view.media_table.setRowCount(0)

        if self.media is None:
            return

        self.view.media_table.setRowCount(len(self.media))

        self.media = MediaDto(**self.media)

        for i, media in enumerate(self.media):
            self.view.media_table.setItem(i, 0, QTableWidgetItem(media.title))
            self.view.media_table.setItem(i, 1, QTableWidgetItem(media.year))
            self.view.media_table.setItem(i, 2, QTableWidgetItem(media.type))
            self.view.media_table.setItem(i, 3, QTableWidgetItem(media.imdbID))

    def handle_search(self):
        search_term = self.view.search_bar.text()
        if search_term == "":
            self.media = self.library.media
        else:
            self.media = [x for x in self.media if search_term in x.title]

        # handle the combo box choice
        filter = self.view.filter_combo.currentText()
        if filter == "Movies":
            self.media = [x for x in self.media if x["type"].lower()
                          == "movie"]
        elif filter == "TV Series":
            self.media = [x for x in self.media if x["type"].lower()
                          == "series"]

        self.populate_media_table()

    def handle_media_click(self, row: int, column: int):
        media = self.media[row]
        self.media_controller.media = media
        self.media_controller.show()
