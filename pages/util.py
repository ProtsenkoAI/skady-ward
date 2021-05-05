from abc import ABC
from PyQt5 import QtWidgets


class AbstractWidgetMeta(type(ABC), type(QtWidgets.QWidget)):
    ...
