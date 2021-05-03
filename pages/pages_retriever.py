from .dashboard_page import DashboardPage
from .access_resources import AccessResourcesPage
from .settings_page import SettingsPage
from pages.dashboard_page.stats import ProxyStats, CredsStats, ParseStats
from pages.dashboard_page.parse_speed_plot import ParseSpeedPlot


from typing import Tuple, List
from PyQt5 import QtWidgets


class PagesRetriever:
    def __init__(self, events_tracker, crawler_init_kwargs,
                 creds_list: QtWidgets.QWidget, proxy_list: QtWidgets.QWidget):
        self.pages_with_names = [(self._create_dashboard_page(events_tracker), "Dashboard"),
                                 (AccessResourcesPage(creds_list, proxy_list), "Access Resources"),
                                 (SettingsPage(crawler_init_kwargs), "Settings")
                                 ]

    def get_pages_and_names(self) -> Tuple[List[QtWidgets.QWidget], List[str]]:
        pages, names = list(zip(*self.pages_with_names))
        return pages, names

    def _create_dashboard_page(self, events_tracker):
        stats_widgets = [
            ProxyStats(),
            CredsStats(),
            ParseStats(),
        ]
        page = DashboardPage(events_tracker, ParseSpeedPlot(), stats_widgets)
        return page
