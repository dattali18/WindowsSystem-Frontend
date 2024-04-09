from .libraries_model import LibrariesModel
from .movies_model import MoviesModel
from .tvseries_model import TvSeriesModel

class Models:
    def __init__(self) -> None:
        self.libraries = LibrariesModel()
        self.movies = MoviesModel()
        self.tvseries = TvSeriesModel()