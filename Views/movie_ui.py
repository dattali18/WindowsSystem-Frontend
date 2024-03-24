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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 5, 621, 411))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.horizontalLayoutWidget)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(24)
        self.title.setFont(font)

        self.verticalLayout.addWidget(self.title, 0, Qt.AlignHCenter)

        self.rating = QLabel(self.horizontalLayoutWidget)
        self.rating.setObjectName(u"rating")
        font1 = QFont()
        font1.setPointSize(18)
        self.rating.setFont(font1)

        self.verticalLayout.addWidget(self.rating)

        self.imdb = QLabel(self.horizontalLayoutWidget)
        self.imdb.setObjectName(u"imdb")
        self.imdb.setFont(font1)

        self.verticalLayout.addWidget(self.imdb)

        self.year = QLabel(self.horizontalLayoutWidget)
        self.year.setObjectName(u"year")
        self.year.setFont(font1)

        self.verticalLayout.addWidget(self.year)

        self.genre = QLabel(self.horizontalLayoutWidget)
        self.genre.setObjectName(u"genre")
        self.genre.setFont(font1)

        self.verticalLayout.addWidget(self.genre)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.image = QLabel(self.horizontalLayoutWidget)
        self.image.setObjectName(u"image")

        self.horizontalLayout.addWidget(self.image)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Movie TItle", None))
        self.rating.setText(QCoreApplication.translate("MainWindow", u"rating", None))
        self.imdb.setText(QCoreApplication.translate("MainWindow", u"imdb ID", None))
        self.year.setText(QCoreApplication.translate("MainWindow", u"year", None))
        self.genre.setText(QCoreApplication.translate("MainWindow", u"genre", None))
        self.image.setText(QCoreApplication.translate("MainWindow", u"Image", None))
    # retranslateUi

