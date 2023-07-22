import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPainter, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QFileDialog
from matplotlib import pyplot as plt

from main_structure import Ui_Form
from ImageViewer import ImageViewer
from segment_anything import sam_model_registry, SamPredictor


sam_checkpoint = "D:/Python Coding/segment-model/sam_vit_h_4b8939.pth"
model_type = "vit_h"

device = "cuda"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)
predictor = SamPredictor(sam)


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

        self.scene_pos = None

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.image_viewer = ImageViewer()
        self.image_viewer.widget()
        self.ui.image_view.setScene(self.image_viewer.scene)

        self.ui.button_import.clicked.connect(self.image_viewer.import_image)

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
            view_pos = event.pos()
            scene_pos = self.ui.image_view.mapToScene(view_pos)
            self.scene_pos = np.array([scene_pos.x(), scene_pos.y()])

    def mouseMoveEvent(self, event):
        if self.draggable and event.buttons() == Qt.LeftButton:
            new_pos = event.globalPos() - self.offset
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False


test = MainWindow()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
