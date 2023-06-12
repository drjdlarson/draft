from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QListWidget,
    QAbstractItemView,
    QStackedWidget)
import pyqtgraph 
from pyqtgraph import PlotDataItem

class Graph(QMainWindow):
    def __init__(self):
        super().__init__()

        # Define layouts
        layoutRight = QVBoxLayout()
        layout = QHBoxLayout()

        # Define Widgets
        self.bottom_label = QStackedWidget()

        self.dynamic_menu = QComboBox()
        self.dynamic_menu.addItems(['Advanced Ratio (Dynamic)','Velocity (Dynamic)'])
        self.RPM_dd = QComboBox()
        self.RPM_label = QLabel("RPM: ")
        dynamic_layout = QVBoxLayout()
        dynamic_layout.addWidget(self.dynamic_menu)
        dynamic_layout.addWidget(self.RPM_label)
        dynamic_layout.addWidget(self.RPM_dd)
        self.RPM_label.hide()
        self.RPM_dd.hide()
        self.dynamic_widget = QWidget()
        self.dynamic_widget.setLayout(dynamic_layout)
        
        self.bottom_label.addWidget(self.dynamic_widget)
        static_label = QLabel("RPM (Static)")
        static_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bottom_label.addWidget(static_label)

        self.graphContainer = pyqtgraph.PlotWidget()
        self.legend = pyqtgraph.LegendItem(offset=(50,50))
        self.legend.setParentItem(self.graphContainer.plotItem)
        self.legend.setLabelTextColor(pyqtgraph.mkColor('w'))
        self.legend.setPen(pyqtgraph.mkPen(pyqtgraph.mkColor('w')))

        self.left_label = QListWidget()
        self.left_label.addItems(['Thrust','Thrust Coefficient','Power','Power Coefficient','Efficiency','Torque'])
        self.left_label.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.left_label.setFixedWidth(120)

        # Add to layouts
        layout.addWidget(self.left_label)

        layoutRight.addWidget(self.graphContainer)
        layoutRight.addWidget(self.bottom_label)

        layout.addLayout(layoutRight)

        # Setting overall layout
        self.Main = QWidget()
        self.Main.setLayout(layout)
        self.setCentralWidget(self.Main)

        # Connections
        self.dynamic_menu.currentIndexChanged.connect(self.DynamicModeSwap)

    def DynamicModeSwap(self,i):
        if i == 0:
            self.RPM_dd.hide()
            self.RPM_label.hide()
        elif i == 1:
            self.RPM_dd.show()
            self.RPM_label.show()

    def StaticVsDynamic(self):
        if self.bottom_label.currentIndex() == 0:
            self.bottom_label.setCurrentIndex(1)
        elif self.bottom_label.currentIndex() == 1:
            self.bottom_label.setCurrentIndex(0)

    def GUI_Plot(self,x,y,ii,name):
        plt = self.graphContainer.plotItem.plot(x,y,pen=pyqtgraph.mkPen(color=pyqtgraph.intColor(index=ii),width=1))
        
        self.legend.addItem(name=name,item=plt)

        
    def Legendless_Plot(self,x,y,ii):
        plt = self.graphContainer.plotItem.plot(x,y,pen=pyqtgraph.mkPen(color=pyqtgraph.intColor(index=ii),width=1))

    def Clear_plot(self):
        self.graphContainer.plotItem.clear()

        self.legend.clear()


if __name__ == "__main__":
    # Call the application
    app = QApplication([])

    # Open the window
    window = Graph()

    x1 = [0, 1, 2, 3, 4]
    y1 = [0, 1, 4, 9, 16]

    x2 = [0, -1, -2, -3, -4]
    y2 = [0, -1, -4, -9, -16]

    window.GUI_Plot(x1,y1,1,'first')
    window.GUI_Plot(x2,y2,2,'second')

    window.show()

    # Start the app
    app.exec()

    



