# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_structure.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1064, 717)
        Form.setStyleSheet(u"background-color: transparent;")
        self.frame_main = QFrame(Form)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setGeometry(QRect(30, 30, 1000, 600))
        self.frame_main.setStyleSheet(u"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setGeometry(QRect(0, 0, 1000, 50))
        self.frame_top.setStyleSheet(u"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"background-color: rgb(222, 222, 222)")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.frame_top_border = QFrame(self.frame_top)
        self.frame_top_border.setObjectName(u"frame_top_border")
        self.frame_top_border.setGeometry(QRect(0, 40, 1000, 10))
        self.frame_top_border.setStyleSheet(u"border-bottom: 0.5px solid rgba(194, 194, 194, 200)")
        self.frame_top_border.setFrameShape(QFrame.StyledPanel)
        self.frame_top_border.setFrameShadow(QFrame.Raised)
        self.button_import = QPushButton(self.frame_top)
        self.button_import.setObjectName(u"button_import")
        self.button_import.setGeometry(QRect(8, 6, 36, 36))
        self.button_import.setStyleSheet(u"QPushButton{\n"
"border-radius: 18px;\n"
"background-color: rgb(40, 40, 40)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(80, 80, 80);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(20, 20, 20);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../UI icon/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_import.setIcon(icon)
        self.button_import.setIconSize(QSize(20, 20))
        self.button_close = QPushButton(self.frame_top)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(960, 13, 24, 24))
        self.button_close.setStyleSheet(u"QPushButton{\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(80, 80, 80, 20);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(20, 20, 20, 40);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../UI icon/close_40.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_close.setIcon(icon1)
        self.button_close.setIconSize(QSize(16, 16))
        self.frame_left = QFrame(self.frame_main)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setGeometry(QRect(0, 50, 50, 550))
        self.frame_left.setStyleSheet(u"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.frame_left_border = QFrame(self.frame_left)
        self.frame_left_border.setObjectName(u"frame_left_border")
        self.frame_left_border.setGeometry(QRect(40, 0, 10, 550))
        self.frame_left_border.setStyleSheet(u"border-right: 0.5px solid rgba(194, 194, 194, 200)")
        self.frame_left_border.setFrameShape(QFrame.StyledPanel)
        self.frame_left_border.setFrameShadow(QFrame.Raised)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_import.setText("")
        self.button_close.setText("")
    # retranslateUi

