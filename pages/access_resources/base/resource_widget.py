from PyQt5 import QtWidgets
from abc import ABC, abstractmethod
from typing import Callable

from pages.util import AbstractWidgetMeta
from suvec.vk_api_impl.session.records_managing.consts import ResourceStatus, RESOURCE_OK_STATUS
from .buttons import EditButton, DeleteButton
from .util import qt_color


class ResourceWidget(QtWidgets.QGroupBox, ABC, metaclass=AbstractWidgetMeta):
    # TODO: maybe add annotations for statuses
    def __init__(self, record, storage, width: int = 220):
        super().__init__()
        layout = QtWidgets.QHBoxLayout()
        self.setLayout(layout)
        self.storage = storage
        self.record = record

        rec_id = record.obj_id
        rec_status = record.status

        layout.addWidget(QtWidgets.QLabel(text=f"ID: {rec_id}"))
        layout.addWidget(QtWidgets.QLabel(text=f"Status: {rec_status}"))

        background_color = self._get_bg_color(rec_status)
        self.setStyleSheet(f"background-color: {background_color}")

        layout.addStretch()

        layout.addWidget(EditButton(self._change_edit_flag_call_edit_callback))
        layout.addWidget(DeleteButton(self.delete_callback))

        self.setFixedWidth(width)
        self.is_in_edit_mode = False

    def _change_edit_flag_call_edit_callback(self):
        self.is_in_edit_mode = True
        self.edit_callback(self.edit_finished)

    def edit_finished(self):
        self.is_in_edit_mode = False

    def _get_bg_color(self, status: ResourceStatus) -> str:
        if status == RESOURCE_OK_STATUS:
            return qt_color("B4FFAD")
        return qt_color("FFADAD")

    def delete_callback(self):
        self.storage.delete_record(self.record)

    def get_obj_id(self):
        return self.record.obj_id

    @abstractmethod
    def edit_callback(self, edit_finish_callback: Callable):
        ...
