import sys

from PySide6.QtWidgets import QApplication

# from Controllers import MediaController
# from Models import MoviesModel
# from Views import MediaViewWindow

from Controllers import LibrariesController
from Models import LibrariesModel
from Views import LibrariesViewWindow


def main():
    app = QApplication(sys.argv)

    controller = LibrariesController(view=LibrariesViewWindow(), model=LibrariesModel())
    controller.window.show()

    # controller = MediaController(view=MediaViewWindow(), model=MoviesModel())
    # controller.window.show()

    # controller = MovieController(view=MovieViewWindow(), model=MoviesModel())
    # controller.window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
