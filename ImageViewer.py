import cv2
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QFileDialog
from segment_anything import sam_model_registry, SamPredictor


sam_checkpoint = "D:/Python Coding/segment-model/sam_vit_h_4b8939.pth"
model_type = "vit_h"

device = "cuda"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)
predictor = SamPredictor(sam)


class ImageViewer(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.pixmap_item = None
        self.pixmap = None
        self.scene = QGraphicsScene()
        self.widget()

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
        self.setSceneRect(0, 0, self.pixmap.width(), self.pixmap.height())
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)


    def widget(self):
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)