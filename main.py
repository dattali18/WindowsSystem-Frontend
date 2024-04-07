import sys

from PySide6.QtWidgets import QApplication

from Controllers import LibrariesController, MediaController, MovieController
from Models import LibrariesModel, MoviesModel
from Views import (
    LibrariesViewWindow,
    MediaViewWindow,
    MovieViewWindow,
    LibraryViewWindow,
)


def library_window() -> None:
    """Show library window."""
    app = QApplication(sys.argv)
    # controller = LibrariesController(view=LibrariesViewWindow(), model=LibrariesModel())
    # controller.window.show()
    window = LibraryViewWindow()
    window.show()
    sys.exit(app.exec())


def libraries_window() -> None:
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


def movie_window() -> None:
    """Show movie window."""
    app = QApplication(sys.argv)
    controller = MovieController(view=MovieViewWindow(), model=MoviesModel())
    controller.window.show()
    sys.exit(app.exec())


def main() -> None:
    libraries_window()


if __name__ == "__main__":
    main()
