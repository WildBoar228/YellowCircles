import random
import sys
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QPushButton, QInputDialog)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.stripes = ''
        self.is_pressed = False;
        self.initUI()

    def initUI(self):
        self.drawBtn.clicked.connect(self.paint)

    def paint(self):
        self.is_pressed = True;
        self.repaint()

    def paintEvent(self, event):
        if self.is_pressed:
            qp = QPainter(self)
            qp.setBrush(QColor(255, 255, 0))
            qp.begin(self)
            size = random.randint(20, 70)
            qp.drawEllipse(random.randint(size // 2, self.width() - size // 2),
                           random.randint(size // 2, self.height() - size // 2),
                           size, size)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
