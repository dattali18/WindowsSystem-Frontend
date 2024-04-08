# this is the file for the library view in pyside6

from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QTableWidgetItem,
    QHeaderView,
    QHBoxLayout,
    QPushButton,
    QGroupBox,
    QCheckBox,
    QLabel,
)
from PySide6.QtCore import Qt


class LibrariesView(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Media Library System")

        # open the window at the center of the screen
        self.setGeometry(0, 0, 1200, 800)

        # creating the widgets
        # main vertical layout
        self.central_widget = QWidget(self)
        self.vertical_layout = QVBoxLayout(self.central_widget)

        # putting in padding
        self.vertical_layout.setContentsMargins(
            30, 20, 30, 20
        )  # left, top, right, bottom padding

        # title label
        self.title_label = QLabel("My Media Libraries", self.central_widget)
        # setting the font size
        font = self.title_label.font()
        font.setPointSize(30)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)  # align the text to the center

        # add the title label to the vertical layout
        self.vertical_layout.addWidget(self.title_label)

        # horizontal layout
        self.horizontalLayout = QHBoxLayout()
        # search bar
        self.search_bar = QLineEdit(self.central_widget)
        self.search_bar.setPlaceholderText("Search for library by name")
        self.search_bar.setStyleSheet("QLineEdit { padding: 5px; }")  # setting padding
        # search button
        self.search_button = QPushButton("Search", self.central_widget)

        # adding the search bar to the horizontal layout
        self.horizontalLayout.addWidget(self.search_bar)
        self.horizontalLayout.addWidget(self.search_button)

        # add the horizontal layout to the vertical layout
        self.vertical_layout.addLayout(self.horizontalLayout)

        # creating a group box
        self.group_box = QGroupBox("Genre", self.central_widget)
        # setting the font size for the group box title
        font = self.group_box.font()
        font.setPointSize(16)
        self.group_box.setFont(font)
        # creating a layout for the group box
        self.group_box_layout = QHBoxLayout()
        # list of items
        genre = ["Sci Fi", "Action", "Romance", "Adventure", "Horror", "Comedy"]
        # creating checkboxes and adding them to the group box layout
        self.checkboxes = {
            genre: QCheckBox(genre, self.central_widget) for genre in genre
        }

        for checkbox in self.checkboxes.values():
            # checkbox = QCheckBox(item, self.central_widget)
            self.group_box_layout.addWidget(checkbox)

        # setting the layout for the group box
        self.group_box.setLayout(self.group_box_layout)
        # adding the group box to the main vertical layout
        self.vertical_layout.addWidget(self.group_box)

        # adding a list widget to the vertical layout below the search bar
        self.table_widget = QTableWidget(self.central_widget)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        self.table_widget.setHorizontalHeaderItem(1, QTableWidgetItem("Keywords"))
        self.table_widget.setHorizontalHeaderItem(2, QTableWidgetItem("Media"))

        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # add the list widget to the vertical layout
        self.vertical_layout.addWidget(self.table_widget)

        # adding a group of buttons (Add, Update, Delete)
        self.button_group = QHBoxLayout()
        # add button
        self.add_button = QPushButton("Add", self.central_widget)
        # making the add button a primary button
        self.add_button.setProperty("default", True)

        # update button
        self.update_button = QPushButton("Update", self.central_widget)
        # delete button
        self.delete_button = QPushButton("Delete", self.central_widget)

        # add the buttons to the button group
        self.button_group.addWidget(self.add_button)
        self.button_group.addWidget(self.update_button)
        self.button_group.addWidget(self.delete_button)

        # add the button group to the vertical layout
        self.vertical_layout.addLayout(self.button_group)

        # set the layout of the central widget
        self.central_widget.setLayout(self.vertical_layout)
        # set the central widget of the QMainWindow
        self.setCentralWidget(self.central_widget)
