import yaml
import sys
from speedback import SpeedbackMatrix
from timer import RoundTimer

class ConsoleIO:
    def printLeftAlign(self, item):
        sys.stdout.flush()
        sys.stdout.write("%-25s" % item)

    def prettyPrintMatrix(self, matrix):
        columnCount=len(matrix[0])
        self.printLeftAlign("")
        for columnNumber in range(1, columnCount+1):
            self.printLeftAlign("Slot "+str(columnNumber))
        print()
        for rowIndex, row in enumerate(matrix):
            self.printLeftAlign("Round "+str(rowIndex+1))
            for column in row:
                self.printLeftAlign(""+str(column))
            print()

    def calculateTotalDuration(self, feedbackTime, switchTime, memberLength):
        timeInSec = feedbackTime*60*(memberLength-1)
        timeInSec = timeInSec+(switchTime+1)*(memberLength-1)
        return "%02d:%02d" % (int(timeInSec/60), int(timeInSec%60))

    def validatedWithUser(self, duration, memberLength):
        feedbackTime=duration['pairFeedbackTimeInMinutes']
        switchTime=duration['pairSwitchTimeInSeconds']
        while(1):
            timeRequired = self.calculateTotalDuration(feedbackTime, switchTime, memberLength)
            print("With %d minutes per round and %d seconds to switch, you will need %s minutes" % 
                (feedbackTime, switchTime, timeRequired))
            choice=input("Do you want to start/edit/quit? (s-start/e-edit/q-quit): ")
            if(choice=='s'):
                duration['pairFeedbackTimeInMinutes']=feedbackTime
                duration['pairSwitchTimeInSeconds']=switchTime
                return True
            elif(choice=='e'):
                newFeedbackTime = input("Provide new pair feedback time in minutes :(%d):" % (feedbackTime))
                newSwitchTime = input("Provide new pair switch in seconds :(%d):" % (switchTime))
                try:
                    if(newFeedbackTime!=""):
                        feedbackTime=int(newFeedbackTime)
                    if(newSwitchTime!=""):
                        switchTime=int(newSwitchTime)
                except:
                    print("Invalid option")
                    continue
            elif(choice=='q'):
                return False
            else:
                print("Wrong choice")

def readConfig():
    with open("config.yml", 'r') as stream:
        try:
            fileContent=yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return fileContent

config=readConfig()
members=config['members']
duration=config['duration']
consoleIO=ConsoleIO()

if(consoleIO.validatedWithUser(duration, len(members))):
    matrix=SpeedbackMatrix().populateGrid(members)
    timer=RoundTimer()
    consoleIO.prettyPrintMatrix(matrix)
    print(duration)
    timer.startRounds(duration, len(members))