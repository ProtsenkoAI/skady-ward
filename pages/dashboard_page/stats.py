from PyQt5 import QtWidgets
from abc import abstractmethod
from typing import List

from .tracker_state_processors.proxy_report_state_processor import ProxyState
from .tracker_state_processors.creds_report_state_processor import CredsState
from .widget_with_data_tracker import WidgetWithDataTracker
from crawler_with_tracker_state import TrackerState

# TODO: setWordWrap to auto-split lines if they are too long
# TODO: apply listeners/notifiers to track stats

print(type(WidgetWithDataTracker), type(QtWidgets.QGroupBox))


class TextStatsWidget(WidgetWithDataTracker, QtWidgets.QGroupBox):
    def __init__(self, tab_name: str, report_data_processor):
        self.report_data_processor = report_data_processor
        QtWidgets.QGroupBox.__init__(self)

        self.setTitle(tab_name)
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        start_state = self.get_start_state()
        report_lines = self.create_report(start_state)
        self.line_containers = []

        for line in report_lines:
            line_cont = QtWidgets.QLabel()
            line_cont.setText(line)
            layout.addWidget(line_cont)
            self.line_containers.append(line_cont)

    def update_state(self, tracker_state: TrackerState):
        report_data = self.report_data_processor.process_tracker_state(tracker_state)
        new_stats_lines = self.create_report(report_data)
        for line, line_container in zip(new_stats_lines, self.line_containers):
            line_container.setText(line)
            line_container.update()

    @abstractmethod
    def create_report(self, report_data) -> List[str]:
        ...


class ProxyStats(TextStatsWidget):
    def __init__(self, report_data_processor):
        super().__init__(tab_name="Proxy Stats", report_data_processor=report_data_processor)

    def create_report(self, report_data: ProxyState) -> List[str]:
        return [f"{key}: {value}" for key, value in report_data.items()]


class CredsStats(TextStatsWidget):
    def __init__(self, report_data_processor):
        super().__init__(tab_name="Creds Stats", report_data_processor=report_data_processor)

    def create_report(self, report_data: CredsState) -> List[str]:
        return [f"{key}: {value}" for key, value in report_data.items()]


class ParseStats(TextStatsWidget):
    def __init__(self, report_data_processor):
        super().__init__(tab_name="Parse Stats", report_data_processor=report_data_processor)

    def create_report(self, report_data) -> List[str]:
        return [f"{key}: {value}" for key, value in report_data.items()]


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = ProxyStats(None)
    widget.resize(800, 600)
    widget.show()

    import sys
    sys.exit(app.exec_())
