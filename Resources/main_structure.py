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
    QGraphicsView, QHBoxLayout, QPushButton, QSizePolicy,
    QToolButton, QWidget)

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
        self.frame_main.setStyleSheet(u"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"background-color: rgb(240, 240, 240);")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.frame_top_bar = QFrame(self.frame_main)
        self.frame_top_bar.setObjectName(u"frame_top_bar")
        self.frame_top_bar.setGeometry(QRect(0, 0, 1000, 50))
        self.frame_top_bar.setStyleSheet(u"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"background-color: rgb(160, 160, 160)")
        self.frame_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_top_bar.setFrameShadow(QFrame.Raised)
        self.frame_top_border = QFrame(self.frame_top_bar)
        self.frame_top_border.setObjectName(u"frame_top_border")
        self.frame_top_border.setGeometry(QRect(0, 40, 1000, 10))
        self.frame_top_border.setStyleSheet(u"")
        self.frame_top_border.setFrameShape(QFrame.StyledPanel)
        self.frame_top_border.setFrameShadow(QFrame.Raised)
        self.button_import = QPushButton(self.frame_top_bar)
        self.button_import.setObjectName(u"button_import")
        self.button_import.setGeometry(QRect(5, 5, 40, 40))
        self.button_import.setStyleSheet(u"QPushButton{\n"
"border-radius: 20px;\n"
"min-width:40px;\n"
"max-width:40px;\n"
"min-height:40px;\n"
"max-height:40px;\n"
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
        icon.addFile(u"UI icon/import-file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_import.setIcon(icon)
        self.button_import.setIconSize(QSize(24, 24))
        self.cbox_mode = QComboBox(self.frame_top_bar)
        icon1 = QIcon()
        icon1.addFile(u"UI icon/2d.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cbox_mode.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u"UI icon/3d.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cbox_mode.addItem(icon2, "")
        self.cbox_mode.setObjectName(u"cbox_mode")
        self.cbox_mode.setGeometry(QRect(55, 10, 85, 30))
        font = QFont()
        font.setFamilies([u"SF Pro Display"])
        font.setPointSize(12)
        font.setBold(False)
        self.cbox_mode.setFont(font)
        self.cbox_mode.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.cbox_mode.setStyleSheet(u"QComboBox {\n"
"    border: 2px solid rgb(120,120,120); \n"
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
"image: url(D:/Python Coding/easy-to-segment/UI icon/down-arrow.svg); \n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background: transparent;\n"
"}\n"
"")
        self.cbox_mode.setIconSize(QSize(20, 20))
        self.frame_top_right = QFrame(self.frame_top_bar)
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
        icon3 = QIcon()
        icon3.addFile(u"UI icon/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_minimize.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u"UI icon/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_close.setIcon(icon4)
        self.button_close.setIconSize(QSize(18, 18))

        self.horizontalLayout.addWidget(self.button_close)

        self.frame_top_border.raise_()
        self.button_import.raise_()
        self.frame_top_right.raise_()
        self.cbox_mode.raise_()
        self.frame_function_bar = QFrame(self.frame_main)
        self.frame_function_bar.setObjectName(u"frame_function_bar")
        self.frame_function_bar.setGeometry(QRect(0, 50, 50, 550))
        self.frame_function_bar.setStyleSheet(u"border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;")
        self.frame_function_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_function_bar.setFrameShadow(QFrame.Raised)
        self.frame_function_bar_border = QFrame(self.frame_function_bar)
        self.frame_function_bar_border.setObjectName(u"frame_function_bar_border")
        self.frame_function_bar_border.setGeometry(QRect(40, 0, 10, 550))
        self.frame_function_bar_border.setStyleSheet(u"border-right: 0.5px solid rgba(180, 180, 180, 200)")
        self.frame_function_bar_border.setFrameShape(QFrame.StyledPanel)
        self.frame_function_bar_border.setFrameShadow(QFrame.Raised)
        self.frame_operation = QFrame(self.frame_function_bar)
        self.frame_operation.setObjectName(u"frame_operation")
        self.frame_operation.setGeometry(QRect(0, 400, 50, 150))
        self.frame_operation.setStyleSheet(u"background: transparent;")
        self.frame_operation.setFrameShape(QFrame.StyledPanel)
        self.frame_operation.setFrameShadow(QFrame.Raised)
        self.button_undo = QPushButton(self.frame_operation)
        self.button_undo.setObjectName(u"button_undo")
        self.button_undo.setGeometry(QRect(5, 10, 40, 40))
        self.button_undo.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:40px;\n"
"max-width:40px;\n"
"min-height:40px;\n"
"max-height:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color: rgba(40,40,40,220);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/undo-white.svg);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"UI icon/undo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_undo.setIcon(icon5)
        self.button_undo.setIconSize(QSize(24, 24))
        self.button_redo = QPushButton(self.frame_operation)
        self.button_redo.setObjectName(u"button_redo")
        self.button_redo.setGeometry(QRect(5, 55, 40, 40))
        self.button_redo.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:40px;\n"
"max-width:40px;\n"
"min-height:40px;\n"
"max-height:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color: rgba(40,40,40,220);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/redo-white.svg);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"UI icon/redo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_redo.setIcon(icon6)
        self.button_redo.setIconSize(QSize(24, 24))
        self.button_reset = QPushButton(self.frame_operation)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setGeometry(QRect(5, 100, 40, 40))
        self.button_reset.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:40px;\n"
"max-width:40px;\n"
"min-height:40px;\n"
"max-height:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color: rgba(40,40,40,220);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/reset-white.svg);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"UI icon/reset.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_reset.setIcon(icon7)
        self.button_reset.setIconSize(QSize(24, 24))
        self.frame_settings = QFrame(self.frame_function_bar)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setGeometry(QRect(0, 0, 50, 100))
        self.frame_settings.setStyleSheet(u"background: transparent;")
        self.frame_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_settings.setFrameShadow(QFrame.Raised)
        self.button_settings = QPushButton(self.frame_settings)
        self.button_settings.setObjectName(u"button_settings")
        self.button_settings.setGeometry(QRect(5, 5, 40, 40))
        self.button_settings.setToolTipDuration(0)
        self.button_settings.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:40px;\n"
"max-width:40px;\n"
"min-height:40px;\n"
"max-height:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color: rgba(40,40,40,220);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/settings-white.svg);\n"
"}\n"
"")
        icon8 = QIcon()
        icon8.addFile(u"UI icon/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_settings.setIcon(icon8)
        self.button_settings.setIconSize(QSize(24, 24))
        self.frame_settings_border = QFrame(self.frame_settings)
        self.frame_settings_border.setObjectName(u"frame_settings_border")
        self.frame_settings_border.setGeometry(QRect(10, 95, 30, 5))
        self.frame_settings_border.setStyleSheet(u"border-bottom: 1px solid rgba(180, 180, 180, 200)")
        self.frame_settings_border.setFrameShape(QFrame.StyledPanel)
        self.frame_settings_border.setFrameShadow(QFrame.Raised)
        self.button_save = QPushButton(self.frame_settings)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(5, 50, 40, 40))
        font1 = QFont()
        font1.setFamilies([u"SF Pro Display"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.button_save.setFont(font1)
        self.button_save.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:40px;\n"
"max-width:40px;\n"
"min-height:40px;\n"
"max-height:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color: rgba(40,40,40,220);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/save-white.svg);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"UI icon/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_save.setIcon(icon9)
        self.button_save.setIconSize(QSize(24, 24))
        self.frame_mode = QFrame(self.frame_function_bar)
        self.frame_mode.setObjectName(u"frame_mode")
        self.frame_mode.setGeometry(QRect(0, 100, 50, 150))
        self.frame_mode.setStyleSheet(u"background: transparent;")
        self.frame_mode.setFrameShape(QFrame.StyledPanel)
        self.frame_mode.setFrameShadow(QFrame.Raised)
        self.button_box_mode = QToolButton(self.frame_mode)
        self.mode_button_group = QButtonGroup(Form)
        self.mode_button_group.setObjectName(u"mode_button_group")
        self.mode_button_group.addButton(self.button_box_mode)
        self.button_box_mode.setObjectName(u"button_box_mode")
        self.button_box_mode.setGeometry(QRect(5, 100, 40, 40))
        self.button_box_mode.setStyleSheet(u"QToolButton{\n"
"border-radius: 5px;\n"
"min-width:40px;\n"
"max-width:40px;\n"
"min-height:40px;\n"
"max-height:40px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: none;\n"
"background-color: rgba(40,40,40,220);\n"
"padding-left: 0px;\n"
"padding-right:0px;\n"
"padding-bottom:0px;\n"
"padding-top:0px;\n"
"}\n"
"\n"
"QToolButton:checked{\n"
"border: none;\n"
"background-color: rgba(40,40,40,220);\n"
"padding-left: 0px;\n"
"padding-right:0px;\n"
"padding-bottom:0px;\n"
"padding-top:0px;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"UI icon/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_box_mode.setIcon(icon10)
        self.button_box_mode.setIconSize(QSize(26, 26))
        self.button_box_mode.setCheckable(True)
        self.button_view_mode = QToolButton(self.frame_mode)
        self.mode_button_group.addButton(self.button_view_mode)
        self.button_view_mode.setObjectName(u"button_view_mode")
        self.button_view_mode.setGeometry(QRect(5, 10, 40, 40))
        self.button_view_mode.setStyleSheet(u"QToolButton{\n"
"border-radius: 5px;\n"
"min-width:40px;\n"
"max-width:40px;\n"
"min-height:40px;\n"
"max-height:40px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: none;\n"
"background-color: rgba(40,40,40,220);\n"
"padding-left: 0px;\n"
"padding-right:0px;\n"
"padding-bottom:0px;\n"
"padding-top:0px;\n"
"}\n"
"\n"
"QToolButton:checked{\n"
"border: none;\n"
"background-color: rgba(40,40,40,220);\n"
"padding-left: 0px;\n"
"padding-right:0px;\n"
"padding-bottom:0px;\n"
"padding-top:0px;\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"UI icon/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_view_mode.setIcon(icon11)
        self.button_view_mode.setIconSize(QSize(26, 26))
        self.button_view_mode.setCheckable(True)
        self.button_view_mode.setChecked(True)
        self.button_point_mode = QToolButton(self.frame_mode)
        self.mode_button_group.addButton(self.button_point_mode)
        self.button_point_mode.setObjectName(u"button_point_mode")
        self.button_point_mode.setGeometry(QRect(5, 55, 40, 40))
        self.button_point_mode.setStyleSheet(u"QToolButton{\n"
"border-radius: 5px;\n"
"min-width:40px;\n"
"max-width:40px;\n"
"min-height:40px;\n"
"max-height:40px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QToolButton:pressed{\n"
"border: none;\n"
"background-color: rgba(40,40,40,220);\n"
"padding-left: 0px;\n"
"padding-right:0px;\n"
"padding-bottom:0px;\n"
"padding-top:0px;\n"
"}\n"
"\n"
"QToolButton:checked{\n"
"border: none;\n"
"background-color: rgba(40,40,40,220);\n"
"padding-left: 0px;\n"
"padding-right:0px;\n"
"padding-bottom:0px;\n"
"padding-top:0px;\n"
"}\n"
"")
        icon12 = QIcon()
        icon12.addFile(u"UI icon/point.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_point_mode.setIcon(icon12)
        self.button_point_mode.setIconSize(QSize(24, 24))
        self.button_point_mode.setCheckable(True)
        self.frame_mode_border = QFrame(self.frame_mode)
        self.frame_mode_border.setObjectName(u"frame_mode_border")
        self.frame_mode_border.setGeometry(QRect(10, 145, 30, 5))
        self.frame_mode_border.setStyleSheet(u"border-bottom: 1px solid rgba(180, 180, 180, 200)")
        self.frame_mode_border.setFrameShape(QFrame.StyledPanel)
        self.frame_mode_border.setFrameShadow(QFrame.Raised)
        self.frame_settings_2 = QFrame(self.frame_function_bar)
        self.frame_settings_2.setObjectName(u"frame_settings_2")
        self.frame_settings_2.setGeometry(QRect(0, 250, 50, 150))
        self.frame_settings_2.setStyleSheet(u"background: transparent;")
        self.frame_settings_2.setFrameShape(QFrame.StyledPanel)
        self.frame_settings_2.setFrameShadow(QFrame.Raised)
        self.button_add_group = QPushButton(self.frame_settings_2)
        self.button_add_group.setObjectName(u"button_add_group")
        self.button_add_group.setGeometry(QRect(5, 10, 40, 40))
        self.button_add_group.setToolTipDuration(0)
        self.button_add_group.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:40px;\n"
"max-width:40px;\n"
"min-height:40px;\n"
"max-height:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color: rgba(40,40,40,220);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/square-add-white.svg);\n"
"}\n"
"")
        icon13 = QIcon()
        icon13.addFile(u"UI icon/square-add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_add_group.setIcon(icon13)
        self.button_add_group.setIconSize(QSize(24, 24))
        self.frame_settings_border_2 = QFrame(self.frame_settings_2)
        self.frame_settings_border_2.setObjectName(u"frame_settings_border_2")
        self.frame_settings_border_2.setGeometry(QRect(10, 145, 30, 5))
        self.frame_settings_border_2.setStyleSheet(u"border-bottom: 1px solid rgba(180, 180, 180, 200)")
        self.frame_settings_border_2.setFrameShape(QFrame.StyledPanel)
        self.frame_settings_border_2.setFrameShadow(QFrame.Raised)
        self.button_generate_mask = QPushButton(self.frame_settings_2)
        self.button_generate_mask.setObjectName(u"button_generate_mask")
        self.button_generate_mask.setGeometry(QRect(5, 55, 40, 40))
        self.button_generate_mask.setFont(font1)
        self.button_generate_mask.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:40px;\n"
"max-width:40px;\n"
"min-height:40px;\n"
"max-height:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color: rgba(40,40,40,220);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/generate-mask-white.svg);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"UI icon/generate-mask.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_generate_mask.setIcon(icon14)
        self.button_generate_mask.setIconSize(QSize(24, 24))
        self.button_auto_mask = QPushButton(self.frame_settings_2)
        self.button_auto_mask.setObjectName(u"button_auto_mask")
        self.button_auto_mask.setGeometry(QRect(5, 100, 40, 40))
        self.button_auto_mask.setFont(font1)
        self.button_auto_mask.setStyleSheet(u"QPushButton{\n"
"border-radius: 5px;\n"
"min-width:40px;\n"
"max-width:40px;\n"
"min-height:40px;\n"
"max-height:40px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(80,80,80,50);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"border: transparent;\n"
"background-color: rgba(40,40,40,220);\n"
"icon: url(D:/Python Coding/easy-to-segment/UI icon/magic-white.svg);\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"UI icon/magic.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_auto_mask.setIcon(icon15)
        self.button_auto_mask.setIconSize(QSize(24, 24))
        self.frame_mask_list = QFrame(self.frame_main)
        self.frame_mask_list.setObjectName(u"frame_mask_list")
        self.frame_mask_list.setGeometry(QRect(800, 50, 200, 550))
        self.frame_mask_list.setFrameShape(QFrame.StyledPanel)
        self.frame_mask_list.setFrameShadow(QFrame.Raised)
        self.frame_mask_list_border = QFrame(self.frame_mask_list)
        self.frame_mask_list_border.setObjectName(u"frame_mask_list_border")
        self.frame_mask_list_border.setGeometry(QRect(0, 0, 10, 550))
        self.frame_mask_list_border.setStyleSheet(u"border-left: 1px solid rgba(180, 180, 180, 200)")
        self.frame_mask_list_border.setFrameShape(QFrame.StyledPanel)
        self.frame_mask_list_border.setFrameShadow(QFrame.Raised)
        self.frame_display = QFrame(self.frame_main)
        self.frame_display.setObjectName(u"frame_display")
        self.frame_display.setGeometry(QRect(50, 550, 750, 50))
        self.frame_display.setFrameShape(QFrame.StyledPanel)
        self.frame_display.setFrameShadow(QFrame.Raised)
        self.frame_display_border = QFrame(self.frame_display)
        self.frame_display_border.setObjectName(u"frame_display_border")
        self.frame_display_border.setGeometry(QRect(0, 0, 750, 10))
        self.frame_display_border.setStyleSheet(u"border-top: 1px solid rgba(180, 180, 180, 200)")
        self.frame_display_border.setFrameShape(QFrame.StyledPanel)
        self.frame_display_border.setFrameShadow(QFrame.Raised)
        self.image_viewer = QGraphicsView(self.frame_main)
        self.image_viewer.setObjectName(u"image_viewer")
        self.image_viewer.setGeometry(QRect(50, 50, 750, 500))
        self.image_viewer.setStyleSheet(u"border-radius:0px;\n"
"background-color: rgb(220, 220, 220)")
        self.image_viewer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.image_viewer.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.image_viewer.setDragMode(QGraphicsView.ScrollHandDrag)
        self.image_viewer.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.image_viewer.setResizeAnchor(QGraphicsView.AnchorViewCenter)
        self.image_viewer.raise_()
        self.frame_top_bar.raise_()
        self.frame_function_bar.raise_()
        self.frame_mask_list.raise_()
        self.frame_display.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_import.setText("")
        self.cbox_mode.setItemText(0, QCoreApplication.translate("Form", u"2D", None))
        self.cbox_mode.setItemText(1, QCoreApplication.translate("Form", u"3D", None))

        self.button_minimize.setText("")
        self.button_close.setText("")
        self.button_undo.setText("")
        self.button_redo.setText("")
        self.button_reset.setText("")
        self.button_settings.setText("")
        self.button_save.setText("")
        self.button_box_mode.setText(QCoreApplication.translate("Form", u"...", None))
        self.button_view_mode.setText("")
        self.button_point_mode.setText(QCoreApplication.translate("Form", u"...", None))
        self.button_add_group.setText("")
        self.button_generate_mask.setText("")
        self.button_auto_mask.setText("")
    # retranslateUi

