from PyQt5 import QtWidgets, QtGui
from abc import ABC, abstractmethod

from pages.util import AbstractWidgetMeta


class ResourcesListWidget(QtWidgets.QWidget, ABC, metaclass=AbstractWidgetMeta):
    """Contains header and function to draw resources. A parent is responsible for calling draw function."""
    def __init__(self, resources_storage, header_text: str, font_size=16):
        super().__init__()
        self.storage = resources_storage
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self._max_record_id = -1

        header = QtWidgets.QLabel(text=header_text)
        font = QtGui.QFont()
        font.setPointSize(font_size)
        header.setFont(font)

        layout.addWidget(header)
        layout.addWidget(self.create_add_new_resource_widget())

        self.records_widgets = []
        layout.addStretch()
        self.reload_resources()  # at the start forcing to draw resources

    def reload_resources(self):
        records = self.storage.get_records()
        records_widgets = [self.create_record_widget(record) for record in records]
        for old_widget in self.records_widgets:
            if old_widget.is_in_edit_mode:
                return  # if in edit mode, stop updating
            self.layout().removeWidget(old_widget)

        for new_widget in records_widgets:
            self._max_record_id = max(new_widget.get_obj_id(), self._max_record_id)
            index_before_stretch = self.layout().count() - 1
            self.layout().insertWidget(index_before_stretch, new_widget)
        self.records_widgets = records_widgets  # replacing deleted with added

    def get_max_record_id(self) -> int:
        return self._max_record_id

    @abstractmethod
    def create_record_widget(self, record) -> QtWidgets.QWidget:
        ...

    @abstractmethod
    def create_add_new_resource_widget(self) -> QtWidgets.QWidget:
        ...
