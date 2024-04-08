# this is the window that will display the media (Movie, Tv Series) type
# window layout:
"""
VStack {
    Title_label
    HStack {
        Media_image
        Media_details_group {
            Media_year
            Media_genre
            Media_rating
            Media_Imdb_Id
        }
    }
}
"""

from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLabel,
    QHBoxLayout,
    QGroupBox,
    QPushButton,
    QCheckBox,
    QLineEdit,
)
from PySide6.QtGui import QPixmap

from PySide6.QtCore import Qt


class MediaView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # setting up the ui
        self.setWindowTitle("Media Info")
        self.setGeometry(0, 0, 800, 600)

        # setting up central widget
        self.central_widget = QWidget(self)
        self.vertical_layout = QVBoxLayout(self.central_widget)

        # putting in padding
        # left, top, right, bottom padding
        self.vertical_layout.setContentsMargins(20, 10, 20, 20)

        # setting up the title label
        self.title_label = QLabel("Media Title")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.vertical_layout.addWidget(self.title_label)
        # font of the title label
        font = self.title_label.font()
        font.setPointSize(20)
        font.setBold(True)
        self.title_label.setFont(font)

        # setting up the H layout
        self.h_layout = QHBoxLayout()

        # setting up the group box for media details
        self.media_details_group = QGroupBox("Media Details")
        self.media_details_layout = QVBoxLayout()
        self.media_details_group.setLayout(self.media_details_layout)

        # setting the font size of the group box
        font = self.media_details_group.font()
        font.setPointSize(15)
        self.media_details_group.setFont(font)


        # setting up the media details
        self.media_year = QLabel("Year: ")
        self.media_details_layout.addWidget(self.media_year)

        self.media_genre = QLabel("Genre: ")
        self.media_details_layout.addWidget(self.media_genre)

        self.media_rating = QLabel("Rating: ")
        self.media_details_layout.addWidget(self.media_rating)

        self.imdb_id = QLabel("IMDB: ")
        self.media_details_layout.addWidget(self.imdb_id)

        self.h_layout.addWidget(self.media_details_group)

        # setting up the image of the media
        self.media_image = QLabel()
        # setting the image to take half the width of the window and 80% of the height
        self.media_image.setFixedSize(400, 480)
        # load the example image from /static/images/movie_poster.jpg
        pix_map: QPixmap = QPixmap("static/images/movie_poster.jpg")
        # setting up the aspect ratio of the image
        pix_map = pix_map.scaled(
            self.media_image.width(),
            self.media_image.height(),
            Qt.KeepAspectRatio,
            Qt.FastTransformation,
        )
        # centering the image in the label
        self.media_image.setAlignment(Qt.AlignCenter)
        self.media_image.setPixmap(pix_map)
        self.h_layout.addWidget(self.media_image)

        # setting up the main widget
        self.central_widget.setLayout(self.vertical_layout)

        self.vertical_layout.addLayout(self.h_layout)

        self.setCentralWidget(self.central_widget)
