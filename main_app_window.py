import sys
from PyQt5 import QtWidgets


from pages import PagesRetriever

from pages.dashboard_page import DashboardPage
from top_bar import TopBar
from tabs import Tabs


class MainWidget(QtWidgets.QWidget):
    # TODO: use QtWidgets.MainWindow
    # TODO: move all consts to consts.py or config
    # TODO: refactor
    def __init__(self, bg_crawler, creds_data_tracker, proxy_data_tracker, parse_data_tracker, parse_speed_tracker):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()

        top_bar = TopBar(height=46)
        pages_retriever = PagesRetriever(bg_crawler)
        tabs = Tabs(pages_retriever)

        layout.addWidget(top_bar)
        layout.addWidget(tabs)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    # widget = App()
    from time import sleep
    from random import randint
    widget = MainAppWindow(CredsDataTracker(), ProxyDataTracker(), ParseDataTracker(), ParseSpeedTracker())

    widget.resize(1000, 520)
    widget.show()
    sys.exit(app.exec_())
