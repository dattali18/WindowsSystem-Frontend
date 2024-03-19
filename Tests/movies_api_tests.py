from Models import MoviesModel, Movie

movies_model = MoviesModel()

def test_get_movies():
    movies: list[Movie] = movies_model.get_movies()
    print(movies)

def main():
    test_get_movies()

if __name__ == "__main__":
    main()
