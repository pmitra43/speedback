import yaml
import sys
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
    sys.stdout.flush()
    sys.stdout.write("%-25s" % item)

def say(item):
    subprocess.call('say -r 200 '+str(item), shell=True)

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

def doCountdown(roundCount):
    say("next round starting in")
    for secondsLeft in range(3,0,-1):
        printLeftAlign("\rRound %d coming up in %02d seconds" % (roundCount, secondsLeft%60))
        say(secondsLeft)
        time.sleep(0.6)

def showTimer(upperLimit, lowerLimit):
    for secondsLeft in range(int(upperLimit),int(lowerLimit), -1):
        printLeftAlign("\rOngoing Round %d : %02d:%02d minutes left" % (roundCount, int(secondsLeft/60), int(secondsLeft%60)))
        time.sleep(1)

def startFeedbackRoundTimer(roundCount, pairFeedbackTimeInMinutes):
    doCountdown(roundCount)
    showTimer(pairFeedbackTimeInMinutes*60, pairFeedbackTimeInMinutes*30)
    say("half time. It's your pair's turn now")
    showTimer(pairFeedbackTimeInMinutes*30, 0)
    printLeftAlign("\rRound %d finished. Time to switch pair\n" % (roundCount))
    say("time up")

def startSwitchTimer(roundCount, pairSwitchTimeInSeconds):
    for secondsLeft in range(int(pairSwitchTimeInSeconds),3, -1):
        printLeftAlign("\rRound %d coming up in %d seconds" % (roundCount, secondsLeft))
        time.sleep(1)

config=readConfig()
members=config['members']
duration=config['duration']
matrix=SpeedbackMatrix().getFinalGrid(members)

prettyPrintMatrix(matrix)
print()
for roundCount in range(1, len(members)):
    startSwitchTimer(roundCount, duration['pairSwitchTimeInSeconds'])
    startFeedbackRoundTimer(roundCount, duration['pairFeedbackTimeInMinutes'])
