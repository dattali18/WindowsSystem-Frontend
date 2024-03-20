class MovieDto:
    """Class for the Movie Entity"""

    def __init__(
        self,
        id: int,
        title: str,
        posterURL: str,
        rating: float,
        year: int,
        imdbID: str,
        time: int,
        genre: str,
    ):
        self.id = id
        self.title = title
        self.poster_url = posterURL
        self.rating = rating
        self.year = year
        self.imdbID = imdbID
        self.time = time
        self.genre = genre

    def __repr__(self) -> str:
        return f"Movie(id={self.id}, title={self.title}, rating={self.rating}, time={self.time} min, imdbID={self.imdbID})"
