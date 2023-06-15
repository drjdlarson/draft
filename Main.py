import typing
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QStackedLayout,
    QWidget,
    QListWidget,
    QTabWidget, 
    QToolBar,
    QAction,
    QStatusBar,
    QTextEdit
)
from PyQt5.QtGui import QPalette, QColor
from pyqtgraph import PlotWidget
import pyqtgraph
import openvsp as vsp
from Prop import DynamicProp

# Main Window Subclass: defines main layout 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DRAFT - Design Resource for Airborne Flight Technology")
        self.setMinimumSize(1000,600)

        self.PropSection = DynamicProp.DynamicPropWindow()

        layout = QHBoxLayout()

        layout.addWidget(self.PropSection)

        # Setting the overall layout as the central widget
        overall = QWidget()
        overall.setLayout(layout)
        self.setCentralWidget(overall)

# Using this if statement to ensure that the code will not run if called by another file
if __name__ == "__main__":
    # Call the application
    app = QApplication([])

    # Open the window
    window = MainWindow()
    window.show()

    # Start the app
    app.exec()

