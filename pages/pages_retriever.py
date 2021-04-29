from .dashboard_page import DashboardPage
from .access_resources_page import AccessResourcesPage
from .settings_page import SettingsPage


from typing import Tuple, List
from PyQt5 import QtWidgets


class PagesRetriever:
    def __init__(self):
        self.pages_with_names = [(DashboardPage(), "Dashboard"),
                                 (AccessResourcesPage(), "Access Resources"),
                                 (SettingsPage(), "Settings")
                                 ]

    def get_pages_and_names(self) -> Tuple[List[QtWidgets.QWidget], List[str]]:
        pages, names = list(zip(*self.pages_with_names))
        return pages, names
