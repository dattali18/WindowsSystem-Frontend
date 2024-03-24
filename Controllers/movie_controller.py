from Views import MovieViewWindow
from Models import MoviesModel, MovieDto

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import (
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QLineEdit,
    QLabel,
    QComboBox,
)
from PySide6.QtGui import QPixmap, QScreen

from typing import Optional
import requests


class MovieController:

    def __init__(self, view: MovieViewWindow, model: MoviesModel):
        self.view = view.ui
        self.window = view
        self.model = model

        self.movie: Optional[MovieDto] = None

        self.title = self.view.title
        self.genre = self.view.genre
        self.imdbID = self.view.imdb
        self.year = self.view.year
        self.rating = self.view.rating
        self.image = self.view.image

        self.pixmap = QPixmap()

        self.create_random_data_for_debug()
        self.populate_media_table()

    def populate_media_table(self):
        self.title.setText(f"{self.movie.title}")
        self.genre.setText(f"Genre \t{self.movie.genre}")
        self.imdbID.setText(f"Imdb ID \t{self.movie.imdbID}")
        self.year.setText(f"Year \t{self.movie.year}")
        self.rating.setText(f"Rating \t{self.movie.rating}")
        self.getAndSetImageFromURL(self.movie.poster_url)

    def getAndSetImageFromURL(self, imageURL):
        request = requests.get(imageURL)
        self.pixmap.loadFromData(request.content)
        width = self.view.horizontalLayoutWidget.width()
        height = self.view.horizontalLayoutWidget.height()
        self.pixmap = self.pixmap.scaled(width, height, QtCore.Qt.KeepAspectRatio)
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
