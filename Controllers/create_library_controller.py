from Controllers.update_library_controller import UpdateLibraryController
from Dto.create_library_dto import CreateLibraryDto
from Views import CreateLibraryView
from Models import LibrariesModel
from Views.update_library_view import UpdateLibraryView

class CreateLibraryController:
    def __init__(self, view: CreateLibraryView, model: LibrariesModel) -> None:
        self.view = view
        self.model = model

        self.view.create_button.clicked.connect(self.handle_create_click)

    def handle_create_click(self):
        lib_name = self.view.name_text.text()
        if lib_name == "":
            self.view.name_text = ""
            return
        
        genres = [s for s in self.view.checkboxes_dict.keys() 
                  if self.view.checkboxes_dict[s].isChecked()]
        
        library = self.model.post_libraries(CreateLibraryDto(lib_name, genres))

        if library == None:
            self.view.name_text = ""
            return
        
        UpdateLibraryController(UpdateLibraryView, LibrariesModel, library.id).view.show()
        return
