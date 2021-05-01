from PyQt5 import QtWidgets, QtCore, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from crawler_with_tracker_state import TrackerState
from .tracker_state_user import TrackerStateUser


class ParseSpeedPlot(TrackerStateUser, QtWidgets.QGroupBox):
    # TODO: refactor
    # TODO: customize x-axis
    def __init__(self, max_plot_points: int = 100):
        QtWidgets.QWidget.__init__(self)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        self.canvas = MplCanvas()
        self.canvas.fig.suptitle("Parse Speed")
        layout.addWidget(self.canvas)

        self.current_speed = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_speed.setFont(font)
        layout.addWidget(self.current_speed)

        self.max_plot_points = max_plot_points
        self._plot_ref = None

        self.setStyleSheet("background: white")

    def update_state(self, tracker_state: TrackerState):
        # TODO: needs huge refactor
        parse_speeds = (tracker_state["parse_speed"])[-self.max_plot_points:]

        if self._plot_ref is None:
            if len(parse_speeds) >= self.max_plot_points:
                xdata = list(range(len(parse_speeds)))
                plot_refs = self.canvas.axes.plot(xdata, parse_speeds, 'r')
                self._plot_ref = plot_refs[0]
        else:
            self.canvas.fig.axes[0].set_ylim(min(parse_speeds) - 1, max(parse_speeds) + 1)
            self._plot_ref.set_ydata(parse_speeds)

        mean_speed = sum(parse_speeds) / len(parse_speeds)
        mean_speed_formatted = "{:10.4f}".format(mean_speed)

        self.current_speed.setText(f"Mean speed: {mean_speed_formatted} requests/sec")
        self.current_speed.update()

        self.canvas.draw()


class MplCanvas(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)

