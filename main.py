import sys

from PySide6.QtWidgets import QApplication

# from Controllers import MediaController
# from Models import MoviesModel
# from Views import MediaViewWindow

from Controllers import MovieController
from Models import MoviesModel
from Views import MovieViewWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = MainWindow()
    # controller = Controller(view=window, model=LibrariesModel())
    # controller.window.show()

    # controller = MediaController(view=MediaViewWindow(), model=MoviesModel())
    # controller.window.show()

    controller = MovieController(view=MovieViewWindow(), model=MoviesModel())
    controller.window.show()
    sys.exit(app.exec())
