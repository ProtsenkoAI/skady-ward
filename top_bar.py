import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class TopBar(QtWidgets.QWidget):
    def __init__(self, height: int):
        super().__init__()
        layout = QtWidgets.QHBoxLayout()
        # TODO: manage paths better way
        logo_img = QtGui.QPixmap("./resources/TopLogo.png")
        logo_img = logo_img.scaled(height, height, aspectRatioMode=QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding)

        logo = QtWidgets.QLabel()
        logo.setPixmap(logo_img)

        layout.addWidget(logo)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = TopBar(height=70)
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
