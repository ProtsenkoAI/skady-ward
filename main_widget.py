import sys
from PyQt5 import QtWidgets


from pages import PagesRetriever
from pages.access_resources import CredsListWidget, ProxyListWidget

from top_bar import TopBar
from tabs import Tabs


class MainWidget(QtWidgets.QWidget):
    # TODO: use QtWidgets.MainWindow
    # TODO: move all consts to consts.py or config
    # TODO: refactor
    def __init__(self, crawler_with_tracker_state, proxy_storage, creds_storage):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()

        top_bar = TopBar(height=46)
        proxy_list_widget = ProxyListWidget(proxy_storage)
        creds_list_widget = CredsListWidget(creds_storage)
        pages_retriever = PagesRetriever(crawler_with_tracker_state, creds_list_widget, proxy_list_widget)
        self.tabs = Tabs(pages_retriever)

        layout.addWidget(top_bar)
        layout.addWidget(self.tabs)
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
