from .media_dto import MediaDto


class GetLibraryDto:
    """Data Transfer Object Class for the GetLibraryDto"""

    def __init__(self, id: int, name: str, keywords: str, media: list[MediaDto]):
        self.id = id
        self.name = name
        # handle the case we recive an empty string
        if keywords == "":
            self.keywords = []
        else:
            self.keywords = keywords.split(",")
        self.media = media

    def __repr__(self) -> str:
        return f"GetLibraryDto(id={self.id}, name={self.name}, keywords={self.keywords}, len(media)={len(self.media)})"
