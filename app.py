#!/usr/bin/env python3

import yaml
from speedback import SpeedbackMatrix
from util import RoundTimer, ConsoleIO

def readConfigFile():
    with open("config.yml", 'r') as stream:
        try:
            fileContent=yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return fileContent

config=readConfigFile()
members=config['members']
duration=config['duration']
consoleIO=ConsoleIO()

if(consoleIO.validatedWithUser(duration, len(members))):
    matrix=SpeedbackMatrix().populateGrid(members)
    timer=RoundTimer()
    consoleIO.prettyPrintMatrix(matrix)
    print(duration)
    timer.startRounds(duration, len(members))
print("Thank you")