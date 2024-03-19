import requests
import json

class MoviesModel:
    """Model Class for the Movie Entity"""
    # def __init__(self):
    #     ...

    def get_movies(self) -> list[Movie]:
        url = f"http://localhost:{PORT}/api/Movies"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = requests.text
            json_obj = json.loads(json_str)
            return [Movie(**obj) for obj in json_obj]
        else:
            return []

class Movie:
    """Class for the Movie Entity"""
    def __init__(self, id: int, title: str, poster_url: str, rating: float, year: int, imdbID: str, time: int):
        self.id = id
        self.title = title
        self.poster_url = poster_url
        self.rating = rating
        self.year = year
        self.imdbID = imdbID  


    