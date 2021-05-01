from PyQt5 import QtWidgets, QtCore
from typing import List, NamedTuple, Any

from .stats import TextStatsWidget
from .widget_with_data_tracker import WidgetWithDataTracker

Cords = NamedTuple("Cords", [("x", int), ("y", int), ("w", int), ("h", int)])
Section = NamedTuple("Section", [("widget", QtWidgets.QWidget), ("cords", Cords)])


class DashboardPage(QtWidgets.QWidget):
    def __init__(self, crawler, speed_report_widget, stats_widgets: List[TextStatsWidget]):
        super().__init__()
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)

        self.widgets_with_tracker: List[WidgetWithDataTracker] = [speed_report_widget]

        layout.addWidget(speed_report_widget, 0, 0, 2, 2)

        for widget, cords in self._get_sections(stats_widgets):
            self.widgets_with_tracker.append(widget)
            layout.addWidget(widget, cords.y, cords.x,
                             cords.h, cords.w)

        timer = QtCore.QTimer()
        self.crawler = crawler
        timer.timeout.connect(self._update_dashboard())
        timer.start(1000)

    def _update_dashboard(self):
        new_state = self.crawler.get_tracker_state()
        for widget in self.widgets_with_tracker:
            widget.update_state(new_state)

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
        return res
