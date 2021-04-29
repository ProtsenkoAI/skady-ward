from PyQt5 import QtWidgets
from typing import List, NamedTuple

from .stats import ProxyStats
import sys

Cords = NamedTuple("Cords", [("x", int), ("y", int), ("w", int), ("h", int)])
Section = NamedTuple("Section", [("widget", QtWidgets.QWidget), ("cords", Cords)])


class DashboardPage(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)

        for widget, cords in self._get_sections():
            layout.addWidget(widget, cords.y, cords.x,
                             cords.h, cords.w)

    def _get_sections(self) -> List[Section]:
        sections = []
        proxy_stats = ProxyStats()
        sections.append(Section(proxy_stats, Cords(0, 0, 1, 1)))

        return sections


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = DashboardPage()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
