import sys
from PyQt5 import QtWidgets, QtCore
from main_widget import MainWidget
from crawler_with_tracker_state import BackgroundCrawler


if __name__ == "__main__":
    qt_app = QtWidgets.QApplication([])

    crawler = BackgroundCrawler(config={})

    main_widget = MainWidget(crawler)

    main_widget.resize(800, 480)
    main_widget.show()

    sys.exit(qt_app.exec_())
