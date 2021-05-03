from PyQt5 import QtWidgets

from ..base.list_widget import ResourcesListWidget
from .creds_create_widget import CredsCreateWidget
from .record_widget import CredsWidget


class CredsListWidget(ResourcesListWidget):
    def __init__(self, creds_storage):
        self.storage = creds_storage
        super().__init__(creds_storage, "Credentials")

    def create_record_widget(self, record) -> QtWidgets.QWidget:
        return CredsWidget(record, self.storage)

    def create_add_new_resource_widget(self) -> QtWidgets.QWidget:
        creator_widget = CredsCreateWidget(self.storage, self.get_max_record_id)
        return creator_widget
