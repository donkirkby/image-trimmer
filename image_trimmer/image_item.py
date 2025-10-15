from PySide6 import QtCore
from PySide6.QtWidgets import QGraphicsPixmapItem


class ImageItem(QGraphicsPixmapItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFlag(self.GraphicsItemFlag.ItemIsMovable)
        self.is_x_pinned = True
        self.pinned_start = 0
        self.move_start = 0
        self.move_delta = 0
        self.move_ratio = 0
        self.min_move = 0
        self.max_move = 0

    def mousePressEvent(self, event):
        if self.is_x_pinned:
            self.pinned_start = event.scenePos().x()
            self.move_start = self.scenePos().y()
        else:
            self.move_start = self.scenePos().x()
            self.pinned_start = event.scenePos().y()

    def mouseMoveEvent(self, event):
        position = event.scenePos()
        if self.is_x_pinned:
            position.setX(self.pinned_start)
            button_start = event.buttonDownScenePos(
                QtCore.Qt.MouseButton.LeftButton).y()
            move_delta = event.scenePos().y() - button_start
            move_end = self.move_start + move_delta
            if move_end < self.min_move:
                position.setY(self.min_move - self.move_start + button_start)
            elif self.max_move < move_end:
                position.setY(self.max_move - self.move_start + button_start)
        else:
            position.setY(self.pinned_start)
            button_start = event.buttonDownScenePos(
                QtCore.Qt.MouseButton.LeftButton).x()
            move_delta = event.scenePos().x() - button_start
            move_end = self.move_start + move_delta
            if move_end < self.min_move:
                position.setX(self.min_move - self.move_start + button_start)
            elif self.max_move < move_end:
                position.setX(self.max_move - self.move_start + button_start)
        event.setScenePos(position)
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        position = event.scenePos()
        if self.is_x_pinned:
            self.move_delta += position.y() - self.move_start
            self.move_ratio = self.move_delta / self.pixmap().height()
        else:
            self.move_delta += position.x() - self.move_start
            self.move_ratio = self.move_delta / self.pixmap().width()
