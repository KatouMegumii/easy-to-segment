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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 600)
        Form.setStyleSheet(u"background-color: transparent;")
        self.frame_main = QFrame(Form)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setGeometry(QRect(0, 0, 1000, 600))
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
        icon.addFile(u"../UI icon/import-file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_import.setIcon(icon)
        self.button_import.setIconSize(QSize(20, 20))
        self.cbox_mode = QComboBox(self.frame_top)
        icon1 = QIcon()
        icon1.addFile(u"../UI icon/2d.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cbox_mode.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u"../UI icon/3d.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cbox_mode.addItem(icon2, "")
        self.cbox_mode.setObjectName(u"cbox_mode")
        self.cbox_mode.setGeometry(QRect(60, 10, 150, 30))
        font = QFont()
        font.setFamilies([u"Segoe UI Historic"])
        font.setPointSize(10)
        font.setBold(False)
        self.cbox_mode.setFont(font)
        self.cbox_mode.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.cbox_mode.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid rgb(120,120,120); \n"
"    border-radius: 6px;\n"
"    color: rgb(40,40,40);\n"
"    padding-left:5px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow { \n"
"width:16px; \n"
"height: 16px;\n"
"padding-right:10px;\n"
"image: url(D:/Python Coding/UI icon/down-arrow.svg); \n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background: transparent;\n"
"}\n"
"")
        self.cbox_mode.setIconSize(QSize(18, 18))
        self.frame_top_divide1 = QFrame(self.frame_top)
        self.frame_top_divide1.setObjectName(u"frame_top_divide1")
        self.frame_top_divide1.setGeometry(QRect(225, 7, 2, 36))
        self.frame_top_divide1.setStyleSheet(u"border-right: 1px solid rgba(194, 194, 194, 200)")
        self.frame_top_divide1.setFrameShape(QFrame.StyledPanel)
        self.frame_top_divide1.setFrameShadow(QFrame.Raised)
        self.button_new_class = QPushButton(self.frame_top)
        self.button_new_class.setObjectName(u"button_new_class")
        self.button_new_class.setGeometry(QRect(492, 10, 101, 30))
        self.button_new_class.setFont(font)
        self.button_new_class.setStyleSheet(u"QPushButton{\n"
"border-radius: 6px;\n"
"border: 1px solid rgb(120,120,120);\n"
"color: rgb(40,40,40);\n"
"padding-bottom:1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(80,80,80);\n"
"background-color: rgb(80, 80, 80);\n"
"color: rgb(255,255,255)\n"
"}\n"
"QPushButton:pressed{\n"
"border: 1px solid rgb(20,20,20);\n"
"background-color: rgb(20, 20, 20);\n"
"color: rgb(255,255,255)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../UI icon/square-add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_new_class.setIcon(icon3)
        self.button_new_class.setIconSize(QSize(18, 18))
        self.frame_top_divide3 = QFrame(self.frame_top)
        self.frame_top_divide3.setObjectName(u"frame_top_divide3")
        self.frame_top_divide3.setGeometry(QRect(470, 7, 2, 36))
        self.frame_top_divide3.setStyleSheet(u"border-right: 1px solid rgba(194, 194, 194, 200)")
        self.frame_top_divide3.setFrameShape(QFrame.StyledPanel)
        self.frame_top_divide3.setFrameShadow(QFrame.Raised)
        self.button_generate_mask = QPushButton(self.frame_top)
        self.button_generate_mask.setObjectName(u"button_generate_mask")
        self.button_generate_mask.setGeometry(QRect(610, 10, 161, 30))
        self.button_generate_mask.setFont(font)
        self.button_generate_mask.setStyleSheet(u"QPushButton{\n"
"border-radius: 6px;\n"
"border: 1px solid rgb(120,120,120);\n"
"color: rgb(40,40,40);\n"
"padding-bottom:1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(80,80,80);\n"
"background-color: rgb(80, 80, 80);\n"
"color: rgb(255,255,255)\n"
"}\n"
"QPushButton:pressed{\n"
"border: 1px solid rgb(20,20,20);\n"
"background-color: rgb(20, 20, 20);\n"
"color: rgb(255,255,255)\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../UI icon/generate-mask.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_generate_mask.setIcon(icon4)
        self.button_generate_mask.setIconSize(QSize(18, 18))
        self.button_save = QPushButton(self.frame_top)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(244, 10, 72, 30))
        self.button_save.setFont(font)
        self.button_save.setStyleSheet(u"QPushButton{\n"
"border-radius: 6px;\n"
"border: 1px solid rgb(120,120,120);\n"
"color: rgb(40,40,40);\n"
"padding-bottom:1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(80,80,80);\n"
"background-color: rgb(80, 80, 80);\n"
"color: rgb(255,255,255)\n"
"}\n"
"QPushButton:pressed{\n"
"border: 1px solid rgb(20,20,20);\n"
"background-color: rgb(20, 20, 20);\n"
"color: rgb(255,255,255)\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../UI icon/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_save.setIcon(icon5)
        self.button_save.setIconSize(QSize(18, 18))
        self.frame_top_divide2 = QFrame(self.frame_top)
        self.frame_top_divide2.setObjectName(u"frame_top_divide2")
        self.frame_top_divide2.setGeometry(QRect(332, 7, 2, 36))
        self.frame_top_divide2.setStyleSheet(u"border-right: 1px solid rgba(194, 194, 194, 200)")
        self.frame_top_divide2.setFrameShape(QFrame.StyledPanel)
        self.frame_top_divide2.setFrameShadow(QFrame.Raised)
        self.button_auto_mask = QPushButton(self.frame_top)
        self.button_auto_mask.setObjectName(u"button_auto_mask")
        self.button_auto_mask.setGeometry(QRect(352, 10, 101, 30))
        self.button_auto_mask.setFont(font)
        self.button_auto_mask.setStyleSheet(u"QPushButton{\n"
"border-radius: 6px;\n"
"border: 1px solid rgb(120,120,120);\n"
"color: rgb(40,40,40);\n"
"padding-bottom:1px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(80,80,80);\n"
"background-color: rgb(80, 80, 80);\n"
"color: rgb(255,255,255)\n"
"}\n"
"QPushButton:pressed{\n"
"border: 1px solid rgb(20,20,20);\n"
"background-color: rgb(20, 20, 20);\n"
"color: rgb(255,255,255)\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../UI icon/magic.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_auto_mask.setIcon(icon6)
        self.button_auto_mask.setIconSize(QSize(18, 18))
        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setGeometry(QRect(919, 0, 71, 50))
        self.frame_top_right.setFrameShape(QFrame.StyledPanel)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_top_right)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_minimize = QPushButton(self.frame_top_right)
        self.button_minimize.setObjectName(u"button_minimize")
        self.button_minimize.setStyleSheet(u"QPushButton{\n"
"border-radius: 0px;\n"
"min-width:30px;\n"
"max-width:30px;\n"
"min-height:30px;\n"
"max-height:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(80, 80, 80, 50);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(20, 20, 20, 100);\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"../UI icon/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_minimize.setIcon(icon7)
        self.button_minimize.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.button_minimize)

        self.button_close = QPushButton(self.frame_top_right)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setStyleSheet(u"QPushButton{\n"
"border-radius: 0px;\n"
"min-width:30px;\n"
"max-width:30px;\n"
"min-height:30px;\n"
"max-height:30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(80, 80, 80, 50);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(20, 20, 20, 100);\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"../UI icon/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_close.setIcon(icon8)
        self.button_close.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.button_close)

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
        self.cbox_mode.setItemText(0, QCoreApplication.translate("Form", u"2D Segement", None))
        self.cbox_mode.setItemText(1, QCoreApplication.translate("Form", u"3D Segement", None))

        self.button_new_class.setText(QCoreApplication.translate("Form", u"New Class", None))
        self.button_generate_mask.setText(QCoreApplication.translate("Form", u"Generate Select Mask", None))
        self.button_save.setText(QCoreApplication.translate("Form", u"Save", None))
        self.button_auto_mask.setText(QCoreApplication.translate("Form", u"Auto Mask", None))
        self.button_minimize.setText("")
        self.button_close.setText("")
    # retranslateUi

