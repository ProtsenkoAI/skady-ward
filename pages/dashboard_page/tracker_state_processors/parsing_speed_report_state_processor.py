from typing import TypedDict

from .report_state_processor import TrackerStateProcessor


class ParseSpeedState(TypedDict):
    speed: float


class ParseSpeedReportStateProcessor(TrackerStateProcessor):
    # TODO: listen to every parsed users and calculate speed
    def __init__(self):
        super().__init__()
        self.state = ParseSpeedState(speed=3.9)

    def speed_updated(self, new_speed):
        # TODO: replace with listener method
        self.state["speed"] = new_speed
        self.push_state_callable(self.state)
