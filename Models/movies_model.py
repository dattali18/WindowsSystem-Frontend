import requests
import json
from typing import Optional

from Models import MediaDto

PORT = 5062


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

    def get_movies(self) -> Optional[list[Movie]]:
        url = f"http://localhost:{self.PORT}/api/Movies"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return [Movie(**obj) for obj in json_obj]
        return None

    def get_movie_id(self, id: int) -> Optional[Movie]:
        url = f"http://localhost:{self.PORT}/api/Movies/{id}"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return Movie(**json_obj)
        return None

    def get_movie_imdbID(self, imdbID: str) -> Optional[Movie]:
        url = f"http://localhost:{self.PORT}/api/Movies/search/{imdbID}"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return Movie(**json_obj)
        return None

    def get_movies_search(
        self, s: str, y: Optional[int] = None
    ) -> Optional[list[MediaDto]]:
        url = f"http://localhost:{self.PORT}/api/Movies/search/?s={s}"
        if y:
            url += f"&y={y}"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return [MediaDto(**obj) for obj in json_obj]
        return None

    def post_movie(self, imdbID: str) -> Optional[Movie]:
        url = f"http://localhost:{self.PORT}/api/Movies?imdbID={imdbID}"

        response = requests.post(url)
        if response.status_code in {200, 201}:
            json_str = response.text
            json_obj = json.loads(json_str)
            return Movie(**json_obj)
        return None
