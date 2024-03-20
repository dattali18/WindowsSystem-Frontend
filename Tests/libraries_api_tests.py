from typing import Optional

from Models import LibrariesModel

libraries_model = LibrariesModel()


def test_get_libraries() -> None:
    libraries: Optional[list[GetLibraryDto]] = libraries_model.get_libraries()
    if not libraries:
        print("There was an error")
    else:
        for library in libraries:
            print(library)


def test_get_library_id(id: int = 1) -> None:
    library: Optional[GetLibraryDto] = libraries_model.get_library_id(id=id)
    if not library:
        print("There was an error")
    else:
        print(library)


def test_get_library_movies(id: int = 1) -> None:
    medias: Optional[list[MediaDto]] = libraries_model.get_library_movies(id=id)
    if not medias:
        print("There was an error")
    else:
        for media in medias:
            print(media)


def test_get_library_tvseries(id: int) -> None:
    medias: Optional[list[MediaDto]] = libraries_model.get_library_tvseries(id=id)
    if not medias:
        print("There was an error")
    else:
        for media in medias:
            print(media)


def test_get_libraries_name(name: str = "My") -> None:
    libraries: Optional[list[GetLibraryDto]] = libraries_model.get_libraries_name(
        name=name
    )
    if not libraries:
        print("There was an error")
    else:
        for library in libraries:
            print(library)


def test_post_libraries() -> None:
    library: CreateLibraryDto = CreateLibraryDto(
        name="My Library II", keywords=["Action, Sci Fi"]
    )
    library_response: Optional[GetLibraryDto] = libraries_model.post_libraries(
        library=library
    )
    if not library_response:
        print("There was an error")
    else:
        print(library_response)


def test_post_libraries_movies(id: int = 1, imdbID: str = "tt0080684") -> None:
    movie: Optional[MediaDto] = libraries_model.post_libraries_movies(
        id=id, imdbID=imdbID
    )
    if not movie:
        print("There was an error")
    else:
        print(movie)


def test_post_libraries_tvseries(id: int = 1, imdbID: str = "tt2934286") -> None:
    tvseries: Optional[MediaDto] = libraries_model.post_libraries_tvseries(
        id=id, imdbID=imdbID
    )
    if not tvseries:
        print("There was an error")
    else:
        print(tvseries)


def test_delete_libraries_movies(id: int = 1, imdbID: str = "tt0080684") -> None:
    res = libraries_model.delete_libraries_movies(id=1, imdbID="tt0080684")
    print(f"the deletion was a success" if res else "the was a problem in the deletion")


def test_delete_libraries_tvseries(id: int = 1, imdbID: str = "tt2934286") -> None:
    res = libraries_model.delete_libraries_tvseries(id=id, imdbID="tt2934286")
    print(f"the deletion was a success" if res else "the was a problem in the deletion")


def test_put_libraries_id() -> None:
    library: CreateLibraryDto = CreateLibraryDto(
        name="My Library II", keywords=["Action"]
    )
    library_response: Optional[GetLibraryDto] = libraries_model.put_libraries_id(
        id=1, library=library
    )
    if not library_response:
        print("There was an error")
    else:
        print(library_response)


def test_delete_libraries_id(id: int = 1) -> None:
    res = libraries_model.delete_libraries_id(id=id)
    print(f"the deletion was a success" if res else "the was a problem in the deletion")
