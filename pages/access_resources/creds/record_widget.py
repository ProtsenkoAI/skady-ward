from PyQt5 import QtWidgets

from ..base.resource_widget import ResourceWidget


class CredsWidget(ResourceWidget):
    def create_edit_button(self) -> QtWidgets.QWidget:
        raise NotImplementedError
