from .dashboard_page import DashboardPage
from .access_resources_page import AccessResourcesPage
from .settings_page import SettingsPage
from pages.dashboard_page.stats import ProxyStats, CredsStats, ParseStats
from pages.dashboard_page.parse_speed_plot import ParseSpeedPlot


from typing import Tuple, List
from PyQt5 import QtWidgets


class PagesRetriever:
    def __init__(self, crawler_with_tracker_state):
        self.pages_with_names = [(self._create_dashboard_page(crawler_with_tracker_state), "Dashboard"),
                                 (AccessResourcesPage(), "Access Resources"),
                                 (SettingsPage(crawler_with_tracker_state), "Settings")
                                 ]

    def get_pages_and_names(self) -> Tuple[List[QtWidgets.QWidget], List[str]]:
        pages, names = list(zip(*self.pages_with_names))
        return pages, names

    def _create_dashboard_page(self, crawler_with_tracker_state):
        stats_widgets = [
            ProxyStats(),
            CredsStats(),
            ParseStats(),
        ]
        page = DashboardPage(crawler_with_tracker_state, ParseSpeedPlot(), stats_widgets)
        return page
