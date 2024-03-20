import sys

from PySide6.QtWidgets import QApplication

from Views import MainWindow, Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    controller = Controller(view=window)
    window.show()
    sys.exit(app.exec())
