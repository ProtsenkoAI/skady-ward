from PyQt5 import QtWidgets
from typing import Optional

from pages import PagesRetriever
from pages.access_resources import CredsListWidget, ProxyListWidget
from top_bar import TopBar
from tabs import Tabs

from events_tracker_with_state import EventsTrackerWithState
from suvec.vk_api_impl.session.records_managing.records_storing import ProxyStorage, CredsStorage


class MainWidget(QtWidgets.QWidget):
    # TODO: use QtWidgets.MainWindow
    # TODO: move all consts to consts.py or config
    # TODO: refactor
    def __init__(self, events_tracker: EventsTrackerWithState, proxy_storage: ProxyStorage, creds_storage: CredsStorage,
                 crawler_kwargs: Optional[dict] = None):
        if crawler_kwargs is None:
            crawler_kwargs = {}
        super().__init__()
        layout = QtWidgets.QVBoxLayout()

        top_bar = TopBar(height=46)
        proxy_list_widget = ProxyListWidget(proxy_storage)
        creds_list_widget = CredsListWidget(creds_storage)
        crawler_kwargs.update({"events_tracker": events_tracker,
                               "proxy_storage": proxy_storage,
                               "creds_storage": creds_storage})
        pages_retriever = PagesRetriever(events_tracker=events_tracker,
                                         crawler_init_kwargs=crawler_kwargs,
                                         creds_list=creds_list_widget,
                                         proxy_list=proxy_list_widget)
        self.tabs = Tabs(pages_retriever)

        layout.addWidget(top_bar)
        layout.addWidget(self.tabs)
        self.setLayout(layout)
