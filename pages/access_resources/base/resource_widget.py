from PyQt5 import QtWidgets, QtGui
from abc import ABC, abstractmethod
from PIL import ImageColor

from pages.util import AbstractWidgetMeta
from vk_api_impl.session.records_managing.consts import ResourceStatus, RESOURCE_OK_STATUS


class ResourceWidget(QtWidgets.QGroupBox, ABC, metaclass=AbstractWidgetMeta):
    # TODO: change color if status is not ok
    # TODO: maybe add annotations for statuses
    def __init__(self, record, storage, width: int = 220):
        super().__init__()
        layout = QtWidgets.QHBoxLayout()
        self.setLayout(layout)
        self.storage = storage
        self.record = record

        rec_id = record.obj_id
        rec_status = record.status

        layout.addWidget(QtWidgets.QLabel(text=f"ID: {rec_id}"))
        layout.addWidget(QtWidgets.QLabel(text=f"Status: {rec_status}"))

        background_color = self._get_bg_color(rec_status)
        self.setStyleSheet(f"background-color: {background_color}")

        layout.addStretch()

        # TODO: uncomment
        # layout.addWidget(self.create_edit_button())
        layout.addWidget(self.create_delete_button())

        self.setFixedWidth(width)

    def _get_bg_color(self, status: ResourceStatus) -> str:
        if status == RESOURCE_OK_STATUS:
            return self._qt_color("B4FFAD")
        return self._qt_color("FFADAD")

    # @abstractmethod
    # def create_edit_button(self) -> QtWidgets.QWidget:
    #     ...

    def create_delete_button(self) -> QtWidgets.QWidget:
        return DeleteButton(self.record, self.storage)

    def _qt_color(self, hex_color: str):
        color_tuple = ImageColor.getcolor(f"#{hex_color}", "RGB")
        stylized_qt_color_string = f"rgb{color_tuple}"
        return stylized_qt_color_string


class DeleteButton(QtWidgets.QPushButton):
    def __init__(self, record, storage, icon_path="/home/gldsn/Projects/skady-ward/resources/icons/delete.png",
                 size: int = 20):
        super().__init__()
        self.storage = storage
        self.record = record

        icon_pixmap = QtGui.QPixmap(icon_path)
        icon_resized = icon_pixmap.scaled(size, size)
        self.setIcon(QtGui.QIcon(icon_resized))
        self.clicked.connect(self._delete_record)

    def _delete_record(self):
        print("trying to delete record")
        self.storage.delete_record(self.record)
