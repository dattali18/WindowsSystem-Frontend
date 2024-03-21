import requests
import json
from typing import Optional

from Models import MediaDto, MovieDto

PORT = 5062


class MoviesModel:
    """Model Class for the Movie Entity"""

    def __init__(self, PORT: int = PORT):
        self.PORT = PORT

    def get_movies(self) -> Optional[list[MovieDto]]:
        """
        GET - /api/Movies
        Returns:
            Optional[list[Movie]] - a list of all movies in the database in the Movie format
            None if response.status_code == 404
        """
        url = f"http://localhost:{self.PORT}/api/Movies"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return [MediaDto(**obj) for obj in json_obj]
        return None

    def get_movie_id(self, id: int) -> Optional[MovieDto]:
        """
        GET - /api/Movies/{id}
        Args:
            id: int - the id of the movie in the database
        Returns:
            Optional[Movie] - a movies in the database with the id=id in the Movie format
            None if response.status_code == 404
        """
        url = f"http://localhost:{self.PORT}/api/Movies/{id}"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return MediaDto(**json_obj)
        return None

    def get_movie_imdbID(self, imdbID: str) -> Optional[MovieDto]:
        """
        GET - /api/Movies/{imdbID}
        Args:
            imdbID: str - the imdbID of the movie in the database
        Returns:
            Optional[Movie] - a movies in the database with the imdbID=imdbID in the Movie format
            None if response.status_code == 404
        """
        url = f"http://localhost:{self.PORT}/api/Movies/search/{imdbID}"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return MediaDto(**json_obj)
        return None

    def get_movies_search(
        self, s: str, y: Optional[int] = None
    ) -> Optional[list[MediaDto]]:
        """
        GET - /api/Movies/search/?s=s
        Args:
            s: str - search term
            y: int - year of the media
        Returns:
            Optional[list[MediaDto]] - a list of media in the Omdb API database in the Media format
            None if response.status_code == 404
        """
        url = f"http://localhost:{self.PORT}/api/Movies/search/?s={s}"
        if y:
            url += f"&y={y}"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return [MediaDto(**obj) for obj in json_obj]
        return None

    def post_movie(self, imdbID: str) -> Optional[MovieDto]:
        """
        POST - /api/Movies/?imdbID=imdbID
        Args:
            imdbID : str - the imdbID of the movie in the database
        Returns:
            Optional[Movie] - a movie that was inserted in the database from the Omdb API
            None if response.status_code == 404
        """
        url = f"http://localhost:{self.PORT}/api/Movies?imdbID={imdbID}"

        response = requests.post(url)
        if response.status_code in {200, 201}:
            json_str = response.text
            json_obj = json.loads(json_str)
            return MediaDto(**json_obj)
        return None
