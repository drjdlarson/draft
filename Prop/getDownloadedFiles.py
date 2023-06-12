import os
from Prop import datFileReader

def datFileList():

    list = os.listdir('Prop\DataFiles')
    list.remove('CSVFiles')

    return list


def CSVFileList():

    list = os.listdir('Prop\DataFiles\CSVFiles')
    list.remove('StaticCSV')

    return list


def updateCSVFiles():

    datList = datFileList()
        
    csvList = CSVFileList()

    for ii, names in enumerate(datList):

        if datList[ii].replace("dat","csv") not in csvList:

            datFileReader.datToCSV(datList[ii])



if __name__ == "__main__":

    updateCSVFiles()


