# TODO: split the to base classes and two subdirs: creds/, proxy/

from PyQt5 import QtWidgets, QtGui
from abc import ABC, abstractmethod
from pages.util import AbstractWidgetMeta


class ResourcesListWidget(QtWidgets.QWidget, ABC, metaclass=AbstractWidgetMeta):
    def __init__(self, resources_storage, header_text: str, font_size=16):
        super().__init__()
        self.storage = resources_storage
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        header = QtWidgets.QLabel(text=header_text)
        font = QtGui.QFont()
        font.setPointSize(font_size)
        header.setFont(font)

        layout.addWidget(header)
        # layout.addWidget(self.create_add_new_resource_widget()) # TODO: uncomment

        self.records_widgets = []
        layout.addStretch()
        # TODO: maybe force calling reload_resources() at first?

    def reload_resources(self):
        records = self.storage.get_records()
        records_widgets = [self.create_record_widget(record) for record in records]
        for old_widget in self.records_widgets:
            self.layout().removeWidget(old_widget)

        for new_widget in records_widgets:
            index_before_stretch = self.layout().count() - 1
            self.layout().insertWidget(index_before_stretch, new_widget)
        self.records_widgets = records_widgets  # replacing deleted with added

    @abstractmethod
    def create_record_widget(self, record) -> QtWidgets.QWidget:
        ...

    # @abstractmethod
    # def create_add_new_resource_widget(self) -> QtWidgets.QWidget:
    #     ...
