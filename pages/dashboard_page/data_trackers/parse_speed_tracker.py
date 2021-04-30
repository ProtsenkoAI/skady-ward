from typing import TypedDict

from .data_tracker import DataTracker


class ParseSpeedState(TypedDict):
    speed: float


class ParseSpeedTracker(DataTracker):
    # TODO: listen to every parsed users and calculate speed
    def __init__(self):
        super().__init__()
        self.state = ParseSpeedState(speed=3.9)

    def get_start_state(self) -> ParseSpeedState:
        return self.state
