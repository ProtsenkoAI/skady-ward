from ..base.create_new_resource_widget import CreateNewResourceWidget
from .record_widget import CredsEditWidget
from vk_api_impl.session.records_managing.records import CredsRecord
from vk_api_impl.session.records_managing.session_types import Credentials
from vk_api_impl.session.records_managing.consts import RESOURCE_OK_STATUS


class CredsCreateWidget(CreateNewResourceWidget):
    def __init__(self, storage, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.storage = storage
        self._edit_widget = None

    def create_record(self, record_id: int):
        record = CredsRecord(creds=Credentials("", ""), obj_id=record_id, status=RESOURCE_OK_STATUS,
                             time_since_status_change=0)
        self.storage.add_record(record)  # TODO: move to base class
        self._edit_widget = CredsEditWidget(record, self.storage, self._close_edit_widget)
        self._edit_widget.show()

    def _close_edit_widget(self):
        self._edit_widget.close()
