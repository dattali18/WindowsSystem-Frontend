from PySide6 import QtWidgets

from .form_1_ui import Ui_MainWindow

class LibrariesViewWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LibrariesViewWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
