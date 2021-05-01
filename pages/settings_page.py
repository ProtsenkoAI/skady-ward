from PyQt5 import QtWidgets
from typing import Optional, Tuple, Callable, List


class SettingsPage(QtWidgets.QWidget):
    def __init__(self, crawler):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        crawl_on_off_buttons = CrawlOnOffButtons(crawler,
                                                 off_callback=self._unlock_settings,
                                                 on_callback=self._lock_settings)
        self.input_settings = self._get_input_settings()

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

    def _get_input_settings(self):
        # TODO: add return typing
        res = [InputSetting("start_user_id", "Start user id:", "", input_len=100),
               InputSetting("max_requests_per_iter", "Max requests per crawl iteration:",
                            "requests", input_len=80), InputSetting("save_data_every", "Save data every",
                                                                    "users", input_len=80),
               InputSetting("max_session_requests", "Max requests per session (proxy/creds)",
                            "requests", input_len=100),
               InputSetting("record_reload_time", "Time between proxy/creds requests limit and its reuse",
                            "hours", input_len=60), InputSetting("max_users", "Number users needed:",
                                                                 "users", input_len=100)]
        return res


class CrawlOnOffButtons(QtWidgets.QWidget):
    def __init__(self, crawler, on_callback: Optional[Callable] = None, off_callback: Optional[Callable] = None):
        super().__init__()
        self.on_callback = on_callback
        self.off_callback = off_callback

        self.crawler = crawler
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
        self.crawler.run()
        self.on_callback()

    def _stop_parsing(self):
        self.off_button.setEnabled(False)
        self.on_button.setEnabled(True)
        self.crawler.stop()
        self.off_callback()


class InputSetting(QtWidgets.QWidget):
    def __init__(self, internal_name: str, text_before_input: str, text_after_input: str,
                 input_len: int = 100, space_before_setting=120):
        # TODO: move spacing to constants
        super().__init__()
        layout = QtWidgets.QHBoxLayout()
        self.setLayout(layout)

        text_before = QtWidgets.QLabel(text=text_before_input)
        text_after = QtWidgets.QLabel(text=text_after_input)

        self.input = QtWidgets.QLineEdit()
        self.input.setFixedWidth(input_len)
        layout.addSpacing(space_before_setting)
        layout.addWidget(text_before)
        layout.addWidget(self.input)
        layout.addWidget(text_after)
        layout.addStretch()

        self.internal_name = internal_name

    def get_value(self) -> Tuple[str, Optional[str]]:
        if self.input.isModified():
            return self.internal_name, self.input.text()
        return self.internal_name, None

    def set_is_locked(self, value: bool):
        self.input.setReadOnly(value)
