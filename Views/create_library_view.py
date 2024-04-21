# this window is used to create a new library
"""
VStack {
    Title
    HStack {
        Label
        TextField
    }
    GroupBox {
        Checkbox1("Horror"),
        Checkbox2("Comedy"),
        Checkbox3("Action"),
        Checkbox4("Drama"),
        Checkbox5("Romance"),
        Checkbox6("Sci-Fi")
    }
    Button
}
"""
from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QGroupBox,
    QVBoxLayout,
    QCheckBox,
    QWidget,
)


class CreateLibraryView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Create Library")
        self.setGeometry(120, 50, 550, 300)

        self.centralWidget = QWidget(self)

        self.layout = QVBoxLayout()
        # setting up the padding
        self.layout.setContentsMargins(20, 10, 20, 20)

        # setting up the title
        self.title = QLabel("Create Library")
        self.layout.addWidget(self.title)

        # setting up the font for the title
        font = self.title.font()
        font.setPointSize(20)
        self.title.setFont(font)

        # setting up the name label and text field
        self.name_label = QLabel("Name")
        self.name_text = QLineEdit()
        # adding a placeholder text
        self.name_text.setPlaceholderText("Enter the name of the library")
        # adding padding inside the text edit
        self.name_text.setStyleSheet("padding: 5px 10px")

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_text)

        # creating the checkboxes
        self.group_box = QGroupBox("Genres")
        # setting up the font for the group box
        font = self.group_box.font()
        font.setPointSize(15)
        self.group_box.setFont(font)

        # setting up the layout for the group box
        self.group_box_layout = QVBoxLayout()

        genre: list[str] = ["Horror", "Comedy",
                            "Action", "Drama", "Romance", "Sci-Fi"]

        # putting checkboxes in dict so it can be accessed later by the key
        self.checkboxes_dict = {genre: QCheckBox(genre) for genre in genre}

        for checkbox in self.checkboxes_dict.values():
            self.group_box_layout.addWidget(checkbox)

        self.group_box.setLayout(self.group_box_layout)
        self.layout.addWidget(self.group_box)

        self.create_button = QPushButton("Create")
        self.create_button.setProperty("default", True)
        self.layout.addWidget(self.create_button)

        self.centralWidget.setLayout(self.layout)

        self.setCentralWidget(self.centralWidget)
