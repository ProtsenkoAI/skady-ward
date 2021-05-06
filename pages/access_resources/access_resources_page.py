from PyQt5 import QtWidgets, QtCore, QtGui
from typing import List

from .base import ResourcesListWidget
from .creds import CredsListWidget
from .proxy import ProxyListWidget


class AccessResourcesPage(QtWidgets.QWidget):
    def __init__(self, creds: CredsListWidget, proxies: ProxyListWidget):
        super().__init__()
        layout = QtWidgets.QHBoxLayout()
        self.setLayout(layout)

        self.resources_list_widgets: List[ResourcesListWidget] = [creds, proxies]

        layout.addStretch()
        layout.addWidget(self._add_vertical_scroll(creds))
        layout.addWidget(self._add_vertical_scroll(proxies))
        layout.addStretch()

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self._update_resources)
        self.timer.start(2000)

    def _add_vertical_scroll(self, widget: QtWidgets.QWidget, height: int = 400) -> QtWidgets.QWidget:
        scroll = QtWidgets.QScrollArea()
        scroll.setWidget(widget)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(height)
        return scroll

    def _update_resources(self):
        for widget in self.resources_list_widgets:
            widget.reload_resources()
