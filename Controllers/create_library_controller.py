from Views import CreateLibraryView
from Models import LibrariesModel


class CreateLibraryController:
    def __init__(self, view: CreateLibraryView, model: LibrariesModel) -> None:
        self.view = view
        self.model = model
