from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from typing import Optional

from Views import MediaView
from Models import MediaDto, ImageModel

from PySide6.QtWidgets import (
    QListWidgetItem,
)


class MediaController:
    def __init__(self, view: MediaView) -> None:
        self.view = view
        self.media: Optional[MediaDto] = None

        self.view.ai_tags_button.clicked.connect(self.handle_ai_tags)

    def show(self) -> None:
        self.view.tag1.hide()
        self.view.tag2.hide()
        self.view.tag3.hide()
        
        if not self.media:
            self.create_dummy_data()
        else:
            self.set_media()
        self.view.show()

        

    def set_media(self) -> None:
        if not self.media:
            return

        self.view.title_label.setText(f"{self.media.title}")
        self.view.media_year.setText(f"Year:\t{self.media.year}")
        self.view.media_imdb_id.setText(f"Imdb ID:\t{self.media.imdbID}")
        self.view.media_type.setText(f"Type:\t{self.media.type}")

        self.set_image()

    def set_image(self) -> None:
        if not self.media:
            return

        self.image: bytes = ImageModel().get_image(self.media.poster)
        pixmap = QPixmap()
        pixmap.loadFromData(self.image)
        pixmap = pixmap.scaled(
            self.view.media_image.width(),
            self.view.media_image.height(),
            Qt.KeepAspectRatio,
            Qt.FastTransformation,
        )
        self.view.media_image.setAlignment(Qt.AlignCenter)
        self.view.media_image.setPixmap(pixmap)

    def create_dummy_data(self) -> None:
        self.media = MediaDto(
            title="The Matrix",
            type="Movie",
            year="1999",
            rating="8.7",
            imdbID="tt0133093",
            poster="https://m.media-amazon.com/images/M/MV5BOTA5NjhiOTAtZWM0ZC00MWNhLThiMzEtZDFkOTk2OTU1ZDJkXkEyXkFqcGdeQXVyMTA4NDI1NTQx._V1_SX300.jpg",
        )
        self.set_media()

    def handle_ai_tags(self) -> None:
        image_tags: list[str] = ImageModel().post_image(image=self.image)

        # take the 3 first tags
        tag1, tag2, tag3 = "", "", ""
        if len(image_tags) >= 1:
            tag1 = image_tags[0]
        if len(image_tags) >= 2:
            tag2 = image_tags[1]
        if len(image_tags) >= 3:
            tag3 = image_tags[2]

        self.view.tag1.setText(tag1)
        self.view.tag2.setText(tag2)
        self.view.tag3.setText(tag3)

        self.view.tag1.show()
        self.view.tag2.show()
        self.view.tag3.show()
