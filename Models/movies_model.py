import requests
import json

PORT = 7237


class Movie:
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
        return f"Movie({self.id=}, {self.title=}, {self.rating=}, {self.time=} min, {self.imdbID=})"


class MoviesModel:
    """Model Class for the Movie Entity"""

    def __init__(self, PORT: int = PORT):
        self.PORT = PORT

    def get_movies(self) -> list[Movie]:
        url = f"https://localhost:{self.PORT}/api/Movies"

        response = requests.get(url, verify=False)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return [Movie(**obj) for obj in json_obj]
        else:
            return []
