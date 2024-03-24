import sys

from PySide6.QtWidgets import QApplication

from Views import LibrariesViewWindow, MediaController, MediaViewWindow
from Models import LibrariesModel, MoviesModel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = MainWindow()
    # controller = Controller(view=window, model=LibrariesModel())
    # controller.window.show()

    frame1 = MediaViewWindow()
    controller = MediaController(view=frame1, model=MoviesModel())
    frame1.show()
    sys.exit(app.exec())
