from ..base.resource_widget import ResourceWidget
from ..base.edit_widget import ResourceEditWidget


class CredsWidget(ResourceWidget):
    def edit_callback(self):
        # TODO: refactor the edit_finished thingy here (inheritor shouldn't know about it)
        self._edit_widg = CredsEditWidget(self.record, self.storage, self.edit_finished)
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
