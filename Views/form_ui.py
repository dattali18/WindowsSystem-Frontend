# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u"icon.JPG", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionSearch = QAction(MainWindow)
        self.actionSearch.setObjectName(u"actionSearch")
        self.actionCreate = QAction(MainWindow)
        self.actionCreate.setObjectName(u"actionCreate")
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName(u"actionUpdate")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setPointSize(13)
        self.centralwidget.setFont(font1)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 801, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.search_field = QLineEdit(self.verticalLayoutWidget)
        self.search_field.setObjectName(u"search_field")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.search_field.setFont(font2)
        self.search_field.setStyleSheet(u"padding: 2 10;\n"
"")
        self.search_field.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.search_field)

        self.search_btn = QPushButton(self.verticalLayoutWidget)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setFont(font1)
        icon1 = QIcon(QIcon.fromTheme(u"zoom-in"))
        self.search_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.search_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.libraries_table = QTableWidget(self.verticalLayoutWidget)
        self.libraries_table.setObjectName(u"libraries_table")

        self.verticalLayout.addWidget(self.libraries_table)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.create_btn = QPushButton(self.verticalLayoutWidget)
        self.create_btn.setObjectName(u"create_btn")

        self.horizontalLayout_2.addWidget(self.create_btn)

        self.update_btn = QPushButton(self.verticalLayoutWidget)
        self.update_btn.setObjectName(u"update_btn")

        self.horizontalLayout_2.addWidget(self.update_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuSearch = QMenu(self.menubar)
        self.menuSearch.setObjectName(u"menuSearch")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSearch.menuAction())
        self.menuSearch.addAction(self.actionSearch)
        self.menuSearch.addSeparator()
        self.menuSearch.addAction(self.actionCreate)
        self.menuSearch.addAction(self.actionUpdate)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Media Library", None))
        self.actionSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
#if QT_CONFIG(shortcut)
        self.actionSearch.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionCreate.setText(QCoreApplication.translate("MainWindow", u"Create", None))
#if QT_CONFIG(shortcut)
        self.actionCreate.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionUpdate.setText(QCoreApplication.translate("MainWindow", u"Update", None))
#if QT_CONFIG(shortcut)
        self.actionUpdate.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+U", None))
#endif // QT_CONFIG(shortcut)
        self.search_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Term", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
#if QT_CONFIG(shortcut)
        self.search_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.create_btn.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.menuSearch.setTitle(QCoreApplication.translate("MainWindow", u"Actions", None))
    # retranslateUi

