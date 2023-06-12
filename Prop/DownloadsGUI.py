from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QListWidget,
    QAbstractItemView)
from Prop import getDownloadedFiles

class DownloadsList(QMainWindow):
    def __init__(self):
        super().__init__()

        # Define the layout(s)
        layout = QHBoxLayout()
        layoutLeft = QVBoxLayout()
        layoutRight = QVBoxLayout()
        InternalLayout = QHBoxLayout()
        externalLayout = QVBoxLayout()

        # Get the list for the widget
        ListValues = getDownloadedFiles.CSVFileList()

        # Define the widgets
        self.DownloadedList = QListWidget()
        self.DownloadedList.addItems(ListValues)
        self.DownloadedList.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        Label = QLabel(".csv models already downloaded: ")
        self.button_updateList = QPushButton("Update List")
        self.checkbox_Static = QCheckBox()
        StaticLabel = QLabel("Static")
        self.checkbox_Dynamic = QCheckBox()
        self.checkbox_Dynamic.setChecked(True)
        DynamicLabel = QLabel("Dynamic")
        self.button_Plot = QPushButton("Plot")

        # Add Widgets to layouts
        InternalLayout.addWidget(self.checkbox_Static)
        InternalLayout.addWidget(StaticLabel)
        InternalLayout.addWidget(self.checkbox_Dynamic)
        InternalLayout.addWidget(DynamicLabel)

        layoutRight.addWidget(self.button_updateList)
        layoutRight.addLayout(InternalLayout)
        layoutRight.addWidget(self.button_Plot)

        layoutLeft.addWidget(self.DownloadedList)

        layout.addLayout(layoutLeft)
        layout.addLayout(layoutRight)

        externalLayout.addWidget(Label)
        externalLayout.addLayout(layout)

        # Setting overall layout
        self.Main = QWidget()
        self.Main.setLayout(externalLayout)
        self.setCentralWidget(self.Main)

        # Connecting crap
        self.button_updateList.clicked.connect(self.update_list)
        self.checkbox_Dynamic.stateChanged.connect(self.Dynamic_Checked)
        self.checkbox_Static.stateChanged.connect(self.Static_Checked)
    
    def update_list(self):
        getDownloadedFiles.updateCSVFiles()
        ListValues = getDownloadedFiles.CSVFileList()
        self.DownloadedList.clear()
        self.DownloadedList.addItems(ListValues)

    def Dynamic_Checked(self):
        if self.checkbox_Dynamic.isChecked() == 0:
            self.checkbox_Static.setChecked(True)
        elif self.checkbox_Dynamic.isChecked() == 1:
            self.checkbox_Static.setChecked(False)

    def Static_Checked(self):
        if self.checkbox_Static.isChecked() == 0:
            self.checkbox_Dynamic.setChecked(True)
        elif self.checkbox_Static.isChecked() == 1:
            self.checkbox_Dynamic.setChecked(False)






if __name__ == "__main__":
    # Call the application
    app = QApplication([])

    # Open the window
    window = DownloadsList()
    window.show()

    # Start the app
    app.exec()