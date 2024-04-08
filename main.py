import sys

from PySide6.QtWidgets import QApplication

from Controllers import LibrariesController, MediaController, MovieController
from Models import LibrariesModel, MoviesModel
from Views import *


def libraries_window() -> None:
    app = QApplication(sys.argv)
    window = LibrariesView()
    window.show()

    # center the window
    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = window.frameGeometry()
    geo.moveCenter(center)
    window.move(geo.topLeft())

    sys.exit(app.exec())


def main() -> None:
    libraries_window()


if __name__ == "__main__":
    main()
