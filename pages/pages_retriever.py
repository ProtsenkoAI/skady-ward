from .dashboard_page import DashboardPage
from .access_resources_page import AccessResourcesPage
from .settings_page import SettingsPage
from pages.dashboard_page.tracker_state_processors.parsing_speed_report_state_processor import ParseSpeedState
from pages.dashboard_page.tracker_state_processors import CredsReportStateProcessor, ProxyReportStateProcessor, ParseSpeedReportStateProcessor, ParseProgressReportStateProcessor
from pages.dashboard_page.stats import ProxyStats, CredsStats, ParseStats
from pages.dashboard_page.parse_speed_plot import ParseSpeedPlot


from typing import Tuple, List
from PyQt5 import QtWidgets


class PagesRetriever:
    def __init__(self, bg_crawler):
        self.pages_with_names = [(self._create_dashboard_page(bg_crawler), "Dashboard"),
                                 (AccessResourcesPage(), "Access Resources"),
                                 (SettingsPage(bg_crawler), "Settings")
                                 ]

    def get_pages_and_names(self) -> Tuple[List[QtWidgets.QWidget], List[str]]:
        pages, names = list(zip(*self.pages_with_names))
        return pages, names

    def _create_dashboard_page(self, bg_crawler):
        stats_widgets = [
            ProxyStats(ProxyReportStateProcessor()),
            CredsStats(CredsReportStateProcessor()),
            ParseStats(ParseProgressReportStateProcessor()),
        ]
        page = DashboardPage(ParseSpeedPlot(ParseSpeedReportStateProcessor()), stats_widgets, bg_crawler)
        return page
