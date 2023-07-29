import ctypes

import cv2
import numpy as np
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QIcon, QPixmap, QWheelEvent, QImage, QBrush, QPen
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QGraphicsView, \
    QGraphicsPixmapItem, QWidget, QGraphicsEllipseItem
from matplotlib import pyplot as plt
from matplotlib.backends.backend_template import FigureCanvas
from segment_anything import sam_model_registry, SamPredictor

from Resources.main_structure import Ui_Form


def show_mask(mask, ax, random_color=False):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([30 / 255, 144 / 255, 255 / 255, 0.6])
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    mask_image = (mask_image * 255).astype(np.uint8)
    return mask_image


def show_points(coords, labels, ax, marker_size=375):
    pos_points = coords[labels == 1]
    neg_points = coords[labels == 0]
    ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='.', s=marker_size)
    ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='.', s=marker_size)


def show_box(box, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0, 0, 0, 0), lw=2))


def register_model():
    sam_checkpoint = "D:/Python Coding/segment-model/sam_vit_h_4b8939.pth"
    model_type = "vit_h"
    device = "cuda"

    sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
    sam.to(device=device)
    predictor = SamPredictor(sam)
    return predictor


def segment(predictor, image_path, input_point, input_label):
    if image_path is not None and input_point is not None:
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        predictor.set_image(image)

        masks, _, _ = predictor.predict(
            point_coords=input_point,
            point_labels=input_label,
            multimask_output=False,
        )
        mask_image = show_mask(masks, plt.gca())
        return mask_image



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.image_path = None
        self.segment_type = None
        self.offset = None
        self.draggable = None
        self.zoom_in_times = 0

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowIcon(QIcon('UI icon/logo.png'))

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.model = register_model()

        self.ui.image_viewer = ImageViewer(self.ui.frame_main)

        self.ui.image_viewer.setGeometry(50, 40, 750, 510)
        self.ui.image_viewer.setStyleSheet("border-radius: 0px; background-color: rgb(230, 230, 230);")

        self.ui.button_import.clicked.connect(self.load_image_viewer)

        self.ui.button_close.clicked.connect(self.close)
        self.ui.button_minimize.clicked.connect(self.showMinimized)

        self.ui.button_generate_mask.clicked.connect(self.generate_mask)
        self.ui.button_reset.clicked.connect(self.reset_mask)

        self.ui.button_view_mode.setIcon(QIcon('UI icon/view-white.svg'))

        self.ui.mode_button_group.buttonClicked.connect(self.group_button_click)
        self.ui.mode_button_group.buttonClicked.connect(self.view_mode_check)

        self.ui.mode_button_group.buttonPressed.connect(self.group_button_press)

    def group_button_click(self, button):
        if button == self.ui.button_point_mode:
            button.setIcon(QIcon('UI icon/point-white.svg'))
            self.ui.button_view_mode.setIcon(QIcon('UI icon/view.svg'))
            self.ui.button_box_mode.setIcon(QIcon('UI icon/box.svg'))

        elif button == self.ui.button_box_mode:
            button.setIcon(QIcon('UI icon/box-white.svg'))
            self.ui.button_point_mode.setIcon(QIcon('UI icon/point.svg'))
            self.ui.button_view_mode.setIcon(QIcon('UI icon/view.svg'))

        elif button == self.ui.button_view_mode:
            button.setIcon(QIcon('UI icon/view-white.svg'))
            self.ui.button_point_mode.setIcon(QIcon('UI icon/point.svg'))
            self.ui.button_box_mode.setIcon(QIcon('UI icon/box.svg'))

    def group_button_press(self, button):
        if button == self.ui.button_point_mode:
            button.setIcon(QIcon('UI icon/point-white.svg'))

        elif button == self.ui.button_box_mode:
            button.setIcon(QIcon('UI icon/box-white.svg'))

        elif button == self.ui.button_view_mode:
            button.setIcon(QIcon('UI icon/view-white.svg'))

    def import_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Select Image File")
        file_dialog.setNameFilter("Image Files (*.png *.jpg *.bmp)")
        if file_dialog.exec():
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

    def generate_mask(self):
        image_path = self.image_path
        input_point = self.ui.image_viewer.point_pos
        input_label = self.ui.image_viewer.point_type

        mask_image = segment(self.model, image_path, input_point, input_label)
        q_image = QImage(mask_image.data, mask_image.shape[1], mask_image.shape[0], QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(q_image)
        pix_item = QGraphicsPixmapItem(pixmap)
        self.ui.image_viewer.scene.addItem(pix_item)

    def reset_mask(self):
        self.ui.image_viewer.scene.clear()

        self.ui.image_viewer.set_image(self.image_path)
        self.ui.image_viewer.set_scene()

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
        self.point_pos = None
        self.point_type = None

        self.pixmap = None
        self.pixmap_item = None

        self.zoom_in_times = 0
        self.is_wheel_enable = False

        self.is_point_pos_enable = False

        self.scene = QGraphicsScene()

    def set_image(self, image_path):
        self.resetTransform()
        self.pixmap = QPixmap(image_path)
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
        if self.is_wheel_enable and self.pixmap_item is not None:
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

            view_pos = event.pos()
            self.scene_pos = self.mapToScene(view_pos)
            x, y = self.scene_pos.x(), self.scene_pos.y()

            if self.is_point_pos_valid():

                self.point_pos = np.array([[self.scene_pos.x(), self.scene_pos.y()]])

                if event.button() == Qt.LeftButton:
                    self.point_type = np.array([1])
                    color = Qt.green
                elif event.button() == Qt.RightButton:
                    self.point_type = np.array([0])
                    color = Qt.red

                point_item = QGraphicsEllipseItem(x-25, y-25, 50, 50)
                point_item.setBrush(color)
                self.scene.addItem(point_item)

            else:
                self.point_pos = None







if __name__ == '__main__':
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("easy-to-segment")

    app = QApplication([])
    window = MainWindow()
    window.show()

    app.exec()






