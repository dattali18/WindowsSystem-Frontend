class CreateLibraryDto:
    """Data Transfer Object Class for the CreateLibraryDto"""

    def __init__(self, name: str, keywords: str | list[str]):
        self.name = name
        if isinstance(keywords, str):
            self.keywords = keywords
        else:
            self.keywords = ",".join(keywords)

    def __repr__(self) -> str:
        return f"CreateLibraryDto(name={self.name}, keywords={self.keywords})"
