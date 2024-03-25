import sys

from PySide6.QtWidgets import QApplication

from Controllers import LibrariesController, MediaController, MovieController
from Models import LibrariesModel, MoviesModel
from Views import LibrariesViewWindow, MediaViewWindow, MovieViewWindow


def LibraryWindow() -> None:
    """Show library window."""
    app = QApplication(sys.argv)
    controller = LibrariesController(view=LibrariesViewWindow(), model=LibrariesModel())
    controller.window.show()
    sys.exit(app.exec())


def media_window() -> None:
    """Show media window."""
    app = QApplication(sys.argv)
    controller = MediaController(view=MediaViewWindow(), model=MoviesModel())
    controller.window.show()
    sys.exit(app.exec())


def MovieWindow() -> None:
    """Show movie window."""
    app = QApplication(sys.argv)
    controller = MovieController(view=MovieViewWindow(), model=MoviesModel())
    controller.window.show()
    sys.exit(app.exec())


def main() -> None:
    MediaWindow()


if __name__ == "__main__":
    main()
