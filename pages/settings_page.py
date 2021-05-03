# TODO: refactor

from PyQt5 import QtWidgets
from typing import Optional, Tuple, Callable, Dict, Any
from suvec.vk_api_impl.crawl_runner import VkApiCrawlRunner

from background_crawler import BackgroundCrawler


class SettingsPage(QtWidgets.QWidget):
    def __init__(self, crawler_init_kwargs: Dict[str, Any]):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.input_settings = self._get_input_settings()
        crawl_on_off_buttons = CrawlOnOffButtons(crawler_init_kwargs,
                                                 off_callback=self._unlock_settings,
                                                 on_callback=self._lock_settings,
                                                 callable_to_get_crawler_settings=self._get_settings_values)

        layout.addWidget(crawl_on_off_buttons)
        for inp_setting in self.input_settings:
            layout.addWidget(inp_setting)

        layout.addStretch()

    def _lock_settings(self):
        for setting in self.input_settings:
            setting.set_is_locked(True)

    def _unlock_settings(self):
        for setting in self.input_settings:
            setting.set_is_locked(False)

    def _get_settings_values(self) -> Dict[str, Optional[str]]:
        res = {}
        for setting_widg in self.input_settings:
            key, value = setting_widg.get_name_and_value()
            res[key] = value

        return res

    def _get_input_settings(self):
        # TODO: split the module and radd returned typing
        # TODO: set standard values from different place
        res = [InputSetting("start_user_id", "Start user id:", "", input_len=100, val_type=int),
               InputSetting("requester_max_requests_per_crawl_loop", "Max requests per crawl iteration:",
                            "requests", input_len=80, val_type=int, input_text="1000"),
               InputSetting("save_every_n_users_parsed", "Save data every", "users", input_len=80,
                            input_text="100", val_type=int),
               InputSetting("session_request_limit", "Max requests per session (proxy/creds)",
                            "requests", input_len=100, val_type=int, input_text="30000"),
               InputSetting("access_resource_reload_hours", "Time between proxy/creds requests limit and its reuse",
                            "hours", input_len=60, val_type=int, input_text="24"),
               InputSetting("max_users", "Number users needed:", "users", input_len=100, val_type=int,
                            input_text="1000000")]
        return res


class CrawlOnOffButtons(QtWidgets.QWidget):
    def __init__(self, crawler_init_kwargs: Dict[str, Any],
                 callable_to_get_crawler_settings: Callable,
                 on_callback: Optional[Callable] = None,
                 off_callback: Optional[Callable] = None):
        super().__init__()
        self.on_callback = on_callback
        self.off_callback = off_callback

        self.get_crawler_settings = callable_to_get_crawler_settings
        self.crawler_init_kwargs = crawler_init_kwargs
        self.crawler = None
        layout = QtWidgets.QHBoxLayout()
        self.setLayout(layout)

        self.on_button = QtWidgets.QPushButton(text="on")
        self.off_button = QtWidgets.QPushButton(text="off")
        self.on_button.clicked.connect(self._start_parsing)
        self.off_button.clicked.connect(self._stop_parsing)

        layout.addSpacing(120)
        layout.addWidget(QtWidgets.QLabel(text="Run crawling:"))
        layout.addWidget(self.on_button)
        layout.addWidget(self.off_button)
        layout.addStretch()

    def _start_parsing(self):
        self.off_button.setEnabled(True)
        self.on_button.setEnabled(False)

        crawler_kwargs = {}
        crawler_kwargs.update(self.crawler_init_kwargs)
        crawler_kwargs.update(self.get_crawler_settings())
        print("crawler kwargs", crawler_kwargs)
        crawler = VkApiCrawlRunner(**crawler_kwargs)

        # TODO: it's dirty code, need to add method get_tracker() to crawler
        self.crawler = BackgroundCrawler(crawler, crawler_kwargs["events_tracker"])
        self.crawler.run()
        self.on_callback()

    def _stop_parsing(self):
        self.off_button.setEnabled(False)
        self.on_button.setEnabled(True)
        self.crawler.stop()
        self.off_callback()


class InputSetting(QtWidgets.QWidget):
    def __init__(self, internal_name: str, text_before_input: str, text_after_input: str,
                 val_type: type, input_len: int = 100, space_before_setting=120,
                 input_text: Optional[str] = None):
        # TODO: move spacing to constants
        super().__init__()
        layout = QtWidgets.QHBoxLayout()
        self.setLayout(layout)

        text_before = QtWidgets.QLabel(text=text_before_input)
        text_after = QtWidgets.QLabel(text=text_after_input)

        self.input = QtWidgets.QLineEdit()
        self.input.setText(input_text)
        self.input.setFixedWidth(input_len)
        layout.addSpacing(space_before_setting)
        layout.addWidget(text_before)
        layout.addWidget(self.input)
        layout.addWidget(text_after)
        layout.addStretch()
        self.val_type = val_type

        self.internal_name = internal_name

    def get_name_and_value(self) -> Tuple[str, Optional[str]]:
        return self.internal_name, self.val_type(self.input.text())

    def set_is_locked(self, value: bool):
        self.input.setReadOnly(value)
