class MediaDto:
    """Data Transfer Object Class for the GetLibraryDto"""
    def __init__(self, title: str, year: str, type: str, poster: str, imdbID: str):
        self.title = title
        self.year = year
        self.type = type
        self.poster = poster
        self.imdbID = imdbID
        