from Views import UpdateLibraryView
from Models import LibrariesModel


class UpdateLibraryController:
    def __init__(
        self, view: UpdateLibraryView, model: LibrariesModel, library_id: int
    ) -> None:
        self.view = view
        self.model = model
        self.library_id = library_id
