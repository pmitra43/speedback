#!/usr/bin/env python3

import yaml
from speedback import SpeedbackMatrix
from util import RoundTimer, ConsoleIO

class App:
    def __init__(self):
        self.consoleIO=ConsoleIO()
        self.timer=RoundTimer()
        self.speedbackMatrix=SpeedbackMatrix()

    def readConfigFile(self):
        with open("config.yml", 'r') as stream:
            try:
                fileContent=yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        return fileContent

    def runApplication(self):
        config=self.readConfigFile()
        members=config['members']
        duration=config['duration']

        if(self.consoleIO.validatedWithUser(duration, len(members))):
            matrix=self.speedbackMatrix.populateGrid(members)
            self.consoleIO.prettyPrintMatrix(matrix)
            print(duration)
            self.timer.startRounds(duration, len(members))
        print("Thank you")

App().runApplication()