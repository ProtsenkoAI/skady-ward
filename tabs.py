from horizontal_tab_bar import HorizontalTabBar
from pages import PagesRetriever
import sys

from PyQt5 import QtWidgets


class Tabs(QtWidgets.QTabWidget):
    def __init__(self, pages_retriever: PagesRetriever):
        super().__init__()
        self.setTabBar(HorizontalTabBar())
        self.setTabPosition(QtWidgets.QTabWidget.West)

        # TODO: add icons
        pages, names = pages_retriever.get_pages_and_names()

        for page, name in zip(pages, names):
            self.addTab(page, name)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Tabs()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
