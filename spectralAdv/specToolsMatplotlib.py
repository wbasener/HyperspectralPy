'''
This file contains custom modified version of classes from Matplotlib
'''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import matplotlib
USE_PYQT5 = True
USE_PYSIDE = False

if not USE_PYQT5:
    if USE_PYSIDE:
        matplotlib.rcParams['backend.qt4'] = 'PySide'

    from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

    try:
        from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
    except ImportError:
        from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
else:
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure


class MatplotlibWidgetBottomToolbar(QWidget):
    """
    Extends the MatplotlibWidget to a class that has the toolbar
    located on the bottom of the GUI.

    Implements a Matplotlib figure inside a QWidget.
    Use getFigure() and redraw() to interact with matplotlib.

    Example::

        mw = MatplotlibWidget()
        subplot = mw.getFigure().add_subplot(111)
        subplot.plot(x,y)
        mw.draw()
    """

    def __init__(self, size=(5.0, 4.0), dpi=100):
        QWidget.__init__(self)
        self.fig = Figure(size, dpi=dpi)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.hbox = QVBoxLayout()
        self.hbox.addWidget(self.canvas)
        self.hbox.addWidget(self.toolbar)

        self.setLayout(self.hbox)

    def getFigure(self):
        return self.fig

    def draw(self):
        self.canvas.draw()
        self.fig.tight_layout()
