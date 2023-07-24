import cv2
import numpy as np
from PySide6.QtCore import Qt, QRectF
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

        self.image_path = None
        self.offset = None
        self.draggable = None
        self.zoom_in_times = 0

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.image_viewer = ImageViewer(self.ui.frame_main)

        self.ui.image_viewer.setGeometry(50, 50, 750, 500)
        self.ui.image_viewer.setStyleSheet("border-radius: 0px; background-color: rgba(200,200,200,200);")

        self.ui.button_import.clicked.connect(self.load_image_viewer)

        self.ui.button_close.clicked.connect(self.close)
        self.ui.button_minimize.clicked.connect(self.showMinimized)

        self.ui.button_view_mode.setIcon(QIcon('../easy-to-segment/UI icon/view-white.svg'))

        self.ui.mode_button_group.buttonClicked.connect(self.group_button_click)
        self.ui.mode_button_group.buttonClicked.connect(self.view_mode_check)

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

    def import_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Select Image File")
        file_dialog.setNameFilter("Image Files (*.png *.jpg *.bmp)")
        if file_dialog.exec_():
            self.image_path = file_dialog.selectedFiles()[0]
            return self.image_path

    def load_image_viewer(self):
        self.ui.image_viewer.set_image(self.import_image())
        self.ui.image_viewer.set_scene()
        self.view_mode_check()

    def view_mode_check(self):
        if self.ui.button_view_mode.isChecked():
            self.ui.image_viewer.is_wheel_enable = True
        else:
            self.ui.image_viewer.is_wheel_enable = False

        self.ui.image_viewer.set_drag_mode_enable()
        self.ui.image_viewer.set_point_mode_enable()

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

        self.scene_pos = None
        self.q_image = None
        self.pixmap = None
        self.pixmap_item = None

        self.zoom_in_times = 0
        self.is_wheel_enable = False

        self.is_point_pos_enable = False
        self.point_pos = None

        self.scene = QGraphicsScene()

    def set_image(self, image_path):
        self.resetTransform()

        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        predictor.set_image(image)

        self.q_image = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(self.q_image)
        self.pixmap_item = QGraphicsPixmapItem(self.pixmap)

    def set_scene(self):
        self.scene.clear()

        self.scene.setSceneRect(QRectF(self.pixmap.rect()))
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        self.scene.addItem(self.pixmap_item)
        self.setScene(self.scene)

        self.fitInView(self.pixmap_item, Qt.KeepAspectRatio)

    def set_drag_mode_enable(self):
        if self.is_wheel_enable:
            self.setDragMode(QGraphicsView.ScrollHandDrag)
        else:
            self.setDragMode(QGraphicsView.NoDrag)

    def set_point_mode_enable(self):
        if self.is_wheel_enable and self.pixmap_item is not None:
            self.is_point_pos_enable = False
        else:
            self.is_point_pos_enable = True

    def is_point_pos_valid(self):
        image_height, image_width = self.pixmap_item.pixmap().height(), self.pixmap_item.pixmap().width()

        if self.scene_pos.x() < 0 or self.scene_pos.y() < 0 or self.scene_pos.x() > image_width or self.scene_pos.y() > image_height:
            is_valid = False
        else:
            is_valid = True

        return is_valid

    def zoom_in(self):
        self.zoom_in_times += 1
        self.scale(1.1, 1.1)

    def zoom_out(self):
        pw = self.width()
        ph = self.height()

        w = pw * 1.1 ** self.zoom_in_times
        h = ph * 1.1 ** self.zoom_in_times

        if w > pw or h > ph:
            self.scale(1/1.1, 1/1.1)
            self.zoom_in_times -= 1

    def wheelEvent(self, event: QWheelEvent):
        delta = event.angleDelta().y()
        if self.is_wheel_enable:
            if delta > 0:
                self.zoom_in()
            else:
                self.zoom_out()

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

        if self.is_point_pos_enable:
            if event.button() == Qt.LeftButton:
                view_pos = event.pos()
                self.scene_pos = self.mapToScene(view_pos)
                if self.is_point_pos_valid():
                    self.point_pos = np.array([self.scene_pos.x(), self.scene_pos.y()])
                else:
                    self.point_pos = None


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


