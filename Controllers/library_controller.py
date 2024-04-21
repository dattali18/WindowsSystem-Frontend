from typing import Optional

from PySide6.QtWidgets import QTableWidgetItem

from .media_controller import MediaController
from .create_library_controller import CreateLibraryController
from Views import LibraryView, MediaView, CreateLibraryView
from Models import LibrariesModel, MediaDto, GetLibraryDto


class LibraryController:
    """
    The LibraryController class is responsible for managing the operations of
    the library window.


    This includes tasks such as adding, removing, or updating books in the
    library, managing user accounts, and handling book checkouts and returns.

    Attributes:
        view: LibraryView
        model: Models
        library_id: Optional[int]
        library: Optional[GetLibraryDto]
        media: Optional[list[MediaDto]]
        media_controller: MediaController

    Methods:
        show: None -> None, This method is responsible for showing the library
        fetch_library: None, This method is responsible for fetching the library
        set_up_ui: None, This method is responsible for setting up the UI
        populate_media_table: None, This method is responsible for populating the media table
        handle_search: None, This method is responsible for handling the search
        handle_media_click: None, This method is responsible for handling the media click
        handle_update: None, This method is responsible for handling the update
    """

    def __init__(
        self,
        view: LibraryView,
        model: LibrariesModel,
    ):
        self.view = view
        self.model = model
        self.library_id: Optional[int] = None

        self.library: Optional[GetLibraryDto] = None
        self.media: Optional[list[MediaDto]] = None

        self.media_controller = MediaController(view=MediaView())
        self.create_library_controller = CreateLibraryController(
            view=CreateLibraryView(), model=LibrariesModel()
        )

        # connecting to signal
        self.view.search_button.clicked.connect(self.handle_search)
        self.view.media_table.cellDoubleClicked.connect(self.handle_media_click)
        self.view.update_button.clicked.connect(self.handle_update)

    def show(self) -> None:
        self.fetch_library()
        self.set_up_ui()
        self.view.show()

    def fetch_library(self) -> None:
        if not self.library_id:
            print("No Library Id found")
            return
        self.library = self.model.get_library_id(self.library_id)

        if self.library is None:
            print("404 error - library not found")
            # close the window
            self.view.close()

        self.library.media = [MediaDto(**media) for media in self.library.media]
        self.media = self.library.media

    def set_up_ui(self) -> None:
        if self.library is None:
            return

        self.view.title_label.setText(self.library.name)
        self.populate_media_table()

    def populate_media_table(self) -> None:
        self.view.media_table.setRowCount(0)

        if self.media is None:
            return

        self.view.media_table.setRowCount(len(self.media))

        for i, media in enumerate(self.media):
            self.view.media_table.setItem(i, 0, QTableWidgetItem(media.title))
            self.view.media_table.setItem(i, 1, QTableWidgetItem(media.year))
            self.view.media_table.setItem(i, 2, QTableWidgetItem(media.type))
            self.view.media_table.setItem(i, 3, QTableWidgetItem(media.imdbID))

    def handle_search(self) -> None:
        search_term = self.view.search_bar.text()
        if search_term == "":
            self.media = self.library.media
        else:
            self.media = [x for x in self.media if search_term in x.title]

        # handle the combo box choice
        filter = self.view.filter_combo.currentText()
        if filter == "Movies":
            self.media = [x for x in self.media if x.type.lower() == "movie"]
        elif filter == "TV Series":
            self.media = [x for x in self.media if x.type.lower() == "series"]

        self.populate_media_table()

    def handle_media_click(self, row: int, column: int) -> None:
        media = self.media[row]
        self.media_controller.media = media
        self.media_controller.show()

    def handle_update(self) -> None:
        if self.library is None:
            return
        self.create_library_controller.library_id = self.library_id
        self.create_library_controller.show()
        self.view.close()
