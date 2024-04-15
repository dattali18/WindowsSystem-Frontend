from typing import Optional

from Views import UpdateLibraryView
from Models import Models, GetLibraryDto, MediaDto


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
        self.view.media_table.cellDoubleClicked\
            .connect(self.handle_media_click)
        self.view.search_media_table.cellDoubleClicked\
            .connect(self.handle_search_click)
        self.view.update_button.clicked.connect(self.handle_update)

    def handle_search(self) -> None:
        # TODO: for Yair
        pass

    def handle_add(self) -> None:
        # TODO: for Yair
        pass

    def handle_remove(self) -> None:
        # TODO: for Yair
        pass

    def handle_update(self) -> None:
        # TODO: for Yair
        pass

    def handle_media_click(self) -> None:
        # TODO: for Yair
        pass

    def handle_search_click(self) -> None:
        # TODO: for Yair
        pass

    def show(self) -> None:
        self.fetch_library()
        self.populate_tables()
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

        self.media = self.library.media

    def populate_media_table(self) -> None:
        # TODO: for Yair
        pass

    def populate_search_table(self) -> None:
        # TODO: for Yair
        pass

    def populate_tables(self) -> None:
        self.populate_media_table()
        self.populate_search_table()
