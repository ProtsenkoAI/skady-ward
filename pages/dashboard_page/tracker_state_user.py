from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QWidget

from suvec.common.events_tracking import TrackerState


class MetaABCandQWidget(type(ABC), type(QWidget)):
    ...


class TrackerStateUser(ABC, metaclass=MetaABCandQWidget):
    @abstractmethod
    def update_state(self, tracker_state: TrackerState):
        ...
