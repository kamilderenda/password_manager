# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_fill_info.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 400)
        Form.setMinimumSize(QSize(300, 400))
        Form.setMaximumSize(QSize(300, 400))
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.272, y1:0, x2:1, y2:0.591, stop:0 rgba(197, 223, 248, 255), stop:1 rgba(160, 191, 224, 255));")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"background-color: #4A55A2;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.153, x2:1, y2:0.688, stop:0 rgba(74, 85, 162, 255), stop:1 rgba(76, 122, 162, 255));")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Fixedsys"])
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.272, y1:0, x2:1, y2:0.591, stop:0 rgba(197, 223, 248, 255), stop:1 rgba(160, 191, 224, 255));")
        self.frame_2.setFrameShape(QFrame.WinPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.17, x2:1, y2:0.75, stop:0 rgba(120, 149, 203, 255), stop:1 rgba(131, 172, 203, 255));")
        self.label_2.setFrameShape(QFrame.WinPanel)
        self.label_2.setFrameShadow(QFrame.Raised)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.le_user = QLineEdit(self.frame_2)
        self.le_user.setObjectName(u"le_user")
        self.le_user.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.le_user)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: #7895CB;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.17, x2:1, y2:0.75, stop:0 rgba(120, 149, 203, 255), stop:1 rgba(131, 172, 203, 255));")
        self.label_3.setFrameShape(QFrame.WinPanel)
        self.label_3.setFrameShadow(QFrame.Raised)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.le_password = QLineEdit(self.frame_2)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.le_password)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: #7895CB;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.17, x2:1, y2:0.75, stop:0 rgba(120, 149, 203, 255), stop:1 rgba(131, 172, 203, 255));")
        self.label_4.setFrameShape(QFrame.WinPanel)
        self.label_4.setFrameShadow(QFrame.Raised)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.le_site = QLineEdit(self.frame_2)
        self.le_site.setObjectName(u"le_site")
        self.le_site.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.le_site)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setStyleSheet(u"background-color: #4A55A2;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.153, x2:1, y2:0.688, stop:0 rgba(74, 85, 162, 255), stop:1 rgba(76, 122, 162, 255));")
        self.frame_3.setFrameShape(QFrame.WinPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_save = QPushButton(self.frame_3)
        self.bt_save.setObjectName(u"bt_save")
        self.bt_save.setFont(font)
        self.bt_save.setStyleSheet(u"background-color: #4A55A2;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.17, x2:1, y2:0.75, stop:0 rgba(120, 149, 203, 255), stop:1 rgba(131, 172, 203, 255));")

        self.horizontalLayout.addWidget(self.bt_save)

        self.bt_cancel = QPushButton(self.frame_3)
        self.bt_cancel.setObjectName(u"bt_cancel")
        self.bt_cancel.setFont(font)
        self.bt_cancel.setStyleSheet(u"background-color: #4A55A2;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.17, x2:1, y2:0.75, stop:0 rgba(120, 149, 203, 255), stop:1 rgba(131, 172, 203, 255));")

        self.horizontalLayout.addWidget(self.bt_cancel)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"FILL THE DATA", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"USERNAME/EMAIL", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"PASSWORD", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"SITE NAME", None))
        self.bt_save.setText(QCoreApplication.translate("Form", u"SAVE", None))
        self.bt_cancel.setText(QCoreApplication.translate("Form", u"CANCEL", None))
    # retranslateUi

