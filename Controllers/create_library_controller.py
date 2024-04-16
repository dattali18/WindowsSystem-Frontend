from Controllers.update_library_controller import UpdateLibraryController
from Views import CreateLibraryView, UpdateLibraryView
from Models import LibrariesModel, Models, CreateLibraryDto

from PySide6.QtWidgets import QMessageBox

from typing import Optional


class CreateLibraryController:
    def __init__(self, view: CreateLibraryView, model: LibrariesModel, library_id: Optional[int] = None) -> None:
        self.view = view
        self.model = model
        self.library_id = library_id

        self.view.create_button.clicked.connect(self.handle_create_click)

        self.update_library_controller = None

    def set_up_ui(self) -> None:
        if self.library_id:
            self.view.title.setText("Update Library")
            self.view.create_button.setText("Update")
            self.view.name_text.setText(self.library.name)

            for genre in self.library.keywords:
                self.view.checkboxes_dict[genre].setChecked(True)

    def handle_create_click(self) -> None:
        lib_name = self.view.name_text.text()
        if lib_name == "":
            QMessageBox.information(
                self, "Error", "Cannot create Library with empty name!"
            )
            return

        # get all the genre names from the checkboxes
        genres = [k for k, v in self.view.checkboxes_dict.items() if v.isChecked()]

        dto = CreateLibraryDto(name=lib_name, keywords=genres)

        if self.library_id:
            library = self.model.put_libraries_id(id=self.library_id, library=dto)
        else:
            library = self.model.post_libraries(library=dto)

        if library is None:
            print("404 error")
            return
        
        self.update_library_controller = UpdateLibraryController(
            view=UpdateLibraryView(), model=Models(), library_id=library.id
        )
        self.update_library_controller.show()
        self.view.close()
