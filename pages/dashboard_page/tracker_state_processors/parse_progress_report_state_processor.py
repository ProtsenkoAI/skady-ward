from typing import TypedDict
from .report_state_processor import TrackerStateProcessor, State


class ParseState(TypedDict):
    parsed_users: int
    errors: int
    total_groups_cnt: int


class ParseProgressReportStateProcessor(TrackerStateProcessor):
    # TODO: add interface
    # TODO: add listeners to get data
    def __init__(self):
        super().__init__()
        self.state = ParseState(
            parsed_users=734342,
            errors=135434,
            total_groups_cnt=1000000
            )
