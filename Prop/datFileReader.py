import numpy as np

def datToDict(FileName):
    DynamicThrust = {}
    RPMList = []

    with open('Prop\DataFiles\\' + FileName, 'r') as dat_file:
        # Preallocated values 
        rowNum = 0
        PropIndexLower = 500
        PropIndexHigher = 500
        Data = []

        for row in dat_file:
            rowNum = rowNum + 1

            if row.__contains__('PROP'):
                PropIndexLower = rowNum + 4 # This skips the next 4 lines
                PropIndexHigher = rowNum + 34 

                Data.clear()

                RPM = [int(ii) for ii in row.split() if ii.isdigit()]
                RPMList.append(RPM[0])
                DynamicThrust.update({RPM[0]: []})

            elif rowNum in range(PropIndexLower,PropIndexHigher):

                rowVals = [float(ii) for ii in row.split()]

                DynamicThrust[RPM[0]].append(rowVals)


    return DynamicThrust, RPMList


def DictToCSV(Dict,DictNames,FileName):

    with open('Prop\DataFiles\CSVFiles\\' + FileName,'w') as csvFile:
        with open('Prop\DataFiles\CSVFiles\StaticCSV\\' + 'static_' + FileName,'w') as static:

            for ii, name in enumerate(DictNames):
                row = []
                length = len(Dict[name][0])

                for kk in range(0, len(Dict[name])-1):
                    row = Dict[name][kk]

                    if len(row) == length:              # This if statement purges all faulty data 
                        csvFile.write(str(name))
                        csvFile.write(", ")
                        csvFile.write(str(row).strip().replace("[","").replace("]",""))
                        csvFile.write("\n")

                staticRow = Dict[name][0]

                static.write(str(name))
                static.write(", ")
                static.write(str(staticRow).strip().replace("[","").replace("]",""))
                static.write("\n")


def datToCSV(FileName):

    Dict, DictNames = datToDict(FileName)

    DictToCSV(Dict,DictNames,FileName.replace("dat","csv"))


def CSVToMatrix(csvFile):

    Matrix = np.genfromtxt('Prop\DataFiles\CSVFiles\\' + csvFile, delimiter=',')

    return Matrix

def StaticCSV(csvFile):

    Matrix = np.genfromtxt('Prop\DataFiles\CSVFiles\StaticCSV\\' + 'static_' + csvFile, delimiter=',')

    return Matrix


def datToMatrix(fileName):

    datToCSV(fileName)

    Matrix = CSVToMatrix(fileName.replace("dat","csv"))

    return Matrix

def MatrixColumns(matrix):

    RPM = matrix[:,0]
    V_MPH = matrix[:,1]
    AdvRatio = matrix[:,2]
    Efficiency = matrix[:,3]
    CoeffThrust = matrix[:,4]
    CoeffPower = matrix[:,5]
    PowerMerica = matrix[:,6]
    TorqueMerica = matrix[:,7]
    ThrustMerica = matrix[:,8]
    Power = matrix[:,9]
    Torque = matrix[:,10]
    Thrust = matrix[:,11]
    ThrustPerPower = matrix[:,12]
    Mach = matrix[:,13]
    Reyn = matrix[:,14]
    FigOMerit = matrix[:,15]

    return RPM,V_MPH,AdvRatio,Efficiency,CoeffThrust,CoeffPower,PowerMerica,TorqueMerica,ThrustMerica,Power,Torque,Thrust,ThrustPerPower,Mach,Reyn,FigOMerit



# Just an example
if __name__ == "__main__":

    file_name = "PER3_105x45.dat"

    datToCSV(file_name)

    # RPM,V_MPH,AdvRatio,Efficiency,CoeffThrust,CoeffPower,PowerMerica,TorqueMerica,ThrustMerica,Power,Torque,Thrust,ThrustPerPower,Mach,Reyn,FigOMerit = MatrixColumns(Matrix)

