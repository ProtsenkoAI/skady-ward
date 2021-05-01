from PyQt5 import QtWidgets



class SettingsPage(QtWidgets.QWidget):
    def __init__(self, crawler):
        super().__init__()
        self.crawler = crawler
        print("crawler", crawler)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        self.on_button = QtWidgets.QPushButton(text="on")
        self.on_button.clicked.connect(self._start_parsing)
        self.off_button = QtWidgets.QPushButton(text="off")
        self.off_button.clicked.connect(self._stop_parsing)

        layout.addWidget(self.on_button)
        layout.addWidget(self.off_button)

    def _start_parsing(self):
        self.off_button.setEnabled(True)
        self.on_button.setEnabled(False)
        self.crawler.run()

    def _stop_parsing(self):
        self.off_button.setEnabled(False)
        self.on_button.setEnabled(True)
        self.crawler.stop()
