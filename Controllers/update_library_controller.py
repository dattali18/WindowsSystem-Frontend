from Views import UpdateLibraryView
from Models import LibrariesModel


class UpdateLibraryController:
    def __init__(self, view: UpdateLibraryView, model: LibrariesModel) -> None:
        self.view = view
        self.model = model
