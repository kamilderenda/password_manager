# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manager.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.176, x2:1, y2:0.807, stop:0 rgba(197, 223, 248, 255), stop:1 rgba(207, 235, 248, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.176, x2:1, y2:0.807, stop:0 rgba(197, 223, 248, 255), stop:1 rgba(160, 191, 224, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.centralwidget.setMaximumSize(QSize(800, 600))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_head = QFrame(self.centralwidget)
        self.frame_head.setObjectName(u"frame_head")
        self.frame_head.setMinimumSize(QSize(0, 100))
        self.frame_head.setMaximumSize(QSize(16777215, 100))
        self.frame_head.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.222, x2:1, y2:0.733, stop:0 rgba(74, 85, 162, 255), stop:1 rgba(83, 114, 162, 255));")
        self.frame_head.setFrameShape(QFrame.WinPanel)
        self.frame_head.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_head)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_username = QScrollArea(self.frame_head)
        self.frame_username.setObjectName(u"frame_username")
        self.frame_username.setMaximumSize(QSize(400, 16777215))
        self.frame_username.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.00555556, y1:0.188, x2:1, y2:0.716, stop:0 rgba(120, 149, 203, 255), stop:1 rgba(135, 170, 203, 255));")
        self.frame_username.setFrameShape(QFrame.WinPanel)
        self.frame_username.setFrameShadow(QFrame.Raised)
        self.frame_username.setLineWidth(1)
        self.frame_username.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 330, 74))
        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 301, 61))
        font = QFont()
        font.setFamilies([u"Terminal"])
        font.setPointSize(14)
        font.setBold(True)
        self.label_2.setFont(font)
        self.frame_username.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.frame_username)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_photo = QFrame(self.frame_head)
        self.frame_photo.setObjectName(u"frame_photo")
        self.frame_photo.setMinimumSize(QSize(80, 80))
        self.frame_photo.setMaximumSize(QSize(80, 80))
        self.frame_photo.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.00555556, y1:0.188, x2:1, y2:0.716, stop:0 rgba(120, 149, 203, 255), stop:1 rgba(135, 170, 203, 255));")
        self.frame_photo.setFrameShape(QFrame.WinPanel)
        self.frame_photo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_photo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_photo)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 60))
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_photo)


        self.verticalLayout.addWidget(self.frame_head)

        self.frame_body = QFrame(self.centralwidget)
        self.frame_body.setObjectName(u"frame_body")
        self.frame_body.setFrameShape(QFrame.WinPanel)
        self.frame_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_body)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.l_widget = QListWidget(self.frame_body)
        self.l_widget.setObjectName(u"l_widget")
        self.l_widget.setFrameShape(QFrame.NoFrame)
        self.l_widget.setSelectionMode(QAbstractItemView.NoSelection)
        self.l_widget.setItemAlignment(Qt.AlignCenter|Qt.AlignHCenter|Qt.AlignTop|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.l_widget)


        self.verticalLayout.addWidget(self.frame_body)

        self.frame_foot = QFrame(self.centralwidget)
        self.frame_foot.setObjectName(u"frame_foot")
        self.frame_foot.setMinimumSize(QSize(0, 50))
        self.frame_foot.setMaximumSize(QSize(16777215, 50))
        self.frame_foot.setFrameShape(QFrame.WinPanel)
        self.frame_foot.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_foot)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bt_add = QPushButton(self.frame_foot)
        self.bt_add.setObjectName(u"bt_add")
        self.bt_add.setMinimumSize(QSize(80, 30))
        self.bt_add.setMaximumSize(QSize(30, 30))
        font1 = QFont()
        font1.setFamilies([u"Terminal"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.bt_add.setFont(font1)
        self.bt_add.setStyleSheet(u"background-color: rgb(120, 149, 203);\n"
"border-radius: 14px;\n"
"border: 2px solid black;")
        self.bt_add.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.bt_add)


        self.verticalLayout.addWidget(self.frame_foot)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"USERNAME NAME", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.bt_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
    # retranslateUi

