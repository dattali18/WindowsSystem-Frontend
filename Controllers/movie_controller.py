from Views import MovieViewWindow
from Models import MoviesModel, MovieDto

from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from typing import Optional
import requests


class MovieController:

    def __init__(self, imdbID: str, view: MovieViewWindow, model: MoviesModel):
        self.view = view.ui
        self.window = view
        self.model = model
        self.imdbID_str = imdbID

        self.movie: Optional[MovieDto] = None

        self.title: QLabel = self.view.title
        self.genre: QLabel = self.view.genre
        self.imdbID: QLabel = self.view.imdb
        self.year: QLabel = self.view.year
        self.rating: QLabel = self.view.rating
        self.image: QLabel = self.view.image

        self.pixmap = QPixmap()

        # self.create_random_data_for_debug()
        # self.populate_data()
        self.get_movie_from_imdbID()

    def populate_data(self):
        self.title.setText(f"{self.movie.title}")
        self.genre.setText(f"Genre: {self.movie.genre}")
        self.imdbID.setText(f"Imdb ID: {self.movie.imdbID}")
        self.year.setText(f"Year: {self.movie.year}")
        self.rating.setText(f"Rating: {self.movie.rating}")
        self.getAndSetImageFromURL(self.movie.poster_url)

    def getAndSetImageFromURL(self, imageURL):
        request = requests.get(imageURL)
        self.pixmap.loadFromData(request.content)
        width = self.view.menubar.width()
        height = self.view.menubar.height()
        self.pixmap = self.pixmap.scaled(width // 2, width, QtCore.Qt.KeepAspectRatio)
        self.image.setPixmap(self.pixmap)

    def create_random_data_for_debug(self):
        self.movie = MovieDto(
            id=0,
            title="Star Wars",
            genre="Science Fiction",
            year=1987,
            rating=8.9,
            imdbID="tt1234567",
            time=123,
            posterURL="https://www.komar.de/media/catalog/product/cache/5/image/1230x/17f82f742ffe127f42dca9de82fb58b1/4/-/4-4127_avengers_endgame_movie_poster_web.jpg",
        )

    def get_movie_from_imdbID(self):
        self.movie = self.model.get_movie_imdbID(imdbID=self.imdbID_str)
        if self.movie is None:
            print("404 probelm please check backend")
        else:
            self.populate_data()
