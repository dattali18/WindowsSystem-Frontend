from Models import MoviesModel, Movie

movies_model = MoviesModel()


def test_get_movies():
    movies: list[Movie] = movies_model.get_movies()
    for movie in movies:
        print(movie)
