import time
from random import randint
from typing import TypedDict, List, Optional


class TrackerState(TypedDict):
    parse_speed: List[float]
    cur_session_requests: int
    mean_session_lifetime: Optional[float]
    working_proxies_cnt: int
    working_creds_cnt: int
    used_proxies_cnt: int
    used_creds_cnt: int
    users_parsed: int
    errors_cnt: int
    total_groups: int


class EventsTrackerWithState:
    def __init__(self):
        self.state = TrackerState(parse_speed=[0],
                                  cur_session_requests=0,
                                  mean_session_lifetime=None,
                                  working_proxies_cnt=20,
                                  working_creds_cnt=20,
                                  used_creds_cnt=0,
                                  used_proxies_cnt=0,
                                  users_parsed=0,
                                  errors_cnt=0,
                                  total_groups=0
                                  )
        self.prev_request_time = time.time()

    def get_state(self) -> TrackerState:
        return self.state

    def request_processed(self):
        self.state["cur_session_requests"] += 1
        time_for_request = time.time() - self.prev_request_time
        self.state["total_groups"] += randint(1, 100)
        if self.state["cur_session_requests"] % 2 == 1:
            self.state["users_parsed"] += 1
        self.state["parse_speed"].append(1 / time_for_request)
        self.prev_request_time = time.time()


class CrawlRunner:
    def __init__(self, tracker: EventsTrackerWithState, config: dict):
        self.tracker = tracker
        self.is_stopped = False

    def run(self):
        for i in range(10**12):
            if self.is_stopped:
                break
            if i % 5 == 0:
                self.tracker.request_processed()
            time.sleep(0.01)

    def stop(self):
        self.is_stopped = True
