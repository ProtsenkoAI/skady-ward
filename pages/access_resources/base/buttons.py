from typing import Callable
from PyQt5 import QtWidgets, QtGui, QtCore
import os

base_icons_path = "/home/gldsn/Projects/skady-ward/resources/icons/"


def join_icon_file_name(file_name):
    return os.path.join(base_icons_path, file_name)


class ButtonWithIcon(QtWidgets.QPushButton):
    def __init__(self, callback: Callable, icon_path,
                 size: int = 20):
        super().__init__()

        icon_pixmap = QtGui.QPixmap(icon_path)
        icon_resized = icon_pixmap.scaled(size, size)
        self.setIcon(QtGui.QIcon(icon_resized))
        self.setFixedSize(QtCore.QSize(size, size))
        self.clicked.connect(callback)


class EditButton(ButtonWithIcon):
    def __init__(self, callback: Callable, size: int = 20):
        super().__init__(callback, icon_path=join_icon_file_name("edit.png"),
                         size=size)


class DeleteButton(ButtonWithIcon):
    def __init__(self, callback: Callable, size: int = 20):
        super().__init__(callback, icon_path=join_icon_file_name("delete.png"),
                         size=size)


class SaveButton(ButtonWithIcon):
    def __init__(self, callback: Callable, size: int = 24):
        super().__init__(callback, icon_path=join_icon_file_name("check.png"),
                         size=size)


class CancelButton(ButtonWithIcon):
    def __init__(self, callback: Callable, size: int = 24):
        super().__init__(callback, icon_path=join_icon_file_name("cancel.png"),
                         size=size)


class AddButton(ButtonWithIcon):
    def __init__(self, callback: Callable, size: int = 24):
        super().__init__(callback, icon_path=join_icon_file_name("plus.png"),
                         size=size)
