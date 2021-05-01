from PyQt5 import QtWidgets


class SettingsPage(QtWidgets.QWidget):
    def __init__(self, crawler):
        super().__init__(self)
        self.crawler = crawler
