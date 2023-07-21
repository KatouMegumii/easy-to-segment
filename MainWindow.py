from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup

from main_structure import Ui_Form


def button_enter(button, icon_path):
    button.setIcon(QIcon(icon_path))


def button_leave(button, icon_path, icon_path_checked):
    if button.isChecked():
        button.setIcon(QIcon(icon_path_checked))
    else:
        button.setIcon(QIcon(icon_path))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.offset = None
        self.draggable = None

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.button_close.clicked.connect(self.close)
        self.ui.button_minimize.clicked.connect(self.showMinimized)

        self.ui.button_point_mode.leaveEvent = lambda event: button_leave(self.ui.button_point_mode, '../easy-to-segment/UI icon/point.svg', '../easy-to-segment/UI icon/point-white.svg')

        self.ui.button_box_mode.leaveEvent = lambda event: button_leave(self.ui.button_box_mode, '../easy-to-segment/UI icon/box.svg', '../easy-to-segment/UI icon/box-white.svg')

        self.ui.button_view_mode.leaveEvent = lambda event: button_leave(self.ui.button_view_mode, '../easy-to-segment/UI icon/view.svg', '../easy-to-segment/UI icon/view-white.svg')

        self.ui.button_view_mode.setIcon(QIcon('../easy-to-segment/UI icon/view-white.svg'))

        self.ui.mode_button_group.buttonClicked.connect(self.group_button_click)
        self.ui.mode_button_group.buttonPressed.connect(self.group_button_press)

    def group_button_click(self, button):
        if button == self.ui.button_point_mode:
            button.setIcon(QIcon('../easy-to-segment/UI icon/point-white.svg'))
            self.ui.button_view_mode.setIcon(QIcon('../easy-to-segment/UI icon/view.svg'))
            self.ui.button_box_mode.setIcon(QIcon('../easy-to-segment/UI icon/box.svg'))
        elif button == self.ui.button_box_mode:
            button.setIcon(QIcon('../easy-to-segment/UI icon/box-white.svg'))
            self.ui.button_point_mode.setIcon(QIcon('../easy-to-segment/UI icon/point.svg'))
            self.ui.button_view_mode.setIcon(QIcon('../easy-to-segment/UI icon/view.svg'))
        elif button == self.ui.button_view_mode:
            button.setIcon(QIcon('../easy-to-segment/UI icon/view-white.svg'))
            self.ui.button_point_mode.setIcon(QIcon('../easy-to-segment/UI icon/point.svg'))
            self.ui.button_box_mode.setIcon(QIcon('../easy-to-segment/UI icon/box.svg'))

    def group_button_press(self, button):
        if button == self.ui.button_point_mode:
            button.setIcon(QIcon('../easy-to-segment/UI icon/point-white.svg'))
        elif button == self.ui.button_box_mode:
            button.setIcon(QIcon('../easy-to-segment/UI icon/box-white.svg'))
        elif button == self.ui.button_view_mode:
            button.setIcon(QIcon('../easy-to-segment/UI icon/view-white.svg'))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.draggable and event.buttons() == Qt.LeftButton:
            # 计算鼠标的偏移量
            new_pos = event.globalPos() - self.offset
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
