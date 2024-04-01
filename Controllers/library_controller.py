from Views import LibraryViewWindow
from Models import LibrariesModel, CreateLibraryDto, MoviesModel, TvSeriesModel, MediaDto
from typing import Optional


class LibraryController:
    """
    The LibraryController class is responsible for managing the operations of the library window.

    This includes tasks such as adding, removing, or updating books in the library, managing user accounts,
    and handling book checkouts and returns.

    Attributes:
        None

    Methods:
        To be defined.
    """

    def __init__(
        self,
        view: LibraryViewWindow,
        library_model: LibrariesModel,
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
        self.movies: list[str] = []
        self.series: list[str] = []

        def populate_search_list(self):
            """Populate the search list with the searched media"""
            self.search_lst.clear()
            if self.media:
                for media in self.media:
                    self.search_lst.addItem(media)
            else:
                # Handle case when media is None
                # TODO: implement this later
                print("No media found.")

        def handle_search(self):
            """search for a media from the api"""
            search_text = self.search_edit.text().lower()
            media_type = self.combo_box.currentText()

            # Use self.model to send an API request to get media based on search_text and media_type
            # Store the result in a variable

            if media_type == "movies":
                self.media = self.movie_model.get_movies_search(search_text)
                if self.media is None:
                    # Handle case when media is None
                    # TODO: implement this later
                    print(f"404 error for search {search_text=}")
            elif media_type == "tv series":
                # Code to get TV series based on search_text
                # TODO: for Yair implement this part
                print(f"searched for {search_text=}, to be handled by Yair")
            self.populate_search_list()

        def handle_create(self):
            pass

        def handle_remove(self):
            selected_item = self.library_lst.currentItem()
            if selected_item:
                media = selected_item.data()
                imdb_id = media.imdbID
                if media.type == "Movies":
                    self.movies.remove(imdb_id)
                else:
                    self.series.remove(imdb_id)
            else:
                print("No media selected.")

        def handle_add(self):
            selected_item = self.search_lst.currentItem()
            media_type = self.combo_box.currentText()
            if selected_item:
                media = selected_item.data()
                imdb_id = media.imdbID
                if media_type == "Movies":
                    self.movies.append(imdb_id)
                else:
                    self.series.append(imdb_id)
            else:
                print("No media selected.")
