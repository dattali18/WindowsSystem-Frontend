class MediaDto:
    """Data Transfer Object Class for the GetLibraryDto"""

    def __init__(
        self,
        title: str,
        year: str,
        type: str,
        poster: str,
        rating: str,
        imdbID: str,
        genre: str,
    ):
        self.title = title
        self.year = year
        self.type = type
        self.poster = poster
        self.rating = rating
        self.imdbID = imdbID
        self.genre = genre

    def __repr__(self) -> str:
        return f"Media({self.title=}, {self.year=}, {self.type=}, {self.imdbID=})"
