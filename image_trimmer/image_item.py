import typing
from typing import runtime_checkable

from PySide6 import QtCore
from PySide6.QtWidgets import QGraphicsPixmapItem


class ImageItem(QGraphicsPixmapItem):
    @runtime_checkable
    class Listener(typing.Protocol):
        def on_image_moved(self):
            ...

    def __init__(self, listener: Listener | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFlag(self.GraphicsItemFlag.ItemIsMovable)
        self.listener = listener
        self.is_x_pinned = True
        self.pinned_start = 0
        self.move_start = 0
        self.move_percent = 0
        self.min_move = 0
        self.max_move = 0

    def setX(self, x, /) -> None:
        super().setX(x)
        if not self.is_x_pinned:
            self.calculate_percent()

    def setY(self, y, /) -> None:
        super().setY(y)
        if self.is_x_pinned:
            self.calculate_percent()

    def calculate_percent(self) -> None:
        if self.is_x_pinned:
            move_delta = -self.y()
        else:
            move_delta = -self.x()
        max_delta = self.max_move - self.min_move
        if max_delta == 0:
            move_ratio = 0.0
        else:
            move_ratio = move_delta / (self.max_move - self.min_move)

        # Not quite percent, cap at two digits.
        self.move_percent = round(move_ratio * 99)

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
        self.calculate_percent()
        if self.listener:
            self.listener.on_image_moved()
