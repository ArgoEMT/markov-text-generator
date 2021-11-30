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
def sample_next(mot):
    if mot not in resultTraining :
        i = np.random.choice(list(resultTraining))
        possible_Chars = list(resultTraining[i].keys())
        return np.random.choice(possible_Chars) 
    else :             
        possible_Chars = list(resultTraining[mot].keys())
        possible_values = list(resultTraining[mot].values())
        return np.random.choice(possible_Chars, p=possible_values)


doContinue = True
print('Premiers mots : ')
resultText = input()
frac = resultText.split(' ')
lastword = frac[-1]
while(doContinue):
    resultText = resultText + ' '
    newWord = sample_next(lastword)
    lastword = newWord
    doStop = functionStopCheck(newWord)

print(resultText)
