import cv2
import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QImage, QPixmap, QPainter, QWheelEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
from segment_anything import sam_model_registry, SamPredictor

from Resources.main_structure import Ui_Form

sam_checkpoint = "D:/Python Coding/segment-model/sam_vit_h_4b8939.pth"
model_type = "vit_h"

device = "cuda"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)
predictor = SamPredictor(sam)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.image_viewer = None
        self.offset = None
        self.draggable = None
        self.zoom_in_times = 0

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.button_import.clicked.connect(self.load_image_viewer)
        self.image_viewer = ImageViewer()

        self.ui.button_close.clicked.connect(self.close)
        self.ui.button_minimize.clicked.connect(self.showMinimized)

        self.ui.button_view_mode.setIcon(QIcon('../easy-to-segment/UI icon/view-white.svg'))

        self.ui.mode_button_group.buttonClicked.connect(self.group_button_click)
        self.ui.mode_button_group.buttonClicked.connect(self.if_view_mode_activated)
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

    def load_image_viewer(self):
        self.image_viewer.import_image()
        self.image_viewer.set_image(self.image_viewer.image_path)
        self.ui.image_viewer.setScene(self.image_viewer.scene)
        self.image_viewer_style()

    def image_viewer_style(self):
        self.ui.image_viewer.fitInView(self.image_viewer.scene.sceneRect(), Qt.KeepAspectRatio)

        self.ui.image_viewer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.image_viewer.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.ui.image_viewer.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def if_view_mode_activated(self):
        if self.ui.button_view_mode.isChecked():
            self.ui.image_viewer.setDragMode(QGraphicsView.ScrollHandDrag)
        else:
            self.ui.image_viewer.setDragMode(QGraphicsView.NoDrag)

    def zoom_in(self):
        self.zoom_in_times += 1
        self.ui.image_viewer.scale(1.1, 1.1)

    def zoom_out(self):
        pw = self.ui.image_viewer.width()
        ph = self.ui.image_viewer.height()

        w = pw * 1.1 ** self.zoom_in_times
        h = ph * 1.1 ** self.zoom_in_times

        if w > pw or h > ph:
            self.ui.image_viewer.scale(1/1.1, 1/1.1)
            self.zoom_in_times -= 1

    def wheelEvent(self, event: QWheelEvent):
        delta = event.angleDelta().y()/120
        if self.ui.button_view_mode.isChecked():
            if delta > 0:
                self.zoom_in()
            else:
                self.zoom_out()
        else:
            pass

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.draggable and event.buttons() == Qt.LeftButton:
            new_pos = event.globalPos() - self.offset
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False


class ImageViewer(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.image_path = None
        self.q_image = None
        self.pixmap = None
        self.pixmap_item = None

        self.scene = QGraphicsScene()

    def import_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Select Image File")
        file_dialog.setNameFilter("Image Files (*.png *.jpg *.bmp)")
        if file_dialog.exec_():
            self.image_path = file_dialog.selectedFiles()[0]
            return self.image_path

    def set_image(self, image_path):
        self.resetTransform()

        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        predictor.set_image(image)

        self.q_image = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(self.q_image)
        self.pixmap_item = QGraphicsPixmapItem(self.pixmap)

        self.pixmap_item.setTransformationMode(Qt.SmoothTransformation)
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        self.scene.clear()

        self.scene.addItem(self.pixmap_item)
        self.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
