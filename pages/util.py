from abc import ABC
from PyQt5 import QtWidgets


class AbstractWidgetMeta(type(ABC), type(QtWidgets.QWidget)):
    # TODO: maybe pick out to module with AbstractWidget class
    ...
