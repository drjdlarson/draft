from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget)

# import DownloadsGUI
from Prop import DownloadsGUI
from Prop import GUIGraphing 
from Prop import datFileReader
from Prop import getDownloadedFiles
import numpy
import webbrowser 

class PropWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Define the layout
        layout = QVBoxLayout()

        # Define the widgets
        self.DownloadsList = DownloadsGUI.DownloadsList()
        self.GraphGUI = GUIGraphing.Graph()
        self.button = QPushButton(text='Go to Website')

        # Add the widgets to the layout
        layout.addWidget(self.button)
        layout.addWidget(self.DownloadsList.Main)
        layout.addWidget(self.GraphGUI.Main)

        # Setting the overall layout as the central widget
        overall = QWidget()
        overall.setLayout(layout)
        self.setCentralWidget(overall)

        # Extra Connections
        self.DownloadsList.checkbox_Dynamic.stateChanged.connect(self.bottom_axis_change)
        self.DownloadsList.checkbox_Dynamic.stateChanged.connect(self.Plot_Stuff)
        self.DownloadsList.button_Plot.pressed.connect(self.Plot_Stuff)

        self.GraphGUI.RPM_dd.currentIndexChanged.connect(self.Plot_Stuff)
        self.GraphGUI.dynamic_menu.currentIndexChanged.connect(self.Plot_Stuff)

        self.button.pressed.connect(self.toWeb)

    def toWeb(self):

        webbrowser.open('https://www.apcprop.com/technical-information/performance-data/')

    def bottom_axis_change(self):

        self.GraphGUI.StaticVsDynamic()

    def Plot_Dict(self):
        self.dict = {}
        objList = self.DownloadsList.DownloadedList.selectedIndexes()
        intList = []
        nameList = getDownloadedFiles.CSVFileList()

        for jj, n in enumerate(objList):
            obj = objList[jj].row()
            intList.append(obj)

        for ii in intList:

            matrix = datFileReader.CSVToMatrix(nameList[ii])

            self.dict.update({ii:matrix})

        return self.dict, nameList
    
    def Static_Data(self):
        self.StaticDict = {}
        objList = self.DownloadsList.DownloadedList.selectedIndexes()
        intList = []
        nameList = getDownloadedFiles.CSVFileList()

        for jj, n in enumerate(objList):
            obj = objList[jj].row()
            intList.append(obj)

        for ii in intList:

            matrix = datFileReader.StaticCSV(nameList[ii])
            
            self.StaticDict.update({ii:matrix})

        return self.StaticDict, nameList

    def Plot_Stuff(self):

        self.GraphGUI.Clear_plot()

        if self.GraphGUI.bottom_label.currentIndex() == 0:
            # Graph is set to be dynamic
            self.dict, nameList = self.Plot_Dict()

            for ii in self.dict:
                RPM,V_MPH,AdvRatio,Efficiency,CoeffThrust,CoeffPower,PowerMerica,TorqueMerica,ThrustMerica,Power,Torque,Thrust,ThrustPerPower,Mach,Reyn,FigOMerit=datFileReader.MatrixColumns(self.dict[ii])
                RPMList = []

                for n, val in enumerate(RPM):
                    if RPM[n] not in RPMList:
                        RPMList.append(RPM[n])

                objList = self.GraphGUI.left_label.selectedIndexes()
                intList = []

                for m, nm in enumerate(objList):
                    obj = objList[m].row()
                    intList.append(obj)

                for kk in intList:

                    if self.GraphGUI.dynamic_menu.currentIndex() == 0:
                        # x axis is the advanced ratio

                        for zz, name in enumerate(RPMList):

                            indices = numpy.where(RPM == name)

                            x = numpy.squeeze(numpy.take(AdvRatio,indices))

                            if kk==0:
                                y = numpy.squeeze(numpy.take(Thrust,indices))
                                NameStr = ' Thrust'
                            elif kk==1:
                                y = numpy.squeeze(numpy.take(CoeffThrust,indices))
                                NameStr = ' Thrust Coeff'
                            elif kk==2:
                                y = numpy.squeeze(numpy.take(Power,indices))
                                NameStr = ' Power'
                            elif kk==3:
                                y = numpy.squeeze(numpy.take(CoeffPower,indices))
                                NameStr = ' Power Coeff'
                            elif kk==4:
                                y = numpy.squeeze(numpy.take(Efficiency,indices))
                                NameStr = ' Efficiency'
                            elif kk==5:
                                y = numpy.squeeze(numpy.take(Torque,indices))
                                NameStr = ' Torque'

                            if zz == 1: 
                                self.GraphGUI.GUI_Plot(x,y,ii+kk,nameList[ii].replace('.csv','').replace('PER3_','')+NameStr)
                            else: 
                                self.GraphGUI.Legendless_Plot(x,y,ii+kk)

                    elif self.GraphGUI.dynamic_menu.currentIndex() == 1:
                        # x axis has the slider
                        if kk==0:
                            y = Thrust
                            self.varying_plot(RPM,V_MPH,y,ii,kk,nameList[ii].replace('.csv','').replace('PER3_','')+' Thrust')
                        elif kk==1:
                            y = CoeffThrust
                            self.varying_plot(RPM,V_MPH,y,ii,kk,nameList[ii].replace('.csv','').replace('PER3_','')+' Thrust Coeff')
                        elif kk==2:
                            y = Power
                            self.varying_plot(RPM,V_MPH,y,ii,kk,nameList[ii].replace('.csv','').replace('PER3_','')+' Power')
                        elif kk==3:
                            y = CoeffPower
                            self.varying_plot(RPM,V_MPH,y,ii,kk,nameList[ii].replace('.csv','').replace('PER3_','')+' Power Coeff')
                        elif kk==4:
                            y = Efficiency
                            self.varying_plot(RPM,V_MPH,y,ii,kk,nameList[ii].replace('.csv','').replace('PER3_','')+' Efficiency')
                        elif kk==5:
                            y = Torque
                            self.varying_plot(RPM,V_MPH,y,ii,kk,nameList[ii].replace('.csv','').replace('PER3_','')+' Torque')
                
        elif self.GraphGUI.bottom_label.currentIndex() == 1:
            # Graph is set to be static
            self.static_dict, nameList = self.Static_Data()

            for ii in self.static_dict:
                static_RPM,static_V_MPH,static_AdvRatio,static_Efficiency,static_CoeffThrust,static_CoeffPower,static_PowerMerica,static_TorqueMerica,static_ThrustMerica,static_Power,static_Torque,static_Thrust,static_ThrustPerPower,static_Mach,static_Reyn,static_FigOMerit=datFileReader.MatrixColumns(self.static_dict[ii])
                static_RPMList = []

                for n, val in enumerate(static_RPM):
                    if static_RPM[n] not in static_RPMList:
                        static_RPMList.append(static_RPM[n])

                objList = self.GraphGUI.left_label.selectedIndexes()
                intList = []

                for m, nm in enumerate(objList):
                    obj = objList[m].row()
                    intList.append(obj)

                for kk in intList:
                     
                    x = numpy.squeeze(static_RPM)

                    if kk==0:
                        y = numpy.squeeze(static_Thrust)
                        NameStr = ' Thrust'
                    elif kk==1:
                        y = numpy.squeeze(static_CoeffThrust)
                        NameStr = ' Thrust Coeff'
                    elif kk==2:
                        y = numpy.squeeze(static_Power)
                        NameStr = ' Power'
                    elif kk==3:
                        y = numpy.squeeze(static_CoeffPower)
                        NameStr = ' Power Coeff'
                    elif kk==4:
                        y = numpy.squeeze(static_Efficiency)
                        NameStr = ' Efficiency'
                    elif kk==5:
                        y = numpy.squeeze(static_Torque)
                        NameStr = ' Torque'
                    
                    self.GraphGUI.GUI_Plot(x,y,ii+kk,nameList[ii].replace('.csv','').replace('PER3_','')+NameStr)
                    
    def varying_plot(self,RPM,V_MPH,yData, ii, kk,LegName):
        RPMList = []
        RPM_Data = []

        for ii, name in enumerate(RPM):
            if name.__str__() not in RPMList:
                RPMList.append(name.__str__())
                RPM_Data.append(name)

        self.GraphGUI.RPM_dd.addItems(RPMList)

        CurrentRPM_index = self.GraphGUI.RPM_dd.currentIndex()
        CurrentRPM = RPM_Data[CurrentRPM_index]

        indices = numpy.where(RPM == CurrentRPM)

        x = numpy.squeeze(numpy.take(V_MPH,indices))
        y = numpy.squeeze(numpy.take(yData,indices))

        self.GraphGUI.GUI_Plot(x,y,ii+kk,LegName)


if __name__ == "__main__":
    # Call the application
    app = QApplication([])

    # Open the window
    window = PropWindow()
    window.show()

    # Start the app
    app.exec()

    
