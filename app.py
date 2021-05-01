import sys
from random import randint
from time import sleep
from PyQt5 import QtWidgets, QtCore
from main_app_window import MainWidget
from pages.dashboard_page.tracker_state_processors import (CredsReportStateProcessor, ProxyReportStateProcessor, ParseProgressReportStateProcessor,
                                                           ParseSpeedReportStateProcessor)
from crawler_with_tracker_state import CrawlerWithTrackerState
import threading


if __name__ == "__main__":
    parse_speed_tracker = ParseSpeedReportStateProcessor()

    qt_app = QtWidgets.QApplication([])

    crawler = CrawlerWithTrackerState(config={})

    main_widget = MainWidget(crawler,
                             CredsReportStateProcessor(),
                             ProxyReportStateProcessor(),
                             ParseProgressReportStateProcessor(),
                             parse_speed_tracker)

    main_widget.resize(800, 480)
    main_widget.show()

    sys.exit(qt_app.exec_())
