# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'library.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 10, 1161, 731))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 40, 531, 671))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.search_edit = QLineEdit(self.verticalLayoutWidget)
        self.search_edit.setObjectName(u"search_edit")
        font1 = QFont()
        font1.setPointSize(13)
        self.search_edit.setFont(font1)
        self.search_edit.setStyleSheet(u"padding: 2;")

        self.horizontalLayout_2.addWidget(self.search_edit)

        self.combo_box = QComboBox(self.verticalLayoutWidget)
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.setObjectName(u"combo_box")
        self.combo_box.setFont(font1)

        self.horizontalLayout_2.addWidget(self.combo_box)

        self.search_btn = QPushButton(self.verticalLayoutWidget)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setFont(font1)

        self.horizontalLayout_2.addWidget(self.search_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.search_lst = QListWidget(self.verticalLayoutWidget)
        self.search_lst.setObjectName(u"search_lst")
        font2 = QFont()
        font2.setPointSize(14)
        self.search_lst.setFont(font2)

        self.verticalLayout.addWidget(self.search_lst)

        self.add_btn = QPushButton(self.verticalLayoutWidget)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setFont(font1)
        self.add_btn.setAutoDefault(False)
        self.add_btn.setFlat(False)

        self.verticalLayout.addWidget(self.add_btn)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.horizontalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 40, 531, 671))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.name_edit = QLineEdit(self.verticalLayoutWidget_2)
        self.name_edit.setObjectName(u"name_edit")
        self.name_edit.setFont(font1)
        self.name_edit.setStyleSheet(u"padding: 2;")

        self.verticalLayout_2.addWidget(self.name_edit)

        self.library_lst = QListWidget(self.verticalLayoutWidget_2)
        self.library_lst.setObjectName(u"library_lst")
        self.library_lst.setFont(font1)

        self.verticalLayout_2.addWidget(self.library_lst)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.create_btn = QPushButton(self.verticalLayoutWidget_2)
        self.create_btn.setObjectName(u"create_btn")
        self.create_btn.setFont(font1)
        self.create_btn.setFlat(False)

        self.horizontalLayout_3.addWidget(self.create_btn)

        self.remove_btn = QPushButton(self.verticalLayoutWidget_2)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.remove_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.create_btn.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Libary Creation", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Search For Media", None))
        self.search_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search for media", None))
        self.combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Movies", None))
        self.combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"TV Series", None))

        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"add", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Your Libary", None))
        self.name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Library name", None))
        self.create_btn.setText(QCoreApplication.translate("MainWindow", u"create", None))
        self.remove_btn.setText(QCoreApplication.translate("MainWindow", u"remove", None))
    # retranslateUi

