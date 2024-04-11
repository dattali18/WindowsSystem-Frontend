class TvSeriesDto:
    """Class for the Tv Series Entity"""

    def __init__(
        self,
        id: int,
        title: str,
        posterURL: str,
        rating: float,
        start_year: int,
        end_year: int,
        total_seasons: int,
        imdbID: str,
        time: int,
        genre: str,
    ):
        self.id = id,
        self.title = title,
        self.posterURL = posterURL,
        self.rating = rating,
        self.start_year = start_year,
        self.end_year = end_year,
        self.total_seasons = total_seasons,
        self.imdbID = imdbID,
        self.time = time,
        self.genre = genre

    def __repr__(self) -> str:
        return f"TvSeries(id={self.id}, title={self.title}, rating={self.rating}, time={self.time} min, imdbID={self.imdbID})"