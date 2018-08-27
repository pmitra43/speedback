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
        pairFeedbackTimeInMinutes=config['duration']['pairFeedbackTimeInMinutes']
        pairSwitchTimeInSeconds=config['duration']['pairSwitchTimeInSeconds']
        continueApp, pairFeedbackTimeInMinutes, pairSwitchTimeInSeconds = self.consoleIO.validateWithUser(
            pairFeedbackTimeInMinutes, pairSwitchTimeInSeconds, len(members))
        if(continueApp):
            matrix=self.speedbackMatrix.populateGrid(members)
            self.consoleIO.prettyPrintMatrix(matrix)
            self.timer.startRounds(pairFeedbackTimeInMinutes, pairSwitchTimeInSeconds, len(members))
        print("Thank you")

    def readConfigFile(self):
        with open("config.yml", 'r') as stream:
            try:
                fileContent=yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return fileContent

App().runApplication()