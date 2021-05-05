from ..base.create_new_resource_widget import CreateNewResourceWidget
from .record_widget import ProxyEditWidget
from suvec.vk_api_impl.session.records_managing.records import ProxyRecord
from suvec.vk_api_impl.session.records_managing.session_types import Proxy
from suvec.vk_api_impl.session.records_managing.consts import RESOURCE_OK_STATUS

import time


class ProxyCreateWidget(CreateNewResourceWidget):
    def __init__(self, storage, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.storage = storage
        self._edit_widget = None

    def create_record(self, record_id: int):
        record = ProxyRecord(proxy=Proxy.create_empty(), obj_id=record_id, status=RESOURCE_OK_STATUS,
                             status_change_time=time.time())
        self.storage.add_record(record)
        self._edit_widget = ProxyEditWidget(record, self.storage, self._close_edit_widget, delete_if_cancel=True)
        self._edit_widget.show()

    def _close_edit_widget(self):
        self._edit_widget.close()
