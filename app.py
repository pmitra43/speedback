import yaml
from speedback import SpeedbackMatrix

def readConfig():
    with open("config.yml", 'r') as stream:
        try:
            fileContent=yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return fileContent

config=readConfig()
matrix=SpeedbackMatrix()
print(matrix.getFinalGrid(config['members']))

