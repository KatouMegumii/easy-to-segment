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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QLabel, QPushButton, QSizePolicy, QToolButton,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 600)
        Form.setStyleSheet(u"background-color: transparent;")
        self.frame_main = QFrame(Form)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setGeometry(QRect(0, 0, 1000, 600))
        self.frame_main.setToolTipDuration(1)
        self.frame_main.setStyleSheet(u"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:5px;\n"
"background-color: rgb(240, 240, 240);")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.frame_top_bar = QFrame(self.frame_main)
        self.frame_top_bar.setObjectName(u"frame_top_bar")
        self.frame_top_bar.setGeometry(QRect(-1, 0, 1000, 40))
        self.frame_top_bar.setStyleSheet(u"QFrame#frame_top_bar{\n"
"border-top-left-radius:5px;\n"
"border-top-right-radius:5px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"background-color: rgb(200, 200, 200);\n"
"border-bottom: 1px solid rgba(180, 180, 180, 200);\n"
"}")
        self.frame_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_top_bar.setFrameShadow(QFrame.Raised)
        self.frame_top_border = QFrame(self.frame_top_bar)
        self.frame_top_border.setObjectName(u"frame_top_border")
        self.frame_top_border.setGeometry(QRect(0, 40, 1000, 10))
        self.frame_top_border.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 1px solid rgba(180, 180, 180, 200)")
        self.frame_top_border.setFrameShape(QFrame.StyledPanel)
        self.frame_top_border.setFrameShadow(QFrame.Raised)
        self.cbox_mode = QComboBox(self.frame_top_bar)
        self.cbox_mode.addItem("")
        self.cbox_mode.addItem("")
        self.cbox_mode.setObjectName(u"cbox_mode")
        self.cbox_mode.setGeometry(QRect(50, 5, 100, 30))
        font = QFont()
        font.setFamilies([u"SF Pro Display"])
        font.setPointSize(10)
        font.setBold(False)
        self.cbox_mode.setFont(font)
        self.cbox_mode.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.cbox_mode.setStyleSheet(u"QComboBox {\n"
"    border-radius: 0px;\n"
"    color: rgb(40,40,40);\n"
"    padding-left:5px;\n"
"    padding-bottom:1px;\n"
"    background:transparent;\n"
"}\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border:transparent;\n"
"    outline: 0px;\n"
"    border-radius:0px;\n"
"	color: rgb(40,40,40);\n"
"    background-color: rgb();\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item{\n"
"    border:transparent;\n"
"    color: rgb(40,40,40);\n"
"    height:30px;\n"
"    padding-left:2px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:selected{\n"
"    border:transparent;\n"
"    color: rgb(40,40,40);\n"
"    background-color: rgba(80, 80, 80, 50);\n"
"}\n"
"\n"
"QComboBox::down-arrow { \n"
"width:12px; \n"
"height: 12px;\n"
"image: url(D:/Python Coding/easy-to-segment/UI icon/down-arrow.svg); \n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background: transparent;\n"
"}\n"
"")
        self.cbox_mode.setIconSize(QSize(16, 16))
        self.button_minimize = QPushButton(self.frame_top_bar)
        self.button_minimize.setObjectName(u"button_minimize")
        self.button_minimize.setGeometry(QRect(935, 5, 30, 30))
        self.button_minimize.setStyleSheet(u"QPushButton{\n"
"border-radius: 0px;\n"
"min-width:30px;\n"
"max-width:30px;\n"
"min-height:30px;\n"
"max-height:30px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(80, 80, 80, 50);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(20, 20, 20, 100);\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"UI icon/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_minimize.setIcon(icon1)
        self.button_minimize.setIconSize(QSize(18, 18))
        self.button_close = QPushButton(self.frame_top_bar)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(965, 5, 30, 30))
        self.button_close.setStyleSheet(u"QPushButton{\n"
"border-radius: 0px;\n"
"min-width:30px;\n"
"max-width:30px;\n"
"min-height:30px;\n"
"max-height:30px;\n"
"background:transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(80, 80, 80, 50);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgba(20, 20, 20, 100);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"UI icon/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_close.setIcon(icon2)
        self.button_close.setIconSize(QSize(18, 18))
        self.icon = QLabel(self.frame_top_bar)
        self.icon.setObjectName(u"icon")
        self.icon.setGeometry(QRect(12, 6, 28, 28))
        self.icon.setStyleSheet(u"image: url(D:/Python Coding/easy-to-segment/UI icon/logo.png);\n"
"boarder-radius:4px;\n"
"background:transparent;")
        self.icon.raise_()
        self.cbox_mode.raise_()
        self.frame_top_border.raise_()
        self.button_minimize.raise_()
        self.button_close.raise_()
        self.frame_function_bar = QFrame(self.frame_main)
        self.frame_function_bar.setObjectName(u"frame_function_bar")
        self.frame_function_bar.setGeometry(QRect(0, 40, 50, 560))
        self.frame_function_bar.setStyleSheet(u"QFrame#frame_function_bar{\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-left-radius:5px;\n"
"border-bottom-right-radius:0px;\n"
"border-right: 1px solid rgba(180, 180, 180, 200)\n"
"}")
        self.frame_function_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_function_bar.setFrameShadow(QFrame.Raised)
        self.frame_settings = QFrame(self.frame_function_bar)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setGeometry(QRect(0, 0, 50, 140))
        self.frame_settings.setStyleSheet(u"\n"
"background: transparent;\n"
"")
        self.frame_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_settings.setFrameShadow(QFrame.Raised)
        self.button_settings = QPushButton(self.frame_settings)
        self.button_settings.setObjectName(u"button_settings")
        self.button_settings.setGeometry(QRect(7, 94, 36, 36))
        self.button_settings.setToolTipDuration(0)
        self.button_settings.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:36px;\n"
"max-width:36px;\n"
"min-height:36px;\n"
"max-height:36px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color: rgb(40,40,40);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/settings-white.svg);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"UI icon/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_settings.setIcon(icon3)
        self.button_settings.setIconSize(QSize(24, 24))
        self.button_save = QPushButton(self.frame_settings)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(7, 52, 36, 36))
        self.button_save.setFont(font)
        self.button_save.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:36px;\n"
