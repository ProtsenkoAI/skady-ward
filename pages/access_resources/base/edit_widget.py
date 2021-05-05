from abc import ABC, abstractmethod
from PyQt5 import QtWidgets
from typing import List, Callable
from suvec.vk_api_impl.session.records_managing.records_storing import AuthRecordsStorage

from .buttons import SaveButton, CancelButton
from pages.util import AbstractWidgetMeta


class ResourceEditWidget(QtWidgets.QDialog, ABC, metaclass=AbstractWidgetMeta):
    def __init__(self, record, storage: AuthRecordsStorage, edit_finish_callback: Callable, delete_if_cancel=False):
        self.record = record
        self.storage = storage
        self.close_callback = edit_finish_callback

        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        input_names = self.get_input_names()
        inputs_texts = self.get_default_input_values()
        print("inputs_texts", inputs_texts)
        self.inputs = [QtWidgets.QLineEdit(text=text) for text in inputs_texts]

        close_callback = self._close_and_delete if delete_if_cancel else self._close
        layout.addWidget(EditTopBar(record, self.save_record, close_callback))
        for name, inp in zip(input_names, self.inputs):
            layout.addWidget(QtWidgets.QLabel(text=name))
            layout.addWidget(inp)

    def get_input_values(self) -> List[str]:
        return [inp.text() for inp in self.inputs]

    @abstractmethod
    def save_record(self):
        ...

    @abstractmethod
    def get_input_names(self):
        ...

    @abstractmethod
    def get_default_input_values(self):
        ...

    def closeEvent(self, event):
        self._close()
        print("close event")
        super().closeEvent(event)

    def _close(self):
        self.close_callback()
        self.close()

    def _close_and_delete(self):
        self.storage.delete_record(self.record)
        self._close()


class EditTopBar(QtWidgets.QWidget):
    def __init__(self, record, save_callable, close_callable):
        super().__init__()
        layout = QtWidgets.QHBoxLayout()
        self.setLayout(layout)

        layout.addWidget(QtWidgets.QLabel(text=f"ID: {record.obj_id}"))
        layout.addWidget(QtWidgets.QLabel(text=f"Status: {record.status}"))
        layout.addStretch()
        save_button = SaveButton(callback=save_callable)
        close_button = CancelButton(callback=close_callable)
        layout.addWidget(save_button)
        layout.addWidget(close_button)
