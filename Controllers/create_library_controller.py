from Controllers.update_library_controller import UpdateLibraryController
from Dto.create_library_dto import CreateLibraryDto
from Views import CreateLibraryView
from Models import LibrariesModel, Models
from Views.update_library_view import UpdateLibraryView
from PySide6.QtWidgets import QMessageBox


class CreateLibraryController:
    def __init__(self, view: CreateLibraryView, model: LibrariesModel) -> None:
        self.view = view
        self.model = model

        self.view.create_button.clicked.connect(self.handle_create_click)

        self.update_library_controller = None

    def handle_create_click(self) -> None:
        lib_name = self.view.name_text.text()
        if lib_name == "":
            QMessageBox.information(
                self, "Error", "Cannot create Library with empty name!"
            )
            return

        genres = [k for k, v in self.view.checkboxes_dict if v.isChecked()]

        dto = CreateLibraryDto(name=lib_name, keywords=genres)
        library = self.model.post_libraries(library=dto)

        if library is None:
            print("404 error")
            return

        self.update_library_controller = UpdateLibraryController(
            view=UpdateLibraryView(), model=Models(), library_id=library.id
        )
        # self.update_library_controller.library_id = library.id
        self.update_library_controller.show()
