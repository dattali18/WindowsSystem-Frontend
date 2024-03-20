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
        """
        GET - /api/Libraries/
        Returns:
            Optional[list[GetLibraryDto]] - a list of all libraries
            in the database in a GetLibraryDto format
            None if response.status_code == 404
        """
        url = f"http://localhost:{self.PORT}/api/Libraries"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return [GetLibraryDto(**obj) for obj in json_obj]
        return None

    def get_library_id(self, id: int) -> Optional[GetLibraryDto]:
        """
        GET - /api/Libraries/{id}
        Args:
            id : int - the id of the library in the database
        Returns:
            Optional[GetLibraryDto] - a library in the database
            with id=id in a GetLibraryDto format
            None if response.status_code == 404
        """
        url = f"http://localhost:{self.PORT}/api/Libraries/{id}"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return GetLibraryDto(**json_obj)
        return None

    def get_library_movies(self, id: int) -> Optional[list[MediaDto]]:
        """
        GET - /api/Libraries/{id}/movies
        Args:
            id : int - the id of the library in the database
        Returns:
            Optional[list[MediaDto]] - a list of all movies in the library
            with id=id in a MediaDto format
            None if response.status_code == 404
        """
        url = f"http://localhost:{self.PORT}/api/Libraries/{id}/movies"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return [MediaDto(**obj) for obj in json_obj]
        return None

    def get_library_tvseries(self, id: int) -> Optional[list[MediaDto]]:
        """
        GET - /api/Libraries/{id}/tvseries
        Args:
            id : int - the id of the library in the database
        Returns:
            Optional[list[MediaDto]] - a list of all tvseries in the
            library with id=id in a MediaDto format
            None if response.status_code == 404
        """
        url = f"http://localhost:{self.PORT}/api/Libraries/{id}/tvseries"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return [MediaDto(**obj) for obj in json_obj]
        return None

    def get_libraries_name(self, name: str) -> Optional[list[GetLibraryDto]]:
        """
        GET - /api/Libraries/search/{name}
        Args:
            name : str - the name of the library
        Returns:
            Optional[list[GetLibraryDto]] - a list of all libraries
            in the database with name starting with name in a GetLibrary format
            None if response.status_code == 404
        """
        url = f"http://localhost:{self.PORT}/api/Libraries/search/{name}"

        response = requests.get(url)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return [GetLibraryDto(**obj) for obj in json_obj]
        return None

    def post_libraries(self, library: CreateLibraryDto) -> Optional[GetLibraryDto]:
        """
        POST - /api/Libraries/
        Args:
            library : CreateLibraryDto - the library data transfer object for creating the library
        Returns:
            Optional[GetLibraryDto] - a library object that was created
            None if response.status_code == 404
        """
        url = f"http://localhost:{self.PORT}/api/Libraries"
        data = CreateLibraryDto.__dict__

        response = requests.post(url, json=data)
        if response.status_code == 201:
            json_str = response.text
            json_obj = json.loads(json_str)
            return GetLibraryDto(**json_obj)
        return None

    def post_libraries_movies(self, library_id: int, imdbID: str) -> Optional[MediaDto]:
        """
        POST - /api/Libraries/{library_id}/movies?imdbID={imdbID}
        Args:
            library_id : int - the library id of the library we want to change
            imdbID: str -  the imdbID of the movie we want to add
        Returns:
            Optional[MediaDto] - the movie object that was added to the library in MediaDto format
            None if response.status_code == 404
        """
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
        """
        POST - /api/Libraries/{library_id}/tvseries?imdbID={imdbID}
        Args:
            library_id : int - the library id of the library we want to change
            imdbID: str -  the imdbID of the tvseries we want to add
        Returns:
            Optional[MediaDto] - the tvseries object that was added to the library in MediaDto format
            None if response.status_code == 404
        """
        url = f"http://localhost:{self.PORT}/api/Libraries/{library_id}/tvseries?imdbID={imdbID}"

        response = requests.post(url, json=data)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return MediaDto(**json_obj)
        return None

    def delete_libraries_movies(self, library_id: int, imdbID: str) -> bool:
        """
        DELETE - /api/Libraries/{library_id}/movies?imdbID={imdbID}
        Args:
            library_id : int - the library id of the library we want to change
            imdbID: str -  the imdbID of the movies we want to add
        Returns:
            bool - True if the object was deleting else False
        """
        url = f"http://localhost:{self.PORT}/api/Libraries/{library_id}/movies?imdbID={imdbID}"

        response = requests.delete(url)
        return response.status_code == 204

    def delete_libraries_tvseries(self, library_id: int, imdbID: str) -> bool:
        """
        DELETE - /api/Libraries/{library_id}/tvseries?imdbID={imdbID}
        Args:
            library_id : int - the library id of the library we want to change
            imdbID: str -  the imdbID of the movies we want to add
        Returns:
            bool - True if the object was deleting else False
        """
        url = f"http://localhost:{self.PORT}/api/Libraries/{library_id}/tvseries?imdbID={imdbID}"

        response = requests.delete(url)
        return response.status_code == 204

    def put_libraries_id(
        self, id: int, library: CreateLibraryDto
    ) -> Optional[GetLibraryDto]:
        """
        PUT - /api/Libraries/{id}
        Args:
            id : int - the library id of the library we want to change
            library: CreateLibraryDto -  the library data transfer object for creating the library
        Returns:
            Optional[GetLibraryDto] - a library object that was changed
            None if response.status_code == 404
        """
        url = f"http://localhost:{self.PORT}/api/Libraries/{id}"
        data = CreateLibraryDto.__dict__

        response = requests.put(url, json=data)
        if response.status_code == 200:
            json_str = response.text
            json_obj = json.loads(json_str)
            return GetLibraryDto(**json_obj)
        return None

    def delete_libraries_id(self, id: int) -> bool:
        """
        DELETE - /api/Libraries/{id}
        Args:
            id : int - the library id of the library we want to change
        Returns:
            bool - True if the object was deleted else False
        """
        url = f"http://localhost:{self.PORT}/api/Libraries/{id}"

        response = requests.delete(url)
        return response.status_code == 204
