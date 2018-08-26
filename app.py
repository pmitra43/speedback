import yaml
import sys
from speedback import SpeedbackMatrix
from timer import RoundTimer

def readConfig():
    with open("config.yml", 'r') as stream:
        try:
            fileContent=yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return fileContent

def printLeftAlign(item):
    sys.stdout.flush()
    sys.stdout.write("%-25s" % item)

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
members=config['members']
duration=config['duration']
matrix=SpeedbackMatrix().populateGrid(members)
timer=RoundTimer()

prettyPrintMatrix(matrix)
print()
timer.startRounds(duration, len(members))