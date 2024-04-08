from Views import MediaView
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
    def __init__(self, view: MediaView, model: MoviesModel):
        self.view = view
        self.model = model

        self.media: Optional[list[MediaDto]] = None
