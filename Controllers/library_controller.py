from Views import LibraryView
from Models import (
    LibrariesModel,
    CreateLibraryDto,
    MoviesModel,
    TvSeriesModel,
    MediaDto,
)
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
        view: LibraryView,
        library_model: LibrariesModel,
        movie_model: MoviesModel,
        tv_series_model: TVSeriesModel,
    ):
        self.view = view
        self.library_model = library_model
        self.movie_model = movie_model
        self.tv_series_model = tv_series_model

        self.media: Optional[list[MediaDto]] = None
