from abc import ABC, abstractmethod

from crawler_with_tracker_state import TrackerState

State = dict


class TrackerStateProcessor(ABC):
    def __init__(self):
        self.push_state_callable = None

    @abstractmethod
    def process_tracker_state(self, state: TrackerState) -> State:
        ...
