from Views import MediaView
from Models import Models, MediaDto, ImageModel

from PySide6.QtWidgets import (
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QLineEdit,
    QComboBox,
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


from typing import Optional


class MediaController:
    def __init__(self, view: MediaView, media: Optional[MediaDto]):
        self.view = view
        self.media: Optional[MediaDto] = media

        if self.media == None:
            self.create_dummy_data()
        else:
            self.set_media()

    def set_media(self):
        if self.media == None:
            return

        self.view.title_label.setText(f"{self.media.title}")
        self.view.media_year.setText(f"Year:\t{self.media.year}")
        self.view.media_rating.setText(f"Ratings:\t{self.media.rating}")
        self.view.media_imdb_id.setText(f"Imdb ID:\t{self.media.imdbID}")
        self.view.media_type.setText(f"Type:\t{self.media.type}")

        self.set_image()

    def set_image(self):
        if self.media == None:
            return

        image = ImageModel().get_image(self.media.poster)
        pixmap = QPixmap()
        pixmap.loadFromData(image)
        pixmap = pixmap.scaled(
            self.view.media_image.width(),
            self.view.media_image.height(),
            Qt.KeepAspectRatio,
            Qt.FastTransformation,
        )
        self.view.media_image.setAlignment(Qt.AlignCenter)
        self.view.media_image.setPixmap(pixmap)

    def create_dummy_data(self):
        self.media = MediaDto(
            title="The Matrix",
            type="Movie",
            year="1999",
            rating="8.7",
            imdbID="tt0133093",
            poster="https://m.media-amazon.com/images/M/MV5BOTA5NjhiOTAtZWM0ZC00MWNhLThiMzEtZDFkOTk2OTU1ZDJkXkEyXkFqcGdeQXVyMTA4NDI1NTQx._V1_SX300.jpg",
        )
        self.set_media()

    def show(self):
        self.view.show()
