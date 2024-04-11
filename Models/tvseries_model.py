import requests
import json

from typing import Optional

from .config import BASE_URL

from Models import MediaDto

from Dto.tv_series_dto import TvSeriesDto


class TvSeriesModel:
    def __init__(self, BASE_URL: str = BASE_URL):
        self.BASE_URL = BASE_URL

    def get_tv_series(self) -> Optional[list[TvSeriesDto]]:
        """
        GET - /api/TvSeries
        Returns:
            Optional[list[TvSeriesDto]] - a list of all series in the database in the TvSeries format
            None if response.status_code == 404
        """
        url = f"{self.BASE_URL}/TvSeries"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                json_str = response.text
                json_obj = json.loads(json_str)
                return [TvSeriesDto(**obj) for obj in json_obj]
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return None
    
    def get_tv_series_id(self, id: int) -> Optional[TvSeriesDto]:
        """
        GET - /api/TvSeries/{id}
        Args:
            id: int - the id of the series in the database
        Returns:
            Optional[TvSeriesDto] - a series in the database with the id=id in the TvSeries format
            None if response.status_code == 404
        """
        url = f"{self.BASE_URL}/TvSeries/{id}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                json_str = response.text
                json_obj = json.loads(json_str)
                return TvSeriesDto(**json_obj)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return None
    
    def get_tv_series_imdbID(self, imdbID: str) -> Optional[TvSeriesDto]:
        """
        GET - /api/TvSeries/search/{imdbID}
        Args:
            id: int - the imdbID of the series in the database
        Returns:
            Optional[TvSeriesDto] - a series in the database with the imdbID=imdbID in the TvSeries format
            None if response.status_code == 404
        """
        url = f"{self.BASE_URL}/TvSeries/search/{imdbID}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                json_str = response.text
                json_obj = json.loads(json_str)
                return TvSeriesDto(**json_obj)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return None
    
    def get_tv_series_search(
            self, s: str, y: Optional[int] = None
    ) -> Optional[list[MediaDto]]:
        """
        GET - /api/TvSeries/search/?s=s
        Args:
            s: str - search term
            y: int - year of the media
        Returns:
            Optional[list[MediaDto]] - a list of media in the Omdb API database in the Media format
            None if response.status_code == 404
        """
        try:
            url = f"{self.BASE_URL}/TvSeries/search/?s={s}"
            if y:
                url += f"&y={y}"

            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                json_str = response.text
                json_obj = json.loads(json_str)
                return [MediaDto(**obj) for obj in json_obj]
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return None
    
    def post_tv_series(self, imdbID: str) -> Optional[TvSeriesDto]:
        """
        POST - /api/TvSeries/?imdbID=imdbID
        Args:
            imdbID : str - the imdbID of the series in the database
        Returns:
            Optional[TvSeriesDto] - a series that was inserted in the database from the Omdb API
            None if response.status_code == 404
        """
        url = f"{self.BASE_URL}/TvSeries?imdbID={imdbID}"

        try:
            response = requests.post(url, timeout=5)
            if response.status_code in {200, 201}:
                json_str = response.text
                json_obj = json.loads(json_str)
                return TvSeriesDto(**json_obj)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return None

