from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QFileDialog


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
        self.scene.clear()
        self.pixmap = QPixmap(image_path)
        self.pixmap_item = QGraphicsPixmapItem(self.pixmap)
        self.scene.addItem(self.pixmap_item)

    def widget(self):
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)