from Views import CreateLibraryView
from Models import LibraryModel

class CreateLibraryController:
    def __init__(self, view: CreateLibraryView, model: LibraryModel) -> None:
        self.view = view
        self.model = model