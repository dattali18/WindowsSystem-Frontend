# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 781, 631))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_field = QLineEdit(self.verticalLayoutWidget)
        self.search_field.setObjectName(u"search_field")
        font = QFont()
        font.setPointSize(14)
        self.search_field.setFont(font)
        self.search_field.setStyleSheet(u"padding: 2 10;")
        self.search_field.setFrame(False)

        self.horizontalLayout.addWidget(self.search_field)

        self.combo_box = QComboBox(self.verticalLayoutWidget)
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.setObjectName(u"combo_box")
        font1 = QFont()
        font1.setPointSize(13)
        self.combo_box.setFont(font1)

        self.horizontalLayout.addWidget(self.combo_box)

        self.search_btn = QPushButton(self.verticalLayoutWidget)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setFont(font1)
        self.search_btn.setAutoDefault(False)
        self.search_btn.setFlat(False)

        self.horizontalLayout.addWidget(self.search_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.media_table = QTableWidget(self.verticalLayoutWidget)
        self.media_table.setObjectName(u"media_table")

        self.verticalLayout.addWidget(self.media_table)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.search_btn.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Media View", None))
        self.search_field.setText("")
        self.search_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Seach For Movies/Tv Series", None))
        self.combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Movies", None))
        self.combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Tv Series", None))

        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
    # retranslateUi

