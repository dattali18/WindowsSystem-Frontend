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
    AI_Tags_button
    HStack {
        Tag1: QLabel
        Tag2: QLabel
        Tag3: QLabel
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
    QListWidget,
)

from PySide6.QtCore import Qt


class MediaView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # setting up the ui
        self.setWindowTitle("Media Info")
        self.setGeometry(120, 50, 800, 600)

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

        self.media_type = QLabel("Type: ")
        self.media_details_layout.addWidget(self.media_type)

        self.media_imdb_id = QLabel("IMDB: ")
        self.media_details_layout.addWidget(self.media_imdb_id)

        self.h_layout.addWidget(self.media_details_group)

        # setting up the image of the media
        self.media_image = QLabel()
        # setting the image to take half the
        # width of the window and 80% of the height
        self.media_image.setFixedSize(400, 480)
        # centering the image in the label
        self.h_layout.addWidget(self.media_image)

        # setting up the main widget
        self.central_widget.setLayout(self.vertical_layout)

        self.vertical_layout.addLayout(self.h_layout)

        # button to trigger Imagga
        self.ai_tags_button = QPushButton("Generate AI Tags")
        self.vertical_layout.addWidget(self.ai_tags_button)

        # setting up the tags
        self.tags_layout = QHBoxLayout()
        self.vertical_layout.addLayout(self.tags_layout)

        self.tag1 = QLabel("Tag 1")
        self.tags_layout.addWidget(self.tag1)

        self.tag2 = QLabel("Tag 2")
        self.tags_layout.addWidget(self.tag2)

        self.tag3 = QLabel("Tag 3")
        self.tags_layout.addWidget(self.tag3)

        # center the text in the tags
        self.tag1.setAlignment(Qt.AlignCenter)
        self.tag2.setAlignment(Qt.AlignCenter)
        self.tag3.setAlignment(Qt.AlignCenter)

        # make the text bigger & bolder
        font = self.tag1.font()
        font.setPointSize(18)
        self.tag1.setFont(font)
        self.tag2.setFont(font)
        self.tag3.setFont(font)

        # hide the tags initially
        self.tag1.hide()
        self.tag2.hide()
        self.tag3.hide()

        self.setCentralWidget(self.central_widget)
