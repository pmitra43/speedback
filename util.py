import time
import subprocess
import sys

class RoundTimer:

    def startRounds(self, pairFeedbackTimeInMinutes, pairSwitchTimeInSeconds, memberLength):
        for roundCount in range(1, memberLength):
            self.startSwitchTimer(roundCount, pairSwitchTimeInSeconds)
            self.startFeedbackRoundTimer(roundCount, pairFeedbackTimeInMinutes)

    def startSwitchTimer(self, roundCount, pairSwitchTimeInSeconds):
        for secondsLeft in range(int(pairSwitchTimeInSeconds),3, -1):
            self.printSameLine("\rRound %d coming up in %d seconds" % (roundCount, secondsLeft))
            time.sleep(1)
    
    def startFeedbackRoundTimer(self, roundCount, pairFeedbackTimeInMinutes):
        self.doCountdown(roundCount)
        self.showTimer(roundCount, pairFeedbackTimeInMinutes*60, pairFeedbackTimeInMinutes*30)
        self.say("half time. It's your pair's turn now")
        self.showTimer(roundCount, pairFeedbackTimeInMinutes*30, 0)
        print("\rRound %d finished. Time to switch pair" % (roundCount))
        self.say("time up")

    def doCountdown(self, roundCount):
        self.say("next round starting in")
        for secondsLeft in range(3,0,-1):
            self.printSameLine("\rRound %d coming up in %d seconds" % (roundCount, secondsLeft%60))
            self.say(secondsLeft)
            time.sleep(0.6)

    def showTimer(self, roundCount, upperLimit, lowerLimit):
        for secondsLeft in range(int(upperLimit),int(lowerLimit), -1):
            self.printSameLine("\rOngoing Round %d : %02d:%02d minutes left" % 
            (roundCount, int(secondsLeft/60), int(secondsLeft%60)))
            time.sleep(1)

    def say(self, item):
        subprocess.call('say -r 200 '+str(item), shell=True)

    def printSameLine(self, item):
        print("\r%s" % item, end="")

class ConsoleIO:

    def validateWithUser(self, feedbackTime, switchTime, memberLength):
        while(1):
            timeRequired = self.calculateTotalDuration(feedbackTime, switchTime, memberLength)
            print("With %d minutes per round and %d seconds to switch, you will need %s minutes" % 
                (feedbackTime, switchTime, timeRequired))
            choice=input("Do you want to start/edit/quit? (s-start/e-edit/q-quit): ")
            if(choice=='s'):
                return (True, feedbackTime, switchTime)
            elif(choice=='e'):
                newFeedbackTime = input("Provide new pair feedback time in minutes :(%d):" % (feedbackTime))
                newSwitchTime = input("Provide new pair switch in seconds :(%d):" % (switchTime))
                try:
                    if(newFeedbackTime!=""):
                        feedbackTime=int(newFeedbackTime)
                    if(newSwitchTime!=""):
                        switchTime=int(newSwitchTime)
                except:
                    print("input is not an integer")
                    continue
            elif(choice=='q'):
                return (False, None, None)
            else:
                print("Wrong choice")
    
    def calculateTotalDuration(self, feedbackTime, switchTime, memberLength):
        timeInSec = feedbackTime*60*(memberLength-1)
        timeInSec = timeInSec+(switchTime+1)*(memberLength-1)
        return "%02d:%02d" % (int(timeInSec/60), int(timeInSec%60))

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
    
    def printLeftAlign(self, item):
        sys.stdout.flush()
        sys.stdout.write("%-25s" % item)