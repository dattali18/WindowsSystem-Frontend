from typing import Optional

from Models import MoviesModel, Movie, MediaDto

movies_model = MoviesModel()


def test_get_movies():
    movies: list[Movie] = movies_model.get_movies()
    for movie in movies:
        print(movie)


def test_get_movie_id():
    movie: Optional[Movie] = movies_model.get_movie_id(id=1)
    print(movie)


def test_get_movie_imdbID():
    movie: Optional[Movie] = movies_model.get_movie_imdbID(imdbID="tt0080684")
    print(movie)


def test_get_movies_search():
    movies: list[MediaDto] = movies_model.get_movies_search(s="Star Wars")
    for movie in movies:
        print(movie)


def test_post_movie():
    movie: Optional[MediaDto] = movies_model.post_movie(imdbID="tt0086190")
    print(movie)


def test_movies_model():
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
