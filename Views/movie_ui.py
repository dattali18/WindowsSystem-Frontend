# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'movie.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 631, 431))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.verticalLayoutWidget)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setMargin(10)

        self.verticalLayout_2.addWidget(self.title, 0, Qt.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(25, -1, -1, -1)
        self.rating = QLabel(self.verticalLayoutWidget)
        self.rating.setObjectName(u"rating")
        font1 = QFont()
        font1.setPointSize(20)
        self.rating.setFont(font1)

        self.verticalLayout.addWidget(self.rating)

        self.imdb = QLabel(self.verticalLayoutWidget)
        self.imdb.setObjectName(u"imdb")
        self.imdb.setFont(font1)

        self.verticalLayout.addWidget(self.imdb)

        self.year = QLabel(self.verticalLayoutWidget)
        self.year.setObjectName(u"year")
        self.year.setFont(font1)

        self.verticalLayout.addWidget(self.year)

        self.genre = QLabel(self.verticalLayoutWidget)
        self.genre.setObjectName(u"genre")
        self.genre.setFont(font1)
        self.genre.setWordWrap(True)

        self.verticalLayout.addWidget(self.genre)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.image = QLabel(self.verticalLayoutWidget)
        self.image.setObjectName(u"image")
        self.image.setFrameShape(QFrame.WinPanel)
        self.image.setFrameShadow(QFrame.Plain)
        self.image.setLineWidth(1)
        self.image.setMargin(0)
        self.image.setIndent(-1)

        self.horizontalLayout.addWidget(self.image)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Movie Window", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Movie TItle", None))
        self.rating.setText(QCoreApplication.translate("MainWindow", u"rating", None))
        self.imdb.setText(QCoreApplication.translate("MainWindow", u"imdb ID", None))
        self.year.setText(QCoreApplication.translate("MainWindow", u"year", None))
        self.genre.setText(QCoreApplication.translate("MainWindow", u"genre", None))
        self.image.setText(QCoreApplication.translate("MainWindow", u"Image", None))
    # retranslateUi

