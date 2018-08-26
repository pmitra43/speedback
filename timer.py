import time
import subprocess

class RoundTimer:

    def say(self, item):
        subprocess.call('say -r 200 '+str(item), shell=True)

    def printSameLine(self, item):
        print("\r%s" % item, end="")

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
    
    def startFeedbackRoundTimer(self, roundCount, pairFeedbackTimeInMinutes):
        self.doCountdown(roundCount)
        self.showTimer(roundCount, pairFeedbackTimeInMinutes*60, pairFeedbackTimeInMinutes*30)
        self.say("half time. It's your pair's turn now")
        self.showTimer(roundCount, pairFeedbackTimeInMinutes*30, 0)
        print("\rRound %d finished. Time to switch pair" % (roundCount))
        self.say("time up")

    def startSwitchTimer(self, roundCount, pairSwitchTimeInSeconds):
        for secondsLeft in range(int(pairSwitchTimeInSeconds),3, -1):
            self.printSameLine("\rRound %d coming up in %d seconds" % (roundCount, secondsLeft))
            time.sleep(1)

    def startRounds(self, duration, memberLength):
        for roundCount in range(1, memberLength):
            self.startSwitchTimer(roundCount, duration['pairSwitchTimeInSeconds'])
            self.startFeedbackRoundTimer(roundCount, duration['pairFeedbackTimeInMinutes'])