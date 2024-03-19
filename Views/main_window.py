from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMenu,
    QWidget,
    QVBoxLayout,
    QPushButton
    )
from PySide6.QtGui import QAction
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from .frame_1 import Ui_Frame_1
from .frame_2 import Ui_Frame_2



class Frame_1(QWidget):
    def __init__(self, parent=None):
        super(Frame_1, self).__init__(parent)

        self.m_ui = Ui_Frame_1()
        self.m_ui.setupUi(self)

class Frame_2(QWidget):
    def __init__(self, parent=None):
        super(Frame_2, self).__init__(parent)

        self.m_ui = Ui_Frame_2()
        self.m_ui.setupUi(self)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 860, 600)

        # Create the menu bar
        menubar = self.menuBar()

        # Create a menu
        menu = menubar.addMenu('MyMenu')

        # Create actions for the menu options
        action_s1 = QAction('Option S1', self)
        action_s2 = QAction('Option S2', self)

        # Connect actions to functions
        action_s1.triggered.connect(self.option_s1_selected)
        action_s2.triggered.connect(self.option_s2_selected)

        # Add actions to the menu
        menu.addAction(action_s1)
        menu.addAction(action_s2)

        # Set the menu bar
        self.setMenuBar(menubar)

        self.option_s1_selected()

    def option_s1_selected(self):
        print("Option S1 Selected")
        frame = Frame_1()
        self.change_widget(frame)
        
    def option_s2_selected(self):
        print("Option S2 Selected")
        frame = Frame_2()
        self.change_widget(frame)
       
     
    def change_widget(self,currentframe):
        # Create a new central widget
        new_widget = QWidget(self)
        new_layout = QVBoxLayout(new_widget)

        # Add content to the new widget
        # new_layout.addWidget(currentframe)
    
        # Set the new widget as the central widget
        self.setCentralWidget(currentframe)