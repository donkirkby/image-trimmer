import os
from pathlib import Path

from PySide6 import QtGui
from PySide6.QtCore import QSize, QTimer
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QSpacerItem, QSizePolicy

from image_trimmer.image_item import ImageItem
from image_trimmer.main_window import Ui_MainWindow


class ImageTrimmerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui = self.ui = Ui_MainWindow()
        ui.setupUi(self)

        ui.progress.setValue(0)

        ui.action_open_source.triggered.connect(self.on_open_source)
        ui.action_save_target.triggered.connect(self.on_save_target)
        ui.next.clicked.connect(self.on_next_image)
        ui.previous.clicked.connect(self.on_previous_image)
        ui.next.setEnabled(False)
        ui.previous.setEnabled(False)
        ui.aspect.setValidator(QtGui.QDoubleValidator())
        ui.aspect.textChanged.connect(self.on_aspect_changed)
        ui.statusbar.showMessage('Choose source and target folders.')

        self.scene = QGraphicsScene(0, 0, 400, 200)
        ui.preview.setScene(self.scene)
        self.raw_pixmap = QPixmap()
        self.pixmap_item = ImageItem(self)
        self.scene.addItem(self.pixmap_item)

        self.source_path: Path | None = None
        self.source_image_paths: list[Path] = []
        self.target_path: Path | None = None

        self.aspect_ratio = 0.0
        QTimer.singleShot(0, self.on_aspect_changed)

        default_source_path = Path(__file__).parent.parent / 'demo' / 'source'
        if default_source_path.exists():
            self.open_source(default_source_path)

    def on_open_source(self) -> None:
        kwargs = get_file_dialog_options()
        source_name: str
        source_name = QFileDialog.getExistingDirectory(
            self,
            'Open Source Folder',
            **kwargs)
        if not source_name:
            return

        self.open_source(source_name)

    def open_source(self, source_name: str | Path) -> None:
        self.source_path = Path(source_name)
        ui = self.ui
        if self.target_path:
            target_summary = f' to {self.target_path.name}'
        else:
            target_summary = ', choose a target folder'
        ui.statusbar.showMessage(
            f'Cropping from {self.source_path.name}{target_summary}.')

        self.source_image_paths.clear()
        for source_image_path in sorted(self.source_path.glob('*')):
            self.source_image_paths.append(source_image_path)
        ui.progress.setMaximum(len(self.source_image_paths))
        ui.progress.setValue(0)
        if not self.source_image_paths:
            ui.next.setEnabled(False)
        else:
            self.on_change_image(1)

    def on_save_target(self) -> None:
        kwargs = get_file_dialog_options()
        target_name: str
        target_name = QFileDialog.getExistingDirectory(
            self,
            'Open Target Folder',
            **kwargs)
        if not target_name:
            return

        self.target_path = Path(target_name)
        ui = self.ui
        if self.source_path:
            message = (f'Cropping from {self.source_path.name} '
                       f'to {self.target_path.name}.')
        else:
            message = (f'Cropping to {self.target_path.name}. '
                       f'Choose a source folder.')
        ui.statusbar.showMessage(message)

    def on_next_image(self):
        self.on_change_image(1)

    def on_previous_image(self):
        self.on_change_image(-1)

    def on_change_image(self, delta: int):
        ui = self.ui
        current_image_index = ui.progress.value() - 1
        new_image_index = current_image_index + delta
        new_image_path = self.source_image_paths[new_image_index]
        ui.progress.setValue(new_image_index+1)
        ui.previous.setEnabled(0 < new_image_index)
        ui.next.setEnabled(new_image_index < len(self.source_image_paths) - 1)
        self.raw_pixmap.load(str(new_image_path))
        self.on_aspect_changed()

    def on_aspect_changed(self, text: str | None = None) -> None:
        ui = self.ui
        if text is None:
            text = ui.aspect.text()
        if not text:
            return
        aspect_ratio = abs(float(text))
        if aspect_ratio == 0:
            return
        min_aspect_ratio = 0.2
        max_aspect_ratio = 7.0
        if aspect_ratio < min_aspect_ratio:
            aspect_ratio = min_aspect_ratio
            ui.aspect.setText(str(aspect_ratio))
        elif max_aspect_ratio < aspect_ratio:
            aspect_ratio = max_aspect_ratio
            ui.aspect.setText(str(aspect_ratio))

        self.aspect_ratio = aspect_ratio
        frame_width = ui.preview_frame.width()
        frame_height = ui.preview_frame.height()
        ideal_width = self.aspect_ratio * frame_height
        if ideal_width <= frame_width:
            # Pad left and right
            ui.preview.setSceneRect(0, 0, ideal_width, frame_height)
            total_padding = frame_width - ideal_width
            self.set_padding(total_padding,
                             ui.left_spacer,
                             ui.right_spacer,
                             ui.top_spacer,
                             ui.bottom_spacer)
        else:
            # Pad top and bottom
            ideal_height = frame_width / self.aspect_ratio
            ui.preview.setSceneRect(0, 0, frame_width, ideal_height)
            total_padding = frame_height - ideal_height
            self.set_padding(total_padding,
                             ui.top_spacer,
                             ui.bottom_spacer,
                             ui.left_spacer,
                             ui.right_spacer)
        if self.raw_pixmap.width() == 0:
            return
        preview_width = ui.preview.width()
        preview_height = ui.preview.height()
        scaled_pixmap = self.raw_pixmap.scaled(
            QSize(preview_width, preview_height),
            aspectMode=Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.pixmap_item.setPixmap(scaled_pixmap)
        self.pixmap_item.is_x_pinned = (
                preview_height < scaled_pixmap.height())
        if self.pixmap_item.is_x_pinned:
            min_move = preview_height - scaled_pixmap.height()
        else:
            min_move = preview_width - scaled_pixmap.width()
        self.pixmap_item.max_move = 0
        self.pixmap_item.min_move = min_move
        self.pixmap_item.setX((preview_width-scaled_pixmap.width()) // 2)
        self.pixmap_item.setY((preview_height-scaled_pixmap.height()) // 2)
        self.save_image()

    def on_image_moved(self):
        self.save_image()

    def set_padding(self,
                    total_padding: int,
                    padded1: QSpacerItem,
                    padded2: QSpacerItem,
                    squeezed1: QSpacerItem,
                    squeezed2: QSpacerItem) -> None:
        padding1 = total_padding // 2
        padding2 = total_padding - padding1
        fixed = QSizePolicy.Policy.Fixed
        padded1.changeSize(padding1, padding1, fixed, fixed)
        padded2.changeSize(padding2, padding2, fixed, fixed)
        squeezed1.changeSize(0, 0, fixed, fixed)
        squeezed2.changeSize(0, 0, fixed, fixed)
        self.ui.preview_frame.layout().invalidate()

    def save_image(self):
        if not self.target_path:
            return
        self.purge_target_images()
        ui = self.ui
        image_index = ui.progress.value() - 1
        source_image_path = self.source_image_paths[image_index]
        move_percent = self.pixmap_item.move_percent
        source_stem = source_image_path.stem
        suffix = source_image_path.suffix
        target_name = f'{source_stem}-{move_percent:02}-{image_index}{suffix}'
        target_image_path = self.target_path / target_name
        if self.pixmap_item.is_x_pinned:
            width = self.raw_pixmap.width()
            height = round(width / self.aspect_ratio)
            y0 = round((self.raw_pixmap.height() - height) * move_percent / 99)
            cropped_pixmap = self.raw_pixmap.copy(0, y0, width, height)
        else:
            height = self.raw_pixmap.height()
            width = round(height * self.aspect_ratio)
            x0 = round((self.raw_pixmap.width() - width) * move_percent / 99)
            cropped_pixmap = self.raw_pixmap.copy(x0, 0, width, height)
        cropped_pixmap.save(str(target_image_path))

        ui.statusbar.showMessage(
            f'Saved {self.source_path.name}/{source_image_path.name} as '
            f'{self.target_path}/{target_name}.')
        self.pixmap_item.is_dirty = False

    def purge_target_images(self):
        image_index = self.ui.progress.value() - 1
        stem_suffix = f'-{image_index}'
        for target_match in self.target_path.glob(f'*{stem_suffix}.*'):
            if target_match.stem.endswith(stem_suffix):
                target_match.unlink()

    def resizeEvent(self, event):
        self.on_aspect_changed()


def get_file_dialog_options():
    kwargs = {}
    if 'SNAP' in os.environ:
        # Native dialog restricts paths for snap processes to /run/user.
        kwargs['options'] = QFileDialog.Option.DontUseNativeDialog
    return kwargs


def main():
    app = QApplication()
    window = ImageTrimmerWindow()
    window.show()
    exit(app.exec())


if __name__ == '__main__':
    main()