"max-width:36px;\n"
"min-height:36px;\n"
"max-height:36px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color:  rgb(40,40,40);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/save-white.svg);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"UI icon/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_save.setIcon(icon4)
        self.button_save.setIconSize(QSize(26, 26))
        self.button_import = QPushButton(self.frame_settings)
        self.button_import.setObjectName(u"button_import")
        self.button_import.setGeometry(QRect(7, 10, 36, 36))
        self.button_import.setToolTipDuration(0)
        self.button_import.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:36px;\n"
"max-width:36px;\n"
"min-height:36px;\n"
"max-height:36px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color: rgb(40,40,40);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/import-white.svg);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"UI icon/import.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_import.setIcon(icon5)
        self.button_import.setIconSize(QSize(26, 26))
        self.frame_settings_bottom = QFrame(self.frame_settings)
        self.frame_settings_bottom.setObjectName(u"frame_settings_bottom")
        self.frame_settings_bottom.setGeometry(QRect(10, 135, 30, 5))
        self.frame_settings_bottom.setStyleSheet(u"border-radius:0px;\n"
"border-bottom: 1px solid rgba(180, 180, 180, 200);")
        self.frame_settings_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_settings_bottom.setFrameShadow(QFrame.Raised)
        self.frame_mode = QFrame(self.frame_function_bar)
        self.frame_mode.setObjectName(u"frame_mode")
        self.frame_mode.setGeometry(QRect(0, 140, 50, 140))
        self.frame_mode.setStyleSheet(u"background: transparent;")
        self.frame_mode.setFrameShape(QFrame.StyledPanel)
        self.frame_mode.setFrameShadow(QFrame.Raised)
        self.button_box_mode = QToolButton(self.frame_mode)
        self.mode_button_group = QButtonGroup(Form)
        self.mode_button_group.setObjectName(u"mode_button_group")
        self.mode_button_group.addButton(self.button_box_mode)
        self.button_box_mode.setObjectName(u"button_box_mode")
        self.button_box_mode.setGeometry(QRect(7, 94, 36, 36))
        self.button_box_mode.setStyleSheet(u"QToolButton{\n"
"border-radius: 5px;\n"
"min-width:36px;\n"
"max-width:36px;\n"
"min-height:36px;\n"
"max-height:36px;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: none;\n"
"background-color: rgb(40,40,40);\n"
"padding-left: 0px;\n"
"padding-right:0px;\n"
"padding-bottom:0px;\n"
"padding-top:0px;\n"
"}\n"
"\n"
"QToolButton:checked{\n"
"border: none;\n"
"background-color: rgb(40,40,40);\n"
"padding-left: 0px;\n"
"padding-right:0px;\n"
"padding-bottom:0px;\n"
"padding-top:0px;\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"UI icon/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_box_mode.setIcon(icon6)
        self.button_box_mode.setIconSize(QSize(26, 26))
        self.button_box_mode.setCheckable(True)
        self.button_view_mode = QToolButton(self.frame_mode)
        self.mode_button_group.addButton(self.button_view_mode)
        self.button_view_mode.setObjectName(u"button_view_mode")
        self.button_view_mode.setGeometry(QRect(7, 10, 36, 36))
        self.button_view_mode.setStyleSheet(u"QToolButton{\n"
"border-radius: 5px;\n"
"min-width:36px;\n"
"max-width:36px;\n"
"min-height:36px;\n"
"max-height:36px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: none;\n"
"background-color: rgb(40,40,40);\n"
"padding-left: 0px;\n"
"padding-right:0px;\n"
"padding-bottom:0px;\n"
"padding-top:0px;\n"
"}\n"
"\n"
"QToolButton:checked{\n"
"border: none;\n"
"background-color: rgb(40,40,40);\n"
"padding-left: 0px;\n"
"padding-right:0px;\n"
"padding-bottom:0px;\n"
"padding-top:0px;\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"UI icon/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_view_mode.setIcon(icon7)
        self.button_view_mode.setIconSize(QSize(26, 26))
        self.button_view_mode.setCheckable(True)
        self.button_view_mode.setChecked(True)
        self.button_point_mode = QToolButton(self.frame_mode)
        self.mode_button_group.addButton(self.button_point_mode)
        self.button_point_mode.setObjectName(u"button_point_mode")
        self.button_point_mode.setGeometry(QRect(7, 52, 36, 36))
        self.button_point_mode.setStyleSheet(u"QToolButton{\n"
"border-radius: 5px;\n"
"min-width:36px;\n"
"max-width:36px;\n"
"min-height:36px;\n"
"max-height:36px;\n"
"}\n"
"\n"
"\n"
"QToolButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: none;\n"
"background-color:  rgb(40,40,40);\n"
"padding-left: 0px;\n"
"padding-right:0px;\n"
"padding-bottom:0px;\n"
"padding-top:0px;\n"
"}\n"
"\n"
"QToolButton:checked{\n"
"border: none;\n"
"background-color: rgb(40,40,40);\n"
"padding-left: 0px;\n"
"padding-right:0px;\n"
"padding-bottom:0px;\n"
"padding-top:0px;\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"UI icon/point.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_point_mode.setIcon(icon8)
        self.button_point_mode.setIconSize(QSize(24, 24))
        self.button_point_mode.setCheckable(True)
        self.frame_mode_bottom = QFrame(self.frame_mode)
        self.frame_mode_bottom.setObjectName(u"frame_mode_bottom")
        self.frame_mode_bottom.setGeometry(QRect(10, 135, 30, 5))
        self.frame_mode_bottom.setStyleSheet(u"border-radius:0px;\n"
"border-bottom: 1px solid rgba(180, 180, 180, 200);")
        self.frame_mode_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_mode_bottom.setFrameShadow(QFrame.Raised)
        self.frame_function = QFrame(self.frame_function_bar)
        self.frame_function.setObjectName(u"frame_function")
        self.frame_function.setGeometry(QRect(0, 280, 50, 140))
        self.frame_function.setStyleSheet(u"background: transparent;")
        self.frame_function.setFrameShape(QFrame.StyledPanel)
        self.frame_function.setFrameShadow(QFrame.Raised)
        self.button_add_group = QPushButton(self.frame_function)
        self.button_add_group.setObjectName(u"button_add_group")
        self.button_add_group.setGeometry(QRect(7, 10, 36, 36))
        self.button_add_group.setToolTipDuration(0)
        self.button_add_group.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:36px;\n"
"max-width:36px;\n"
"min-height:36px;\n"
"max-height:36px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color:  rgb(40,40,40);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/square-add-white.svg);\n"
"}\n"
"")
        icon9 = QIcon()
        icon9.addFile(u"UI icon/square-add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_add_group.setIcon(icon9)
        self.button_add_group.setIconSize(QSize(24, 24))
        self.button_generate_mask = QPushButton(self.frame_function)
        self.button_generate_mask.setObjectName(u"button_generate_mask")
        self.button_generate_mask.setGeometry(QRect(7, 52, 36, 36))
        self.button_generate_mask.setFont(font)
        self.button_generate_mask.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:36px;\n"
"max-width:36px;\n"
"min-height:36px;\n"
"max-height:36px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color:  rgb(40,40,40);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/generate-mask-white.svg);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"UI icon/generate-mask.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_generate_mask.setIcon(icon10)
        self.button_generate_mask.setIconSize(QSize(24, 24))
        self.button_auto_mask = QPushButton(self.frame_function)
        self.button_auto_mask.setObjectName(u"button_auto_mask")
        self.button_auto_mask.setGeometry(QRect(7, 94, 36, 36))
        self.button_auto_mask.setFont(font)
        self.button_auto_mask.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:36px;\n"
"max-width:36px;\n"
"min-height:36px;\n"
"max-height:36px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color:  rgb(40,40,40);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/magic-white.svg);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"UI icon/magic.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_auto_mask.setIcon(icon11)
        self.button_auto_mask.setIconSize(QSize(24, 24))
        self.frame_function_bottom = QFrame(self.frame_function)
        self.frame_function_bottom.setObjectName(u"frame_function_bottom")
        self.frame_function_bottom.setGeometry(QRect(10, 135, 30, 5))
        self.frame_function_bottom.setStyleSheet(u"border-radius:0px;\n"
"border-bottom: 1px solid rgba(180, 180, 180, 200);")
        self.frame_function_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_function_bottom.setFrameShadow(QFrame.Raised)
        self.frame_operation = QFrame(self.frame_function_bar)
        self.frame_operation.setObjectName(u"frame_operation")
        self.frame_operation.setGeometry(QRect(0, 420, 50, 140))
        self.frame_operation.setStyleSheet(u"background: transparent;")
        self.frame_operation.setFrameShape(QFrame.StyledPanel)
        self.frame_operation.setFrameShadow(QFrame.Raised)
        self.button_undo = QPushButton(self.frame_operation)
        self.button_undo.setObjectName(u"button_undo")
        self.button_undo.setGeometry(QRect(7, 10, 36, 36))
        self.button_undo.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:36px;\n"
"max-width:36px;\n"
"min-height:36px;\n"
"max-height:36px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color:  rgb(40,40,40);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/undo-white.svg);\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"UI icon/undo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_undo.setIcon(icon12)
        self.button_undo.setIconSize(QSize(24, 24))
        self.button_redo = QPushButton(self.frame_operation)
        self.button_redo.setObjectName(u"button_redo")
        self.button_redo.setGeometry(QRect(7, 52, 36, 36))
        self.button_redo.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:36px;\n"
"max-width:36px;\n"
"min-height:36px;\n"
"max-height:36px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color:  rgb(40,40,40);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/redo-white.svg);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"UI icon/redo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_redo.setIcon(icon13)
        self.button_redo.setIconSize(QSize(24, 24))
        self.button_reset = QPushButton(self.frame_operation)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setGeometry(QRect(7, 94, 36, 36))
        self.button_reset.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:36px;\n"
"max-width:36px;\n"
"min-height:36px;\n"
"max-height:36px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color:  rgb(40,40,40);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/reset-white.svg);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"UI icon/reset.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_reset.setIcon(icon14)
        self.button_reset.setIconSize(QSize(24, 24))
        self.frame_mask_list = QFrame(self.frame_main)
        self.frame_mask_list.setObjectName(u"frame_mask_list")
        self.frame_mask_list.setGeometry(QRect(800, 40, 200, 560))
        self.frame_mask_list.setStyleSheet(u"QFrame{\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:5px;\n"
"border-left: 1px solid rgba(180, 180, 180, 200);\n"
"}")
        self.frame_mask_list.setFrameShape(QFrame.StyledPanel)
        self.frame_mask_list.setFrameShadow(QFrame.Raised)
        self.frame_display = QFrame(self.frame_main)
        self.frame_display.setObjectName(u"frame_display")
        self.frame_display.setGeometry(QRect(50, 550, 750, 50))
        self.frame_display.setStyleSheet(u"QFrame{\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top: 1px solid rgba(180, 180, 180, 200);\n"
"}")
        self.frame_display.setFrameShape(QFrame.StyledPanel)
        self.frame_display.setFrameShadow(QFrame.Raised)
        self.frame_mask_list.raise_()
        self.frame_display.raise_()
        self.frame_function_bar.raise_()
        self.frame_top_bar.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Easy To Segement", None))
        self.cbox_mode.setItemText(0, QCoreApplication.translate("Form", u"Segment 2D", None))
        self.cbox_mode.setItemText(1, QCoreApplication.translate("Form", u"Segment 3D", None))

        self.button_minimize.setText("")
        self.button_close.setText("")
        self.icon.setText("")
        self.button_settings.setText("")
        self.button_save.setText("")
        self.button_import.setText("")
        self.button_box_mode.setText(QCoreApplication.translate("Form", u"...", None))
        self.button_view_mode.setText("")
        self.button_point_mode.setText(QCoreApplication.translate("Form", u"...", None))
        self.button_add_group.setText("")
        self.button_generate_mask.setText("")
        self.button_auto_mask.setText("")
        self.button_undo.setText("")
        self.button_redo.setText("")
        self.button_reset.setText("")
    # retranslateUi

