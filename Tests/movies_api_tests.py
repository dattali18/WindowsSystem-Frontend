from typing import Optional

from Models import MoviesModel, MovieDto, MediaDto

movies_model = MoviesModel()


def test_get_movies() -> None:
    movies: list[MovieDto] = movies_model.get_movies()
    if not libraries:
        print("There was an error")
    else:
        for movie in movies:
            print(movie)


def test_get_movie_id(id: int = 1) -> None:
    movie: Optional[MovieDto] = movies_model.get_movie_id(id=id)
    if not libraries:
        print("There was an error")
    else:
        print(movie)


def test_get_movie_imdbID(imdbID: str = "tt0080684") -> None:
    movie: Optional[MovieDto] = movies_model.get_movie_imdbID(imdbID=imdbID)
    if not libraries:
        print("There was an error")
    else:
        print(movie)


def test_get_movies_search(s: str = "Star Wars") -> None:
    movies: list[MediaDto] = movies_model.get_movies_search(s=s)
    if not libraries:
        print("There was an error")
    else:
        for movie in movies:
            print(movie)


def test_post_movie(imdbID: str = "tt0086190") -> None:
    movie: Optional[MediaDto] = movies_model.post_movie(imdbID=imdbID)
    if not libraries:
        print("There was an error")
    else:
        print(movie)


def test_movies_model() -> None:
    intro = ""
    print(f"{intro:*^30}")
    greeting = "Testing Movies Model Class\n"
    print(f"{greeting:^30}")

    print(f"{intro:_^30}")
    print("Testing get_movies\n")
    test_get_movies()

    print(f"{intro:_^30}")
    print("Testing get_movie_id\n")
    test_get_movie_id()

    print(f"{intro:_^30}")
    print("Testing get_movie_imdbIB\n")
    test_get_movie_imdbID()

    print(f"{intro:_^30}")
    print("Testing get_movies_search\n")
    test_get_movies_search()

    print(f"{intro:_^30}")
    print("Testing post_movie\n")
    test_post_movie()

    print(f"{intro:*^30}")
