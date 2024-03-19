import requests
from . import MediaDto


class LibrariesModel:
    """Model Class for the Library Entity"""

    def __init__(self): ...


class CreateLibraryDto:
    """Data Transfer Object Class for the CreateLibraryDto"""

    def __init__(self, name: str, keywords: list[str]):
        self.name = name
        self.keywords = ",".join(keywords)


class GetLibraryDto:
    """Data Transfer Object Class for the GetLibraryDto"""

    def __init__(self, name: str, keywords: str, media: list[MediaDto]):
        self.name = name
        self.keywords = keywords.split(",")
        self.media = media
