# this file will be used to create the library view in pyside6
# the will contain
# - a title label at the top "Library Title"
# - a search bar and a search button
# - a group box for filtering the media
# - a list of media (movies, tv series)
# - a button group with (Update, Delete)

from PySide6.QtWidgets import QMainWindow

from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QListWidget,
    QHBoxLayout,
    QPushButton,
    QGroupBox,
    QCheckBox,
    QLabel,
    QComboBox,
)

from PySide6.QtCore import Qt


class LibraryView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Media Library")
        self.setGeometry(0, 0, 1200, 800)

        # creating the widgets
        # main vertical layout
        self.central_widget = QWidget(self)
        self.vertical_layout = QVBoxLayout(self.central_widget)

        # putting in padding
        self.vertical_layout.setContentsMargins(30, 20, 30, 20)

        # title label
        self.title_label = QLabel("Library Name", self.central_widget)
        font = self.title_label.font()
        font.setPointSize(30)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)

        # add the title label to the vertical layout
        self.vertical_layout.addWidget(self.title_label)

        # horizontal layout
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        # search bar
        self.search_bar = QLineEdit(self.central_widget)
        self.search_bar.setPlaceholderText("Search for media")
        self.search_bar.setStyleSheet("QLineEdit { padding: 5px; }")

        # combo box for Movies/Tv Series search
        self.filter_combo = QComboBox(self.central_widget)
        self.filter_combo.addItem("All")
        self.filter_combo.addItem("Movies")
        self.filter_combo.addItem("TV Series")

        self.horizontalLayout.addWidget(self.search_bar)
        self.horizontalLayout.addWidget(self.filter_combo)

        self.vertical_layout.addLayout(self.horizontalLayout)

        # search button
        self.search_button = QPushButton("Search", self.central_widget)

        # adding the search bar to the horizontal layout
        self.horizontalLayout.addWidget(self.search_bar)
        self.horizontalLayout.addWidget(self.filter_combo)
        self.horizontalLayout.addWidget(self.search_button)

        # list of media
        self.media_list = QListWidget(self.central_widget)
        self.vertical_layout.addWidget(self.media_list)

        # button group
        self.button_group = QHBoxLayout()
        self.button_group.setObjectName("button_group")
        self.update_button = QPushButton("Update", self.central_widget)
        self.delete_button = QPushButton("Delete", self.central_widget)

        self.button_group.addWidget(self.update_button)
        self.button_group.addWidget(self.delete_button)

        self.vertical_layout.addLayout(self.button_group)

        self.setCentralWidget(self.central_widget)
