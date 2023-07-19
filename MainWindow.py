
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QTimer, QEvent
from main_structure import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.button_close.clicked.connect(self.delay_close)

    # 重写关闭按钮
    def delay_close(self):
        timer = QTimer(self)
        timer.start(200)
        timer.timeout.connect(self.close)

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


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
