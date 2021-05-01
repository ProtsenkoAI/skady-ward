from typing import TypedDict
from .report_state_processor import TrackerStateProcessor
from crawler_with_tracker_state import TrackerState


class CredsState(TypedDict):
    working_creds_cnt: int
    used_creds_cnt: int
    curr_session_req_cnt: int
    mean_creds_lifetime: float


class CredsReportStateProcessor(TrackerStateProcessor):
    # TODO: add interface
    # TODO: add listeners to get data
    def __init__(self):
        super().__init__()
        self.state =

    def update_curr_session_req_cnt(self, cnt=1):
        # TODO: delete
        self.state['curr_session_req_cnt'] += cnt

    def process_tracker_state(self, state: TrackerState) -> CredsState:
        return CredsState(
            working_creds_cnt=state["working_creds_cnt"],
            used_creds_cnt=state["used_creds_cnt"],
            curr_session_req_cnt=state["curr_session_req_cnt"],
            mean_creds_lifetime=state["mean_creds_lifetime"]
        )
