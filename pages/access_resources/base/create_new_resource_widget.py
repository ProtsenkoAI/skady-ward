from abc import ABC, abstractmethod
from PyQt5 import QtWidgets, QtCore
from typing import Callable
from pages.util import AbstractWidgetMeta
from .util import qt_color
from .buttons import AddButton


class CreateNewResourceWidget(QtWidgets.QGroupBox, ABC, metaclass=AbstractWidgetMeta):
    def __init__(self, func_to_get_max_record_id: Callable, width: int = 220, background_hex="efefef", height=30):
        super().__init__()
        # TODO: remove ugly qgroupbox borders
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        # self.setFlat(True)
        # layout.setAlignment(QtCore.Qt.Alignment(QtCore.Qt.AlignmentFlag.AlignCenter))
        self.setLayout(layout)
        self.get_max_record_id = func_to_get_max_record_id

        self.setFixedWidth(width)
        self.setFixedHeight(height)
        background_color = qt_color(background_hex)
        self.setStyleSheet(f"background-color: {background_color}")

        create_resource_button = AddButton(self._call_create_record)
        layout.addWidget(create_resource_button)

    def _call_create_record(self):
        self.create_record(self.get_max_record_id() + 1)



    @abstractmethod
    def create_record(self, record_id: int):
        ...
