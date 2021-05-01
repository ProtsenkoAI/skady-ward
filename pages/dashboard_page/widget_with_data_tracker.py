from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QWidget

from crawler_with_tracker_state import TrackerState


class MetaABCandQWidget(type(ABC), type(QWidget)):
    ...


class WidgetWithDataTracker(ABC, metaclass=MetaABCandQWidget):
    @abstractmethod
    def update_state(self, tracker_state: TrackerState):
        ...
