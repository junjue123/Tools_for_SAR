from PyQt5 import QtWidgets, QtGui, QtCore

class ZoomableDraggableLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(ZoomableDraggableLabel, self).__init__(parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setMouseTracking(True)
        self._pixmap = None
        self._scale_factor = 1.0
        self._dragging = False
        self._drag_start_position = None
        self._pixmap_offset = QtCore.QPoint(0, 0)
        self.original_width = None
        self.original_height = None

    def get_size(self,width,height):
        self.original_width = width
        self.original_height = height

    def setPixmap(self, pixmap):
        self._pixmap = pixmap
        self._pixmap_offset = QtCore.QPoint(0, 0)

        # 获取label的尺寸
        label_size = self.size()

        # 获取图像的原始尺寸
        pixmap_size = pixmap.size()

        # 计算宽度和高度的缩放比例
        scale_w = label_size.width() / pixmap_size.width()
        scale_h = label_size.height() / pixmap_size.height()

        # 选择较小的缩放比例，这样可以确保图像在label中完全显示
        self._scale_factor = min(scale_w, scale_h)
        self._pixmap_offset = QtCore.QPoint(0, 0)

        # 更新显示
        self.update()

    def wheelEvent(self, event):
        if self._pixmap:
            # 获取当前鼠标位置相对于 QLabel 的坐标
            mouse_position = event.pos()

            # 计算缩放前的图像位置
            relative_mouse_pos = mouse_position - self._pixmap_offset

            # 根据滚轮方向调整缩放因子
            angle_delta = event.angleDelta().y()
            if angle_delta > 0:
                scale_factor_increment = 1.05
            else:
                scale_factor_increment = 0.95

            new_scale_factor = self._scale_factor * scale_factor_increment

            # 计算缩放后的相对坐标
            new_relative_mouse_pos = relative_mouse_pos * (new_scale_factor / self._scale_factor)

            # 更新偏移量，确保鼠标位置的像素在缩放后保持不变
            self._pixmap_offset += (relative_mouse_pos - new_relative_mouse_pos)*new_scale_factor

            # 更新缩放因子
            self._scale_factor = new_scale_factor

            # 触发重绘
            self.update()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._dragging = True
            self._drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if self._dragging and self._pixmap:
            offset = event.pos() - self._drag_start_position
            self._pixmap_offset += offset
            self._drag_start_position = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._dragging = False

    def paintEvent(self, event):
        super(ZoomableDraggableLabel, self).paintEvent(event)
        if self._pixmap:
            painter = QtGui.QPainter(self)

            # 使用高质量的 QImage 进行处理
            qimage = self._pixmap.toImage()

            # 缩放 QImage 并保持高质量
            scaled_qimage = qimage.scaled(
                self._pixmap.size() * self._scale_factor,
                QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation
            )

            # 将处理后的 QImage 转回 QPixmap
            scaled_pixmap = QtGui.QPixmap.fromImage(scaled_qimage)

            pixmap_rect = scaled_pixmap.rect()
            pixmap_rect.moveCenter(self.rect().center() + self._pixmap_offset)
            painter.drawPixmap(pixmap_rect, scaled_pixmap)

    def center_on_coordinates(self, x, y, target_width, target_height):
        if self._pixmap:
            # 计算目标缩放比例
            pixmap_size = self._pixmap.size()
            scale_x = self.original_width / pixmap_size.width()
            scale_y = self.original_height / pixmap_size.height()
            self._scale_factor = min(scale_x, scale_y)

            # 计算新的 QPixmap 大小
            scaled_pixmap_size = pixmap_size * self._scale_factor
            scaled_pixmap = self._pixmap.scaled(
                scaled_pixmap_size,
                QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation
            )

            # 设置 QLabel 的 Pixmap
            self.setPixmap(scaled_pixmap)
            self.setAlignment(QtCore.Qt.AlignCenter)

            # 获取目标图像的最大尺寸
            target_max_size = max(target_width, target_height)

            # 获取 QLabel 的最小尺寸
            label_min_size = min(self.original_width, self.original_height)

            # 计算缩放因子
            scale_factor = max(1,label_min_size / (target_max_size*24))

            # 计算新的偏移量，使指定的 (x, y) 坐标居中
            off_x = (self.original_width / 2 - x) * scale_factor
            off_y = (self.original_height / 2 - y) * scale_factor

            # 更新偏移量
            self._pixmap_offset = QtCore.QPoint(off_x, off_y)

            # 更新缩放
            self._scale_factor = scale_factor

            # 触发重绘
            self.update()