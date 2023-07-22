import cv2
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QGraphicsView
from segment_anything import sam_model_registry, SamPredictor

from main_structure import Ui_Form

sam_checkpoint = "D:/Python Coding/segment-model/sam_vit_h_4b8939.pth"
model_type = "vit_h"

device = "cuda"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)
predictor = SamPredictor(sam)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.offset = None
        self.draggable = None

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.image_viewer = ImageViewer()
        self.ui.image_view.setScene(self.image_viewer.scene)

        self.ui.button_import.clicked.connect(self.image_viewer.import_image)

        self.ui.button_close.clicked.connect(self.close)
        self.ui.button_minimize.clicked.connect(self.showMinimized)

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
            new_pos = event.globalPos() - self.offset
            self.move(new_pos)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False


class ImageViewer(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.pixmap_item = None
        self.pixmap = None
        self.scene = QGraphicsScene()

    def import_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Select Image File")
        file_dialog.setNameFilter("Image Files (*.png *.jpg *.bmp)")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            image_path = file_dialog.selectedFiles()[0]

        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        predictor.set_image(image)
        q_image = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(q_image)
        self.pixmap_item = self.scene.addPixmap(self.pixmap)
        self.scene.addItem(self.pixmap_item)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
