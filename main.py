import sys

from PySide6.QtWidgets import QApplication

from Views import MainWindow, Controller
from Models import LibrariesModel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    controller = Controller(view=window, model=LibrariesModel())
    controller.window.show()
    sys.exit(app.exec())
