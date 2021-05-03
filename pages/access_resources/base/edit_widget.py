from abc import ABC, abstractmethod
from PyQt5 import QtWidgets
from typing import List, Callable

from .buttons import SaveButton, CancelButton
from pages.util import AbstractWidgetMeta


class ResourceEditWidget(QtWidgets.QDialog, ABC, metaclass=AbstractWidgetMeta):
    # TODO: move to base/ and inherit
    def __init__(self, record, storage, edit_finish_callback: Callable):
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

        layout.addWidget(EditTopBar(record, self.save_record, self._close))
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
