import requests
from typing import Optional

from . import MediaDto

PORT = 5062


class CreateLibraryDto:
    """Data Transfer Object Class for the CreateLibraryDto"""

    def __init__(self, name: str, keywords: list[str]):
        self.name = name
        self.keywords = ",".join(keywords)

    def __repr__(self) -> str:
        return f"CreateLibraryDto(name={self.name}, keywords={self.keywords})"


class GetLibraryDto:
    """Data Transfer Object Class for the GetLibraryDto"""

    def __init__(self, name: str, keywords: str, media: list[MediaDto]):
        self.name = name
        self.keywords = keywords.split(",")
        self.media = media

    def __repr__(self) -> str:
        return f"CreateLibraryDto(name={self.name}, keywords={self.keywords}, len(media)={len(self.media)})"


class LibrariesModel:
    """Model Class for the Library Entity"""

    def __init__(self, PORT=PORT):
        self.PORT = PORT

    def get_libraries(self) -> Optional[list[GetLibraryDto]]:
        url = f"http://localhost:{self.PORT}/api/Libraries"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return [GetLibraryDto(**obj) for obj in json_obj]
        return None

    def get_library_id(self, id: int) -> Optional[GetLibraryDto]:
        url = f"http://localhost:{self.PORT}/api/Libraries/{id}"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return GetLibraryDto(**json_obj)
        return None

    def get_library_movies(self, id: int) -> Optional[list[MediaDto]]:
        url = f"http://localhost:{self.PORT}/api/Libraries/{id}/movies"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return [MediaDto(**obj) for obj in json_obj]
        return None

    def get_library_tvseries(self, id: int) -> Optional[list[MediaDto]]:
        url = f"http://localhost:{self.PORT}/api/Libraries/{id}/tvseries"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return [MediaDto(**obj) for obj in json_obj]
        return None

    def get_libraries_name(self, name: str) -> Optional[list[GetLibraryDto]]:
        url = f"http://localhost:{self.PORT}/api/Libraries/search/{name}"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return [GetLibraryDto(**obj) for obj in json_obj]
        return None

    def post_libraries(self, library: CreateLibraryDto) -> Optional[GetLibraryDto]:
        url = f"http://localhost:{self.PORT}/api/Libraries"
        data = CreateLibraryDto.__dict__

        response = requests.post(url, json=data)
        if response.status_code == 201:
            json_str = response.text
            json_obj = json.loads(json_str)
            return GetLibraryDto(**json_obj)
        return None

    def post_libraries_movies(self, library_id: int, imdbID: str) -> Optional[MediaDto]:
        url = f"http://localhost:{self.PORT}/api/Libraries/{library_id}/movies?imdbID={imdbID}"

        response = requests.post(url, json=data)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return MediaDto(**json_obj)
        return None

    def post_libraries_tvseries(
        self, library_id: int, imdbID: str
    ) -> Optional[MediaDto]:
        url = f"http://localhost:{self.PORT}/api/Libraries/{library_id}/tvseries?imdbID={imdbID}"

        response = requests.post(url, json=data)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return MediaDto(**json_obj)
        return None

    def delete_libraries_movies(self, library_id: int, imdbID: str) -> bool:
        url = f"http://localhost:{self.PORT}/api/Libraries/{library_id}/movies?imdbID={imdbID}"

        response = requests.delete(url)
        return response.status_code == 204

    def delete_libraries_tvseries(self, library_id: int, imdbID: str) -> bool:
        url = f"http://localhost:{self.PORT}/api/Libraries/{library_id}/tvseries?imdbID={imdbID}"

        response = requests.delete(url)
        return response.status_code == 204

    def put_libraries_id(
        self, id: int, library: CreateLibraryDto
    ) -> Optional[GetLibraryDto]:
        url = f"http://localhost:{self.PORT}/api/Libraries/{id}"
        data = CreateLibraryDto.__dict__

        response = requests.put(url, json=data)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return GetLibraryDto(**json_obj)
        return None

    def delete_libraries_id(self, id: int) -> bool:
        url = f"http://localhost:{self.PORT}/api/Libraries/{id}"

        response = requests.delete(url)
        return response.status_code == 204
