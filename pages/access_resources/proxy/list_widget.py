from PyQt5 import QtWidgets

from ..base.list_widget import ResourcesListWidget
from .record_widget import ProxyWidget


class ProxyListWidget(ResourcesListWidget):
    def __init__(self, proxy_storage):
        self.storage = proxy_storage
        super().__init__(proxy_storage, "Proxies")

    def create_record_widget(self, record) -> QtWidgets.QWidget:
        return ProxyWidget(record, self.storage)

    # def create_add_new_resource_widget(self) -> QtWidgets.QWidget:
    #     creator_widget = ProxyCreateWidget(record_created_callback=self.storage.add_record)
    #     return creator_widget
