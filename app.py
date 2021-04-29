import sys
from PyQt5 import QtWidgets
from top_bar import TopBar
from tabs import Tabs


class App(QtWidgets.QWidget):
    # TODO: use QtWidgets.MainWindow
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()

        top_bar = TopBar(height=46)
        tabs = Tabs()

        layout.addWidget(top_bar)
        layout.addWidget(tabs)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = App()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
