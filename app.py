import yaml
import time
import subprocess
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

def startFeedbackRoundTimer(roundCount, duration):
    for secondsLeft in range(int(duration['feedbackTimeInMinutes']*60),0, -1):
        print("\rRound %d : %02d:%02d minutes left" % (roundCount, int(secondsLeft/60), int(secondsLeft%60)), end="")
        time.sleep(1)
    print("\rTime is up", end="")
    subprocess.call('say -r 200 "time up"', shell=True)


config=readConfig()
members=config['members']
duration=config['duration']
matrix=SpeedbackMatrix().getFinalGrid(members)

prettyPrintMatrix(matrix)
for roundCount in range(1, len(members)):
    startFeedbackRoundTimer(roundCount, duration)

