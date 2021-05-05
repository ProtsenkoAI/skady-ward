from typing import Callable

from ..base.resource_widget import ResourceWidget
from ..base.edit_widget import ResourceEditWidget


class CredsWidget(ResourceWidget):
    def edit_callback(self, edit_finish_callback: Callable):
        self._edit_widg = CredsEditWidget(self.record, self.storage, edit_finish_callback)
        self._edit_widg.show()


class CredsEditWidget(ResourceEditWidget):
    def save_record(self):
        email, password = self.get_input_values()
        self.storage.replace_creds(self.record, email, password)
        self.close()

    def get_input_names(self):
        return ["Email", "Password"]

    def get_default_input_values(self):
        return self.record.creds.email, self.record.creds.password
