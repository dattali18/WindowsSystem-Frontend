# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame_1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_Frame_1(object):
    def setupUi(self, Frame_1):
        if not Frame_1.objectName():
            Frame_1.setObjectName("Frame_1")
        Frame_1.resize(640, 480)
        self.verticalLayoutWidget = QWidget(Frame_1)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 860, 600))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        # ifndef Q_OS_MAC
        self.horizontalLayout_3.setSpacing(-1)
        # endif
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.header = QLabel(self.verticalLayoutWidget)
        self.header.setObjectName("header")
        font = QFont()
        font.setPointSize(18)
        self.header.setFont(font)

        self.horizontalLayout_3.addWidget(self.header)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.back_btn = QPushButton(self.verticalLayoutWidget)
        self.back_btn.setObjectName("back_btn")
        self.back_btn.setMaximumSize(QSize(32, 32))
        icon = QIcon()
        icon.addFile("icons/chevron.backward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_btn.setIcon(icon)
        self.back_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.back_btn)

        self.forward_btn = QPushButton(self.verticalLayoutWidget)
        self.forward_btn.setObjectName("forward_btn")
        self.forward_btn.setMaximumSize(QSize(32, 32))
        icon1 = QIcon()
        icon1.addFile("icons/chevron.forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.forward_btn.setIcon(icon1)
        self.forward_btn.setFlat(True)

        self.horizontalLayout_3.addWidget(self.forward_btn)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_field = QLineEdit(self.verticalLayoutWidget)
        self.search_field.setObjectName("search_field")
        self.search_field.setFont(font)

        self.horizontalLayout.addWidget(self.search_field)

        self.search_btn = QPushButton(self.verticalLayoutWidget)
        self.search_btn.setObjectName("search_btn")
        icon2 = QIcon()
        icon2.addFile("icons/magnifyingglass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.search_btn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.playlist_table = QTableWidget(self.verticalLayoutWidget)
        self.playlist_table.setObjectName("playlist_table")
        font1 = QFont()
        font1.setPointSize(16)
        self.playlist_table.setFont(font1)

        self.verticalLayout.addWidget(self.playlist_table)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.create_btn = QPushButton(self.verticalLayoutWidget)
        self.create_btn.setObjectName("create_btn")

        self.horizontalLayout_2.addWidget(self.create_btn)

        self.update_btn = QPushButton(self.verticalLayoutWidget)
        self.update_btn.setObjectName("update_btn")

        self.horizontalLayout_2.addWidget(self.update_btn)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Frame_1)

        QMetaObject.connectSlotsByName(Frame_1)

    # setupUi

    def retranslateUi(self, Frame_1):
        Frame_1.setWindowTitle(QCoreApplication.translate("Frame_1", "Frame", None))
        self.header.setText(
            QCoreApplication.translate("Frame_1", "Search Playlist", None)
        )
        self.back_btn.setText("")
        self.forward_btn.setText("")
        self.search_btn.setText(QCoreApplication.translate("Frame_1", "search", None))
        self.create_btn.setText(QCoreApplication.translate("Frame_1", "Create", None))
        self.update_btn.setText(QCoreApplication.translate("Frame_1", "Update", None))

    # retranslateUi
