from PySide6 import QtWidgets

from .movie_ui import Ui_MainWindow


class MovieViewWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MovieViewWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
