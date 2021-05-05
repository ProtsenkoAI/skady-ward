from typing import Callable

from ..base.resource_widget import ResourceWidget
from ..base.edit_widget import ResourceEditWidget


class ProxyWidget(ResourceWidget):
    def edit_callback(self, edit_finish_callback: Callable):
        self._edit_widget = ProxyEditWidget(self.record, self.storage, edit_finish_callback)
        self._edit_widget.show()
        print("showed edit widget")


class ProxyEditWidget(ResourceEditWidget):
    def save_record(self):
        address, protocols_str = self.get_input_values()
        self.storage.replace_proxy(self.record, address, protocols_str)
        self.close()

    def get_input_names(self):
        return ["address and port", "protocols (example: http,https,ftp)"]

    def get_default_input_values(self):
        return self.record.proxy.address, ",".join(self.record.proxy.protocols)
