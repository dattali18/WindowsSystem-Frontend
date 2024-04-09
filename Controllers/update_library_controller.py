from Views import UpdateLibraryView
from Models import LibraryModel


class UpdateLibraryController:
    def __init__(self, view: UpdateLibraryView, model: LibraryModel) -> None:
        self.view = view
        self.model = model
