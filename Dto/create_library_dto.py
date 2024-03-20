class CreateLibraryDto:
    """Data Transfer Object Class for the CreateLibraryDto"""

    def __init__(self, name: str, keywords: list[str]):
        self.name = name
        self.keywords = ",".join(keywords)

    def __repr__(self) -> str:
        return f"CreateLibraryDto(name={self.name}, keywords={self.keywords})"
