#!/usr/bin/env python3

import yaml
from speedback import SpeedbackMatrix
from util import RoundTimer, ConsoleIO

class App:
    def __init__(self):
        self.consoleIO=ConsoleIO()
        self.timer=RoundTimer()
        self.speedbackMatrix=SpeedbackMatrix()

    def runApplication(self):
        config=self.readConfigFile()
        members=config['members']
        feedbackPreparationTimeInMinutes=config['duration']['feedbackPreparationTimeInMinutes']
        pairFeedbackTimeInMinutes=config['duration']['pairFeedbackTimeInMinutes']
        pairSwitchTimeInSeconds=config['duration']['pairSwitchTimeInSeconds']
        continueApp, feedbackPreparationTimeInMinutes, pairFeedbackTimeInMinutes, pairSwitchTimeInSeconds = self.consoleIO.validateWithUser(
            feedbackPreparationTimeInMinutes, pairFeedbackTimeInMinutes, pairSwitchTimeInSeconds, len(members))
        if(continueApp):
            matrix=self.speedbackMatrix.populateGrid(members)
            self.consoleIO.prettyPrintMatrix(matrix)
            print("Feedback preparation time (minutes): %d\t" % feedbackPreparationTimeInMinutes, end="")
            print("Feedback sharing time (minutes): %d\t" % pairFeedbackTimeInMinutes, end="")
            print("Pair switch time (seconds): %d\t" % pairSwitchTimeInSeconds)
            self.timer.startRounds(feedbackPreparationTimeInMinutes, pairFeedbackTimeInMinutes, pairSwitchTimeInSeconds, len(members))
        print("Thank you")

    def readConfigFile(self):
        with open("config.yml", 'r') as stream:
            try:
                fileContent=yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return fileContent

App().runApplication()