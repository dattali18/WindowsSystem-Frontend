# this will be the window to modify a library
"""
VStack {
    Title
    HStack {
        VStack {
            HStack {
                Label,
                ComboBox,
                TextField,
            },
            ListView
        },
        VStack {
            ListView,
            HStack {
                Button,
                Button
            }
        }
    }
}
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QListView,
    QWidget,
)


class UpdateLibraryView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Update Library")
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

        # horizontal layout I
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # inner vertical layout
        self.inner_vertical_layout = QVBoxLayout()
        self.inner_vertical_layout.setObjectName("inner_vertical_layout")

        # inner horizontal layout for search bar and combo box
        self.inner_horizontal_layout = QHBoxLayout()
        self.inner_horizontal_layout.setObjectName("inner_horizontal_layout")

        # search bar
        self.search_bar = QLineEdit(self.central_widget)
        self.search_bar.setPlaceholderText("Search for media")
        self.search_bar.setStyleSheet("QLineEdit { padding: 5px; }")

        # combo box for Movies/Tv Series search
        self.filter_combo = QComboBox(self.central_widget)
        self.filter_combo.addItem("All")
        self.filter_combo.addItem("Movies")
        self.filter_combo.addItem("TV Series")

        # search button
        self.search_button = QPushButton("Search", self.central_widget)

        self.inner_horizontal_layout.addWidget(self.search_bar)
        self.inner_horizontal_layout.addWidget(self.filter_combo)
        self.inner_horizontal_layout.addWidget(self.search_button)

        self.inner_vertical_layout.addLayout(self.inner_horizontal_layout)

        # list view
        self.search_media_list = QListView(self.central_widget)
        self.inner_vertical_layout.addWidget(self.search_media_list)

        self.horizontalLayout.addLayout(self.inner_vertical_layout)

        self.vertical_layout.addLayout(self.horizontalLayout)

        # horizontal layout II
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # list view
        self.media_list = QListView(self.central_widget)

        # buttons
        self.add_button = QPushButton("Add", self.central_widget)
        self.remove_button = QPushButton("Remove", self.central_widget)
        self.update_button = QPushButton("Update", self.central_widget)
        self.update_button.setProperty("default", True)

        self.horizontalLayout_2.addWidget(self.add_button)
        self.horizontalLayout_2.addWidget(self.remove_button)
        self.horizontalLayout_2.addWidget(self.update_button)

        self.vertical_layout.addWidget(self.media_list)

        self.vertical_layout.addLayout(self.horizontalLayout_2)

        self.setCentralWidget(self.central_widget)
