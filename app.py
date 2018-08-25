import yaml
from speedback import SpeedbackMatrix

def readConfig():
    with open("config.yml", 'r') as stream:
        try:
            fileContent=yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return fileContent

def printLeftAlign(item):
    print("%-25s" % item, end="")

def prettyPrintMatrix(matrix):
    columnCount=len(matrix[0])
    printLeftAlign("")
    for columnNumber in range(1, columnCount+1):
        printLeftAlign("Slot "+str(columnNumber))
    print()
    for rowIndex, row in enumerate(matrix):
        printLeftAlign("Round "+str(rowIndex+1))
        for column in row:
            printLeftAlign(""+str(column))
        print()

config=readConfig()
matrix=SpeedbackMatrix().getFinalGrid(config['members'])

prettyPrintMatrix(matrix)

