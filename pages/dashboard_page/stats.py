from PyQt5 import QtWidgets, QtGui, QtCore
import sys


class ProxyStats(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        text = QtWidgets.QLabel()
        text.setText("sdfaljdsg")
        layout.addWidget(text)
        layout.addWidget(text)

        radius = 40.0
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())

        self.setStyleSheet("background-color: yellow;")

        self.setMask(mask)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = ProxyStats()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
