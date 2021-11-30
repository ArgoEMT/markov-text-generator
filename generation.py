import json
import os
import numpy as np
from constants import *

# Checks if the files exist
isResultFileExists = os.path.isfile('./training-result.json')


# Open or create the training result file
if(isResultFileExists):
    with open('./training-result.json') as json_file:
        resultTraining = json.load(json_file)
else:
    raise ValueError(
        'Training result file does not exist. This program cannot be launch.')


def getNextWord(mot):
    mot = mot.lower()
    possible_Chars = list(resultTraining[mot].keys())
    possible_values = list(resultTraining[mot].values())
    return np.random.choice(possible_Chars, p=possible_values)


doStop = False
resultText = 'Dumbledore '
lastword = 'Dumbledore'
while(doStop != True):
    newWord = getNextWord(lastword)
    resultText = resultText + newWord + ' '
    lastword = newWord
    doStop = functionStopCheck(newWord)

print(resultText)
