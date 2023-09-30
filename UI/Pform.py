# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
    QProgressBar, QPushButton, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setStyleSheet(u"background-color: #C5DFF8;")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Fixedsys"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(120, 149, 203);")
        self.label.setFrameShape(QFrame.WinPanel)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 200))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(120, 149, 203);")
        self.stackedWidget.setFrameShape(QFrame.WinPanel)
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.progressBar = QProgressBar(self.page)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"background-color: rgb(120, 149, 203);")
        self.progressBar.setValue(24)

        self.verticalLayout_4.addWidget(self.progressBar)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Fixedsys"])
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout = QHBoxLayout(self.page_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.page_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(300, 100))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 255, 0);")

        self.horizontalLayout.addWidget(self.pushButton)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"WELCOME!", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Loading...", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Start", None))
    # retranslateUi

