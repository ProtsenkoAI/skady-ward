from typing import TypedDict
from .data_tracker import DataTracker, State


class ParseState(TypedDict):
    parsed_users: int
    errors: int
    total_groups_cnt: int


class ParseDataTracker(DataTracker):
    # TODO: add interface
    # TODO: add listeners to get data
    def __init__(self):
        super().__init__()
        self.state = ParseState(
            parsed_users=734342,
            errors=135434,
            total_groups_cnt=1000000
            )

    def get_start_state(self) -> State:
        return self.state
