from typing import TypedDict
from .data_tracker import DataTracker, State


class CredsState(TypedDict):
    working_creds_cnt: int
    used_creds_cnt: int
    curr_session_req_cnt: int
    mean_creds_lifetime: float


class CredsDataTracker(DataTracker):
    # TODO: add interface
    # TODO: add listeners to get data
    def __init__(self):
        super().__init__()
        self.state = CredsState(
            working_creds_cnt=7,
            used_creds_cnt=13,
            curr_session_req_cnt=30000,
            mean_creds_lifetime=29999
            )

    def update_curr_session_req_cnt(self, cnt=1):
        # TODO: delete
        self.state['curr_session_req_cnt'] += cnt
        self.push_state(self.state)

    def get_start_state(self) -> State:
        return self.state
