from PyQt5 import QtWidgets, QtCore, QtGui
from label import ZoomableDraggableLabel


class MyTableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.target_label = None  # 初始目标 QLabel 为 None

        # 连接单击事件
        self.cellClicked.connect(self.on_cell_clicked)

    def set_target_label(self, label):
        """设置目标 QLabel"""
        self.target_label = label

    def on_cell_clicked(self, row, column):
        if column == 0 and self.target_label is not None:  # 确保点击的是第一列且目标 QLabel 已设置
            coordinates_item = self.item(row, 2)  # 获取第三列的坐标信息
            if coordinates_item:
                coordinates = coordinates_item.text()
                # 去掉开头和结尾的方括号，然后通过逗号和空格分隔
                coordinates = coordinates.strip("[]")
                try:
                    # 将字符串转换为浮点数列表
                    points = []
                    for point_str in coordinates.split('], ['):
                        point = point_str.strip().split(',')
                        x, y = float(point[0].strip()), float(point[1].strip())
                        points.append((x, y))

                    if len(points) == 4:  # 检查是否有四个角点
                        # 找到外接矩形的边界
                        min_x = min(point[0] for point in points)
                        max_x = max(point[0] for point in points)
                        min_y = min(point[1] for point in points)
                        max_y = max(point[1] for point in points)

                        # 计算中心坐标
                        center_x = (min_x + max_x) / 2
                        center_y = (min_y + max_y) / 2

                        # 计算宽度和高度
                        width = max_x - min_x
                        height = max_y - min_y

                        # 调用函数来居中显示图像
                        self.center_image_at(center_x, center_y, width, height)
                    else:
                        print("Expected four corner points")
                except ValueError:
                    print("Invalid coordinate format")

    def center_image_at(self, x, y, width, height):
        """根据给定的坐标和尺寸，将图片的指定区域显示在 QLabel 的中心"""
        try:
            # 假设 target_label 是 ZoomableDraggableLabel 实例
            if isinstance(self.target_label, ZoomableDraggableLabel):
                self.target_label.center_on_coordinates(x, y, width, height)
            else:
                print("Target label is not an instance of ZoomableDraggableLabel.")
        except Exception as e:
            print(f"Error in center_image_at: {e}")

    def set_items_non_editable(self):
        """将表格中的所有单元格设置为不可编辑"""
        for row in range(self.rowCount()):
            for column in range(self.columnCount()):
                item = self.item(row, column)
                if item:
                    item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
