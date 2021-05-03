import time
from random import randint
from typing import TypedDict, List, Optional
from suvec.common.events_tracker import EventsTracker
from suvec.common.top_level_types import User, Group
from suvec.common.executing import ErrorObj


class TrackerState(TypedDict):
    parse_speed: List[float]
    cur_session_requests: int
    mean_session_lifetime: Optional[float]
    working_proxies_cnt: Optional[int]
    working_creds_cnt: Optional[int]
    used_proxies_cnt: int
    used_creds_cnt: int
    users_parsed: int
    errors_cnt: int
    total_groups: int


class EventsTrackerWithState(EventsTracker):
    # TODO: add logging
    # TODO: move to suvec
    # TODO: pass user to friends_added and groups_added
    # TODO: need to get working_proxies_cnt and working_creds_cnt at init stage from storages
    # TODO: separate creds session change and proxy session change
    def __init__(self):
        self._sessions_requests_cnt = []
        self._parsed_users: List[User] = []
        self.state = TrackerState(parse_speed=[],
                                  cur_session_requests=0,
                                  mean_session_lifetime=None,
                                  working_proxies_cnt=None,
                                  working_creds_cnt=None,
                                  used_creds_cnt=0,
                                  used_proxies_cnt=0,
                                  users_parsed=0,
                                  errors_cnt=0,
                                  total_groups=0
                                  )
        self.prev_request_time = time.time()
        self.start_loop_time = None

    def get_state(self) -> TrackerState:
        return self.state

    def _request_processed(self):
        self.state["cur_session_requests"] += 1
        self.state["total_groups"] += randint(1, 100)
        if self.state["cur_session_requests"] % 2 == 1:
            self.state["users_parsed"] += 1
        self.prev_request_time = time.time()

    def error_occurred(self, error: ErrorObj, msg: Optional[str] = None):
        self.state["errors_cnt"] += 1

    def message(self, msg: str):
        self._request_processed()

    def skip_user(self, user: User, msg: Optional[str] = None):
        self._request_processed()

    def friends_added(self, friends: List[User]):
        self._request_processed()
        # if user in self._parsed_users:
        #     self.state["users_parsed"] += 1
        # else:
        #     self._parsed_users.append(user)

    def groups_added(self, groups: List[Group]):
        self._request_processed()
        self.state["total_groups"] += len(groups)
        self.state["users_parsed"] += 1
        # if user in self._parsed_users:
        #     self.state["users_parsed"] += 1
        # else:
        #     self._parsed_users.append(user)

    def creds_report(self, creds_left, creds_can_be_used, changed):
        if changed:
            self.state["working_creds_cnt"] = creds_can_be_used
            self.state["used_creds_cnt"] = creds_left - creds_can_be_used

    def proxy_report(self, proxy_left: int, proxy_left_with_ok_state: int, changed):
        if changed:
            self._sessions_requests_cnt.append(self.state["cur_session_requests"])
            self.state["cur_session_requests"] = 0
            self.state["mean_session_lifetime"] = self._mean(self._sessions_requests_cnt)
            self.state["working_proxies_cnt"] = proxy_left_with_ok_state
            self.state["used_proxies_cnt"] = proxy_left - proxy_left_with_ok_state

    def loop_started(self):
        self.start_loop_time = time.time()

    def loop_ended(self):
        time_for_loop = time.time() - self.start_loop_time
        self.state["parse_speed"].append(time_for_loop)
        self.start_loop_time = time.time()

    def _mean(self, lst):
        if len(lst):
            return sum(lst) / len(lst)
        return 0