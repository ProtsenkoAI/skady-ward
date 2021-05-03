from PyQt5 import QtWidgets
from abc import abstractmethod
from typing import List

from .tracker_state_user import TrackerStateUser
from background_crawler import TrackerState

# TODO: setWordWrap to auto-split lines if they are too long
# TODO: apply listeners/notifiers to track stats


class TextStatsWidget(TrackerStateUser, QtWidgets.QGroupBox):
    def __init__(self, tab_name: str):
        QtWidgets.QGroupBox.__init__(self)

        self.setTitle(tab_name)
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.line_containers = None

    def update_state(self, tracker_state: TrackerState):
        new_stats_lines = self.create_report(tracker_state)
        if self.line_containers is None:
            self._create_line_containers(new_stats_lines)
        for line, line_container in zip(new_stats_lines, self.line_containers):
            line_container.setText(line)
            line_container.update()

    def _create_line_containers(self, report):
        self.line_containers = []

        for line in report:
            line_cont = QtWidgets.QLabel()
            line_cont.setText(line)
            self.layout().addWidget(line_cont)
            self.line_containers.append(line_cont)

    @abstractmethod
    def create_report(self, tracker_state: TrackerState) -> List[str]:
        ...


class ProxyStats(TextStatsWidget):
    def __init__(self):
        super().__init__(tab_name="Proxy Stats")

    def create_report(self, report_data: TrackerState) -> List[str]:
        return self._create_report_using_vars(
            report_data['working_proxies_cnt'], report_data["used_proxies_cnt"],
            report_data["cur_session_requests"], report_data["mean_session_lifetime"])

    def _create_report_using_vars(self, work_left, used_cnt: int, cur_requests, lifetime):
        return [f"Working proxies left: {work_left}",
                f"Already used proxies: {used_cnt}",
                f"Made {cur_requests} requests with current proxy",
                f"Mean proxy lifetime: {lifetime} req"
               ]


class CredsStats(TextStatsWidget):
    def __init__(self):
        super().__init__(tab_name="Creds Stats")

    def create_report(self, report_data: TrackerState) -> List[str]:
        return self._create_report_using_vars(
            report_data['working_creds_cnt'], report_data["used_creds_cnt"],
            report_data["cur_session_requests"], report_data["mean_session_lifetime"])

    def _create_report_using_vars(self, work_left, used_cnt: int, cur_requests, lifetime):
        return [f"Working creds left: {work_left}",
                f"Already used creds: {used_cnt}",
                f"Made {cur_requests} requests with current creds",
                f"Mean creds lifetime: {lifetime} req"
                ]


class ParseStats(TextStatsWidget):
    def __init__(self):
        super().__init__(tab_name="Parse Stats")

    def create_report(self, report_data: TrackerState) -> List[str]:
        return self._create_report_using_vars(
            report_data['users_parsed'], report_data["errors_cnt"],
            report_data["total_groups"])

    def _create_report_using_vars(self, users_parsed, errors_cnt: int, groups_parsed):
        return [f"Users parsed: {users_parsed}",
                f"Cnt errors: {errors_cnt}",
                f"Total groups parsed (not unique) {groups_parsed}"
                ]

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = ProxyStats()
    widget.resize(800, 600)
    widget.show()

    import sys
    sys.exit(app.exec_())
