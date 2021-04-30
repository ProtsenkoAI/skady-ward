from abc import ABC, abstractmethod, ABCMeta

from .data_trackers import DataTracker
from PyQt5.QtWidgets import QWidget


class MetaABCandQWidget(type(ABC), type(QWidget)):
    ...


class WidgetWithDataTracker(ABC, metaclass=MetaABCandQWidget):
    def __init__(self, data_tracker: DataTracker):
        self.data_tracker = data_tracker
        self.data_tracker.set_callable_to_push_state(self.update_state)

    @abstractmethod
    def update_state(self, state):
        ...

    def get_start_state(self):
        return self.data_tracker.get_start_state()
