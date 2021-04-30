from abc import ABC, abstractmethod
from typing import Callable

State = dict


class DataTracker(ABC):
    def __init__(self):
        self.push_state_callable = None

    def set_callable_to_push_state(self, call: Callable):
        self.push_state_callable = call

    def push_state(self, state: State):
        self.push_state_callable(state)

    @abstractmethod
    def get_start_state(self) -> State:
        ...
