from PyQt5 import QtWidgets
from abc import abstractmethod
from typing import List

from .data_trackers.proxy_data_tracker import ProxyState
from .data_trackers.creds_data_tracker import CredsState
from .widget_with_data_tracker import WidgetWithDataTracker

# TODO: setWordWrap to auto-split lines if they are too long
# TODO: apply listeners/notifiers to track stats

print(type(WidgetWithDataTracker), type(QtWidgets.QGroupBox))


# class MultiMetaClass(type(QtWidgets.QGroupBox), type(WidgetWithDataTracker)):
#     # TODO: think about it if it'll work at all
#     ...


class TextStatsWidget(WidgetWithDataTracker, QtWidgets.QGroupBox):
    def __init__(self, tab_name: str, data_tracker):

        WidgetWithDataTracker.__init__(self, data_tracker)
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

    def update_state(self, state):
        new_stats_lines = self.create_report(state)
        for line, line_container in zip(new_stats_lines, self.line_containers):
            line_container.setText(line)
            line_container.update()

    @abstractmethod
    def create_report(self, state) -> List[str]:
        ...


class ProxyStats(TextStatsWidget):
    def __init__(self, data_tracker):
        super().__init__(tab_name="Proxy Stats", data_tracker=data_tracker)

    def create_report(self, state: ProxyState) -> List[str]:
        return [f"{key}: {value}" for key, value in state.items()]


class CredsStats(TextStatsWidget):
    def __init__(self, data_tracker):
        super().__init__(tab_name="Creds Stats", data_tracker=data_tracker)

    def create_report(self, state: CredsState) -> List[str]:
        return [f"{key}: {value}" for key, value in state.items()]


class ParseStats(TextStatsWidget):
    def __init__(self, data_tracker):
        super().__init__(tab_name="Parse Stats", data_tracker=data_tracker)

    def create_report(self, state) -> List[str]:
        return [f"{key}: {value}" for key, value in state.items()]


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = ProxyStats(None)
    widget.resize(800, 600)
    widget.show()

    import sys
    sys.exit(app.exec_())
