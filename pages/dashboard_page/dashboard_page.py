from PyQt5 import QtWidgets, QtCore
from typing import List, NamedTuple

from .stats import TextStatsWidget

Cords = NamedTuple("Cords", [("x", int), ("y", int), ("w", int), ("h", int)])
Section = NamedTuple("Section", [("widget", QtWidgets.QWidget), ("cords", Cords)])


class DashboardPage(QtWidgets.QWidget):
    def __init__(self, events_tracker, speed_report_widget, stats_widgets: List[TextStatsWidget]):
        super().__init__()
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)

        self.widgets_with_tracker: List[QtWidgets.QWidget] = [speed_report_widget]

        layout.addWidget(speed_report_widget, 0, 0, 2, 2)

        for widget, cords in self._get_sections(stats_widgets):
            self.widgets_with_tracker.append(widget)
            layout.addWidget(widget, cords.y, cords.x,
                             cords.h, cords.w)

        self.timer = QtCore.QTimer()
        self.tracker_with_state = events_tracker
        self.timer.timeout.connect(self._update_dashboard)
        self.timer.start(1000)

    def _update_dashboard(self):
        new_state = self.tracker_with_state.get_state()
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
