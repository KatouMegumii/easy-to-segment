from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Qt, QTimer, QEvent
from main_structure import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # bar button
        self.ui.button_close.clicked.connect(self.close)
        self.ui.button_minimize.clicked.connect(self.showMinimized)


        # function buttons
        self.ui.button_auto_mask.enterEvent = self.button_auto_mask_enter
        self.ui.button_auto_mask.leaveEvent = self.button_auto_mask_leave

        self.ui.button_save.enterEvent = self.button_save_enter
        self.ui.button_save.leaveEvent = self.button_save_leave

        self.ui.button_new_class.enterEvent = self.button_new_class_enter
        self.ui.button_new_class.leaveEvent = self.button_new_class_leave

        self.ui.button_generate_mask.enterEvent = self.button_generate_mask_enter
        self.ui.button_generate_mask.leaveEvent = self.button_generate_mask_leave

    def button_auto_mask_enter(self, event):
        self.ui.button_auto_mask.setIcon(QIcon('../UI icon/magic-white.svg'))

    def button_auto_mask_leave(self, event):
        self.ui.button_auto_mask.setIcon(QIcon('../UI icon/magic.svg'))

    def button_save_enter(self, event):
        self.ui.button_save.setIcon(QIcon('../UI icon/save-white.svg'))

    def button_save_leave(self, event):
        self.ui.button_save.setIcon(QIcon('../UI icon/save.svg'))

    def button_new_class_enter(self, event):
        self.ui.button_new_class.setIcon(QIcon('../UI icon/square-add-white.svg'))

    def button_new_class_leave(self, event):
        self.ui.button_new_class.setIcon(QIcon('../UI icon/square-add.svg'))

    def button_generate_mask_enter(self, event):
        self.ui.button_generate_mask.setIcon(QIcon('../UI icon/generate-mask-white.svg'))

    def button_generate_mask_leave(self, event):
        self.ui.button_generate_mask.setIcon(QIcon('../UI icon/generate-mask.svg'))

    # 重写窗口拖动
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
