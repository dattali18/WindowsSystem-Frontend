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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.frame1_action = QAction(MainWindow)
        self.frame1_action.setObjectName(u"frame1_action")
        self.frame2_action = QAction(MainWindow)
        self.frame2_action.setObjectName(u"frame2_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 781, 531))
        self.frame_1 = QWidget()
        self.frame_1.setObjectName(u"frame_1")
        self.verticalLayoutWidget = QWidget(self.frame_1)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 751, 491))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(9, 29, 731, 211))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setPointSize(13)
        self.pushButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)

        self.verticalLayout.addWidget(self.groupBox_2)

        self.tabWidget.addTab(self.frame_1, "")
        self.frame_2 = QWidget()
        self.frame_2.setObjectName(u"frame_2")
        self.tabWidget.addTab(self.frame_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        self.menuFrames = QMenu(self.menubar)
        self.menuFrames.setObjectName(u"menuFrames")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFrames.menuAction())
        self.menuFrames.addAction(self.frame1_action)
        self.menuFrames.addAction(self.frame2_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Library View", None))
        self.frame1_action.setText(QCoreApplication.translate("MainWindow", u"Frame 1", None))
#if QT_CONFIG(shortcut)
        self.frame1_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+1", None))
#endif // QT_CONFIG(shortcut)
        self.frame2_action.setText(QCoreApplication.translate("MainWindow", u"Frame 2", None))
#if QT_CONFIG(shortcut)
        self.frame2_action.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+2", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Group 1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Group 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.frame_1), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.frame_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuFrames.setTitle(QCoreApplication.translate("MainWindow", u"Frames", None))
    # retranslateUi

