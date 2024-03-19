from Models import MoviesModel, Movie

movies_model = MoviesModel()


def test_get_movies():
    movies: list[Movie] = movies_model.get_movies()
    for movie in movies:
        print(movie)


def test_get_movie_id():
    movie: Optional[Movie] = movies_model.get_movie_id(id=1)
    print(movie)


def test_get_movie_imdbID():
    movie: Optional[Movie] = movies_model.get_movie_imdbID(imdbID="tt0067759")
    print(movie)


def test_get_movies_search():
    movies: list[MediaDto] = movies_model.get_movies_search(s="Star Wars")
    for movie in movies:
        print(movie)


def test_post_movie():
    movie: Optional[Movie] = movies_model.post_movie(imdbID="tt0796366")
    print(movie)


def test_movies_model():
    print("{:*^30}")
    greeting = "Testing Movies Model Class"
    print("f{greeting:^30}")

    print("Testing get_movies")
    test_get_movies()

    print("Testing get_movie_id")
    test_get_movie_id()

    print("Testing get_movie_imdbIB")
    test_get_movie_imdbID()

    print("Testing get_movies_search")
    test_get_movies_search()

    print("Testing post_movie")
    test_post_movie()
    print("{:*^30}")
