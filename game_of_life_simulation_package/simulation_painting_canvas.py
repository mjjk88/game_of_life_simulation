from PyQt5 import QtGui
from PyQt5.QtWidgets import QLabel


class SimulationPaintingCanvas(QLabel):
    def __init__(self, parent, ls):
        super().__init__(parent)
        self.ls = ls
        self.cell_size = 0  # parent.cell_size #int(parent.cell_size_line_edit.text())
        self.box_length = self.ls.box_length

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

        x_pixel = event.pos().x()
        y_pixel = event.pos().y()

        cell_x = x_pixel // self.cell_size
        cell_y = y_pixel // self.cell_size
        self.ls.alive_cells_coordinates.add((cell_x, cell_y))

        self.refresh()

    def refresh(self):
        painter = QtGui.QPainter()
        pen = QtGui.QPen()
        pen.setWidth(self.cell_size)
        pen.setColor(QtGui.QColor(0x0000FF))

        canvas = QtGui.QPixmap(self.cell_size * self.box_length, self.cell_size * self.box_length)
        painter.begin(canvas)
        painter.eraseRect(0, 0, self.cell_size * self.box_length, self.cell_size * self.box_length)
        painter.setPen(pen)

        for (x, y) in self.ls.alive_cells_coordinates:
            painter.drawPoint(self.cell_size * x + self.cell_size // 2, self.cell_size * y + self.cell_size // 2)
        painter.end()
        self.setPixmap(canvas)