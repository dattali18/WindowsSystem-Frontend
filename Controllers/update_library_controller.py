from Views import UpdateLibraryView
from Models import Models


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
        self.view.search_table.cellDoubleClicked.connect(self.handle_search_click)
        self.view.update_button.clicked.connect(self.handle_update)

    def show() -> None:
        self.fetch_library()
        self.populate_tables()
        self.view.show()

    def fetch_library() -> None:
        if not self.library_id:
            print("No Library Id found")
            return

        self.library = self.model.libraries.get_library_id(id=self.library_id)

        if self.library is None:
            print("404 error - library not found")
            # close the window
            self.view.close()

        self.media = self.library.media

    def populate_tables() -> None:
        self.populate_media_table()
        self.populate_search_table()
