import sys
from PyQt5 import QtWidgets

from pages.dashboard_page.data_trackers import CredsDataTracker
from top_bar import TopBar
from tabs import Tabs


class App(QtWidgets.QWidget):
    # TODO: use QtWidgets.MainWindow
    # TODO: move all consts to consts.py or config
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

    # widget = App()
    from pages.dashboard_page import DashboardPage
    from time import sleep
    from random import randint
    from pages.dashboard_page.stats import ProxyStats, CredsStats, ParseStats
    from pages.dashboard_page.parse_speed_plot import ParseSpeedPlot
    from pages.dashboard_page.data_trackers import CredsDataTracker, ProxyDataTracker, ParseSpeedTracker, ParseDataTracker
    from pages.dashboard_page.data_trackers.parse_speed_tracker import ParseSpeedState

    creds_tracker = CredsDataTracker()
    proxy_tracker = ProxyDataTracker()
    parse_tracker = ParseDataTracker()
    stats_widgets = [
        ProxyStats(proxy_tracker),
        CredsStats(creds_tracker),
        ParseStats(parse_tracker),
    ]

    speed_tracker = ParseSpeedTracker()
    widget = DashboardPage(ParseSpeedPlot(speed_tracker), stats_widgets)
    widget.resize(1000, 520)
    widget.show()
    for i in range(20):
        creds_tracker.update_curr_session_req_cnt(5)
        speed_tracker.push_state(ParseSpeedState(speed=randint(1, 10)))

    sys.exit(app.exec_())
