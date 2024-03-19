# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame_2.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Frame_2(object):
    def setupUi(self, Frame_2):
        if not Frame_2.objectName():
            Frame_2.setObjectName(u"Frame_2")
        Frame_2.resize(640, 480)
        self.verticalLayoutWidget = QWidget(Frame_2)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 860, 600))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayout_3.setSpacing(-1)
#endif
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.header_2 = QLabel(self.verticalLayoutWidget)
        self.header_2.setObjectName(u"header_2")
        font = QFont()
        font.setPointSize(18)
        self.header_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.header_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.back_btn = QPushButton(self.verticalLayoutWidget)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setMaximumSize(QSize(32, 32))
        icon = QIcon()
        icon.addFile(u"icons/chevron.backward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.back_btn)

        self.forword_btn = QPushButton(self.verticalLayoutWidget)
        self.forword_btn.setObjectName(u"forword_btn")
        self.forword_btn.setMaximumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile(u"icons/chevron.forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.forword_btn.setIcon(icon1)
        self.forword_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.forword_btn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.seach_field = QLineEdit(self.verticalLayoutWidget)
        self.seach_field.setObjectName(u"seach_field")
        self.seach_field.setFont(font)

        self.horizontalLayout.addWidget(self.seach_field)

        self.search_btn = QPushButton(self.verticalLayoutWidget)
        self.search_btn.setObjectName(u"search_btn")
        font1 = QFont()
        font1.setPointSize(13)
        self.search_btn.setFont(font1)
        icon2 = QIcon()
        icon2.addFile(u"icons/magnifyingglass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.search_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.song_table = QTableWidget(self.verticalLayoutWidget)
        self.song_table.setObjectName(u"song_table")
        self.song_table.setFont(font)

        self.verticalLayout.addWidget(self.song_table)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.edit_lbl = QLabel(self.verticalLayoutWidget)
        self.edit_lbl.setObjectName(u"edit_lbl")
        font2 = QFont()
        font2.setPointSize(16)
        self.edit_lbl.setFont(font2)

        self.verticalLayout.addWidget(self.edit_lbl)

        self.name_field = QLineEdit(self.verticalLayoutWidget)
        self.name_field.setObjectName(u"name_field")
        self.name_field.setFont(font)

        self.verticalLayout.addWidget(self.name_field)

        self.playlist_table = QTableWidget(self.verticalLayoutWidget)
        self.playlist_table.setObjectName(u"playlist_table")
        self.playlist_table.setFont(font)

        self.verticalLayout.addWidget(self.playlist_table)

        self.click_lbl = QLabel(self.verticalLayoutWidget)
        self.click_lbl.setObjectName(u"click_lbl")
        self.click_lbl.setFont(font2)

        self.verticalLayout.addWidget(self.click_lbl)

        self.create_btn = QPushButton(self.verticalLayoutWidget)
        self.create_btn.setObjectName(u"create_btn")
        self.create_btn.setFont(font1)

        self.verticalLayout.addWidget(self.create_btn)


        self.retranslateUi(Frame_2)

        QMetaObject.connectSlotsByName(Frame_2)
    # setupUi

    def retranslateUi(self, Frame_2):
        Frame_2.setWindowTitle(QCoreApplication.translate("Frame_2", u"Frame", None))
        self.header_2.setText(QCoreApplication.translate("Frame_2", u"Create Playlist", None))
        self.back_btn.setText("")
        self.forword_btn.setText("")
        self.search_btn.setText(QCoreApplication.translate("Frame_2", u"search", None))
        self.edit_lbl.setText(QCoreApplication.translate("Frame_2", u"name your playlist", None))
        self.click_lbl.setText(QCoreApplication.translate("Frame_2", u"click on the button to create playlist", None))
        self.create_btn.setText(QCoreApplication.translate("Frame_2", u"Create", None))
    # retranslateUi

