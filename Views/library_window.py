from PySide6 import QtWidgets

from .library_ui import Ui_MainWindow


class LibraryViewWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LibraryViewWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
