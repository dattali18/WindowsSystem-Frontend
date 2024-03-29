from Views import LibraryViewWindow
from Models import LibraryModel, CreateLibraryDto, MoviesModel, TvSeriesModel

from typing import Optional


class LibraryController:
    def __init__(
        self,
        view: LibraryViewWindow,
        library_model: LibraryModel,
        movie_model: MoviesModel,
        tv_series_model: TVSeriesModel,
    ):
        self.view = view.ui
        self.window = view
        self.library_model = library_model
        self.movie_model = movie_model
        self.tv_series_model = tv_series_model

        # please take a look in the library_ui.py file and init all the widgets here

        self.search_edit = self.view.search_edit
        self.combo_box = self.view.combo_box
        self.search_btn = self.view.search_btn
        self.search_lst = self.view.search_lst
        self.add_btn = self.view.add_btn
        self.create_btn = self.view.create_btn
        self.remove_btn = self.view.remove_btn
        self.name_edit = self.view.name_edit
        self.library_lst = self.view.library_lst

        self.search_btn.clicked.connect(self.handle_search)
        self.create_btn.clicked.connect(self.handle_create)
        self.remove_btn.clicked.connect(self.handle_remove)
        self.add_btn.clicked.connect(self.handle_add)

        self.media: Optional[list[MediaDto]] = None

        def handle_search(self):
            """search for a media from the api"""
            search_text = self.search_edit.text()
            media_type = self.combo_box.currentText()

            # Use self.model to send an API request to get media based on search_text and media_type
            # Store the result in a variable

            if media_type == "Movies":
                self.media = self.movie_model.get_movies_search(search_text)
                if self.media is None:
                    # Handle case when media is None
                    # TODO: implement this later
                    pass
            elif media_type == "TV Series":
                # Code to get TV series based on search_text
                # TODO: for Yair implement this part
                pass

        def handle_create(self):
            pass

        def handle_remove(self):
            pass

        def handle_add(self):
            pass
