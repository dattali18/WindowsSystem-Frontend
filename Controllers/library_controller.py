from PySide6.QtWidgets import QTableWidgetItem

from Views import LibraryView
from Models import Models, MediaDto, GetLibraryDto
from typing import Optional


class LibraryController:
    """
    The LibraryController class is responsible for managing the operations of the library window.

    This includes tasks such as adding, removing, or updating books in the library, managing user accounts,
    and handling book checkouts and returns.

    Attributes:
        None

    Methods:
        To be defined.
    """

    def __init__(
        self,
        view: LibraryView,
        model: Models,
        library_id: int,
    ):
        self.view = view
        self.model = model
        self.library_id = library_id

        self.library: Optional[GetLibraryDto] = None
        self.media: Optional[list[MediaDto]] = None

        # contecting to signal
        self.view.search_button.clicked.connect(self.handle_search)

    def show(self):
        self.fetch_library()
        self.setUpWidgets()
        self.view.show()

    def fetch_library(self):
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
        if self.media is None:
            return

        self.view.media_table.setRowCount(len(self.media))

        for i, media in enumerate(self.media):
            self.view.media_table.setItem(i, 0, QTableWidgetItem(media["title"]))
            self.view.media_table.setItem(i, 1, QTableWidgetItem(media["year"]))
            self.view.media_table.setItem(i, 2, QTableWidgetItem(media["type"]))
            self.view.media_table.setItem(i, 3, QTableWidgetItem(media["imdbID"]))

    def handle_search(self):
        search_term = self.view.search_bar.text()
        if search_term == "":
            self.media = self.library.media
        else:
            # self.media = self.media.filter(lambda x: search_term in x.title)
            self.media = [x for x in self.media if search_term in x.title]

        # handle the combo box choice
        filter = self.view.filter_combo.currentText()
        if filter == "Movies":
            # self.media = self.media.filter(lambda x: x.type.lower() == "movie")
            self.media = [x for x in self.media if x["type"].lower() == "movie"]
        elif filter == "TV Series":
            # self.media = self.media.filter(lambda x: x.type.lower() == "series")
            self.media = [x for x in self.media if x["type"].lower() == "series"]

        self.populate_media_table()
