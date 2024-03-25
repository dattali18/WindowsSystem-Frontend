from .movie_controller import MovieController
from Views import MediaViewWindow, MovieViewWindow
from Models import MoviesModel, MediaDto

from PySide6.QtWidgets import (
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QLineEdit,
    QComboBox,
)

from typing import Optional


class MediaController:
    def __init__(self, view: MediaViewWindow, model: MoviesModel):
        self.view = view.ui
        self.window = view
        self.model = model

        self.media: Optional[list[MediaDto]] = None

        self.movie_controller: Optional[MovieController]

        # Defining the component
        self.search_btn: QPushButton = self.view.search_btn
        self.search_field: QLineEdit = self.view.search_field
        self.combo_box: QComboBox = self.view.combo_box
        self.media_table: QTableWidget = self.view.media_table

        # connecting the component
        self.search_btn.clicked.connect(self.handle_search)
        self.view.media_table.cellDoubleClicked.connect(self.handle_click)

        self.view.media_table.horizontalHeader().setStretchLastSection(True)
        self.view.media_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        # self.add_random_data_for_debug()
        self.populate_media_table()

    def handle_click(self, row: int, column: int):
        # print(f"item clicked at {row=}, {column=}")
        imdbID = self.media[row].imdbID
        self.movie_controller = MovieController(
            imdbID=imdbID, view=MovieViewWindow(), model=MoviesModel()
        )
        self.movie_controller.window.show()

    def handle_search(self):
        print("Search button clicked")
        search_term: str = self.search_field.text()
        print(search_term)
        if search_term == "":
            # TODO - for yair, when you finish the TvSeries model update to add also tvseriesModel.get_series()
            self.media = []
        else:
            self.media = self.model.get_movies_search(s=search_term)
        self.populate_media_table()

    def populate_media_table(self):
        # deleting all the old entries
        self.view.media_table.setRowCount(0)
        self.view.media_table.setColumnCount(4)

        self.view.media_table.setHorizontalHeaderItem(0, QTableWidgetItem("Title"))
        self.view.media_table.setHorizontalHeaderItem(1, QTableWidgetItem("Year"))
        self.view.media_table.setHorizontalHeaderItem(2, QTableWidgetItem("Type"))
        self.view.media_table.setHorizontalHeaderItem(3, QTableWidgetItem("Imdb ID"))

        if self.media is None:
            print("404 error please check backend")
            return

        self.view.media_table.setRowCount(len(self.media))

        for i, media in enumerate(self.media):
            self.view.media_table.setItem(i, 0, QTableWidgetItem(media.title))
            self.view.media_table.setItem(i, 1, QTableWidgetItem(media.year))
            self.view.media_table.setItem(i, 2, QTableWidgetItem(media.type))
            self.view.media_table.setItem(i, 3, QTableWidgetItem(media.imdbID))

    def add_random_data_for_debug(self):
        # create a list of MediaDto objects to test the ui
        self.media = [
            MediaDto(
                id=1,
                title="Test Title 1",
                year="2022",
                type="Movie",
                poster="",
                imdbID="tt1234567",
            ),
            MediaDto(
                id=2,
                title="Test Title 2",
                year="2022",
                type="Movie",
                poster="",
                imdbID="tt1234567",
            ),
            MediaDto(
                id=3,
                title="Test Title 3",
                year="2022",
                type="Movie",
                poster="",
                imdbID="tt1234567",
            ),
        ]
