from PySide6.QtWidgets import QGraphicsPixmapItem, QGraphicsItem


class ImageItem(QGraphicsPixmapItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFlag(self.GraphicsItemFlag.ItemIsMovable)
        self.is_x_pinned = True
        self.pinned_start = 0
        self.move_start = 0
        self.move_delta = 0
        self.move_ratio = 0

    def mousePressEvent(self, event):
        if self.is_x_pinned:
            self.pinned_start = event.scenePos().x()
            self.move_start = event.scenePos().y()
        else:
            self.move_start = event.scenePos().x()
            self.pinned_start = event.scenePos().y()

    def mouseMoveEvent(self, event):
        position = event.scenePos()
        if self.is_x_pinned:
            position.setX(self.pinned_start)
        else:
            position.setY(self.pinned_start)
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
