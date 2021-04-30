from PyQt5 import QtWidgets, QtCore, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from .widget_with_data_tracker import WidgetWithDataTracker
from .data_trackers.parse_speed_tracker import ParseSpeedState


class ParseSpeedPlot(WidgetWithDataTracker, QtWidgets.QGroupBox):
    # TODO: refactor
    # TODO: customize x-axis
    def __init__(self, tracker, max_plot_points: int = 10):
        WidgetWithDataTracker.__init__(self, tracker)
        QtWidgets.QWidget.__init__(self)

        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        self.canvas = MplCanvas()
        self.canvas.fig.suptitle("Parse Speed")
        layout.addWidget(self.canvas)

        self.current_speed = QtWidgets.QLabel()
        font = QtGui.QFont()
        font.setPointSize(16)
        self.current_speed.setFont(font)
        layout.addWidget(self.current_speed)

        self.max_plot_points = max_plot_points
        self._plot_ref = None

        self.parse_speeds = [self.get_start_state()["speed"]]

        self.setStyleSheet("background: white")

    def update_state(self, state: ParseSpeedState):
        # TODO: needs huge refactor
        self.parse_speeds = (self.parse_speeds + [state["speed"]])[-self.max_plot_points:]
        xdata = list(range(len(self.parse_speeds)))

        if self._plot_ref is None:
            if len(xdata) == self.max_plot_points:
                print("setting")
                plot_refs = self.canvas.axes.plot(xdata, self.parse_speeds, 'r')
                self._plot_ref = plot_refs[0]
        else:
            print("setting", self.parse_speeds)
            self._plot_ref.set_ydata(self.parse_speeds)

        # Trigger the canvas to update and redraw.
        self.canvas.draw()

        mean_speed = sum(self.parse_speeds) / len(self.parse_speeds)

        self.current_speed.setText(f"Current speed: {mean_speed} requests/sec")
        self.current_speed.update()


class MplCanvas(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super().__init__(self.fig)

