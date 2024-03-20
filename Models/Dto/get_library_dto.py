from .media_dto import MediaDto

class GetLibraryDto:
    """Data Transfer Object Class for the GetLibraryDto"""

    def __init__(self, id: int, name: str, keywords: str, media: list[MediaDto]):
        self.id = id
        self.name = name
        self.keywords = keywords.split(",")
        self.media = media

    def __repr__(self) -> str:
        return f"CreateLibraryDto(id={self.id}, name={self.name}, keywords={self.keywords}, len(media)={len(self.media)})"
