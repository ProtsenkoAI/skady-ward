from PyQt5 import QtWidgets
from typing import List, NamedTuple, Any

from .stats import TextStatsWidget, ProxyStats, CredsStats
from .data_trackers import CredsDataTracker, ProxyDataTracker
from .parse_speed_plot import ParseSpeedPlot
import sys

Cords = NamedTuple("Cords", [("x", int), ("y", int), ("w", int), ("h", int)])
Section = NamedTuple("Section", [("widget", QtWidgets.QWidget), ("cords", Cords)])


class DashboardPage(QtWidgets.QWidget):
    def __init__(self, speed_report_widget, stats_widgets: List[TextStatsWidget]):
        super().__init__()
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)

        layout.addWidget(speed_report_widget, 0, 0, 2, 2)

        for widget, cords in self._get_sections(stats_widgets):
            layout.addWidget(widget, cords.y, cords.x,
                             cords.h, cords.w)
            print(widget)

    def _get_sections(self, widgets) -> List[Section]:
        # hardcoding positions, if will need to expand number of widgets, need to
        #   find free positions automatically
        widgets_cords = [(2, 0), (2, 1), (0, 2), (1, 2), (2, 2), None]
        res = []
        for widget, cords in zip(widgets, widgets_cords):
            if cords is None:
                raise ValueError("out of cords, check source code")

            width, height = 1, 1
            res.append(Section(widget, Cords(*cords, width, height)))
        print(res)
        return res


if __name__ == "__main__":
    stats_widgets = [
        ProxyStats(ProxyDataTracker()),
        CredsStats(CredsDataTracker())
    ]

    app = QtWidgets.QApplication(stats_widgets)

    widget = DashboardPage(stats_widgets)
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
