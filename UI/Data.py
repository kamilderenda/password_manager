# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(867, 72)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(11111, 80))
        Form.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 80))
        self.frame_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.165, x2:1, y2:0.75, stop:0 rgba(120, 149, 203, 255), stop:1 rgba(128, 174, 203, 255));")
        self.frame_4.setFrameShape(QFrame.WinPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(1)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(200, 16777215))
        self.frame_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.239, x2:1, y2:0.727273, stop:0 rgba(197, 223, 248, 255), stop:1 rgba(160, 191, 224, 255));")
        self.frame_5.setFrameShape(QFrame.WinPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_site = QLabel(self.frame_5)
        self.label_site.setObjectName(u"label_site")
        self.label_site.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setFamilies([u"Fixedsys"])
        font.setPointSize(11)
        font.setBold(True)
        self.label_site.setFont(font)

        self.verticalLayout.addWidget(self.label_site)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(400, 50))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.239, x2:1, y2:0.727273, stop:0 rgba(197, 223, 248, 255), stop:1 rgba(160, 191, 224, 255));")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_mail = QLabel(self.frame)
        self.label_mail.setObjectName(u"label_mail")
        self.label_mail.setMinimumSize(QSize(230, 0))
        self.label_mail.setMaximumSize(QSize(350, 16777215))
        self.label_mail.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_mail)


        self.horizontalLayout_5.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(400, 50))
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.239, x2:1, y2:0.727273, stop:0 rgba(197, 223, 248, 255), stop:1 rgba(160, 191, 224, 255));")
        self.frame_2.setFrameShape(QFrame.WinPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_password = QLabel(self.frame_2)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setMinimumSize(QSize(160, 0))
        self.label_password.setMaximumSize(QSize(350, 16777215))
        self.label_password.setFont(font)
        self.label_password.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_4.addWidget(self.label_password)


        self.horizontalLayout_5.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(150, 50))
        self.frame_3.setMaximumSize(QSize(150, 50))
        self.frame_3.setFrameShape(QFrame.WinPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bt_change = QPushButton(self.frame_3)
        self.bt_change.setObjectName(u"bt_change")
        self.bt_change.setMinimumSize(QSize(30, 30))
        self.bt_change.setMaximumSize(QSize(30, 30))
        self.bt_change.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.239, x2:1, y2:0.727273, stop:0 rgba(197, 223, 248, 255), stop:1 rgba(160, 191, 224, 255));")
        icon = QIcon()
        icon.addFile(u"../UI/images/pen.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_change.setIcon(icon)
        self.bt_change.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.bt_change)

        self.bt_del = QPushButton(self.frame_3)
        self.bt_del.setObjectName(u"bt_del")
        self.bt_del.setMinimumSize(QSize(30, 30))
        self.bt_del.setMaximumSize(QSize(30, 30))
        self.bt_del.setFont(font)
        self.bt_del.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.239, x2:1, y2:0.727273, stop:0 rgba(197, 223, 248, 255), stop:1 rgba(160, 191, 224, 255));")
        icon1 = QIcon()
        icon1.addFile(u"../UI/images/bin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_del.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.bt_del)

        self.bt_hide = QPushButton(self.frame_3)
        self.bt_hide.setObjectName(u"bt_hide")
        self.bt_hide.setMinimumSize(QSize(30, 30))
        self.bt_hide.setMaximumSize(QSize(30, 30))
        self.bt_hide.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.239, x2:1, y2:0.727273, stop:0 rgba(197, 223, 248, 255), stop:1 rgba(160, 191, 224, 255));")
        icon2 = QIcon()
        icon2.addFile(u"../UI/images/eye.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_hide.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.bt_hide)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_site.setText(QCoreApplication.translate("Form", u"---EMPTY---", None))
        self.label_mail.setText(QCoreApplication.translate("Form", u"---EMPTY---", None))
        self.label_password.setText(QCoreApplication.translate("Form", u"---EMPTY---", None))
        self.bt_change.setText("")
        self.bt_del.setText("")
        self.bt_hide.setText("")
    # retranslateUi

