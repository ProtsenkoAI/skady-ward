from PyQt5 import QtWidgets

from ..base.list_widget import ResourcesListWidget
from .record_widget import CredsWidget


class CredsListWidget(ResourcesListWidget):
    def __init__(self, creds_storage):
        self.storage = creds_storage
        super().__init__(creds_storage, "Credentials")

    def create_record_widget(self, record) -> QtWidgets.QWidget:
        return CredsWidget(record, self.storage)

    # def create_add_new_resource_widget(self) -> QtWidgets.QWidget:
    #     creator_widget = CredsCreateWidget(record_created_callback=self.storage.add_record)
    #     return creator_widget
