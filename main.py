import sys

from PySide6.QtWidgets import QApplication

from Views import MainWindow, Controller, Frame1Window
from Models import LibrariesModel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = MainWindow()
    # controller = Controller(view=window, model=LibrariesModel())
    # controller.window.show()
    frame1 = Frame1Window()
    frame1.show()
    sys.exit(app.exec())
