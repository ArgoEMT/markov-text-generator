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
    if mot not in resultTraining :
        i = np.random.choice(list(resultTraining))
        possible_Chars = list(resultTraining[i].keys())
        return np.random.choice(possible_Chars) 
    else :             
        possible_Chars = list(resultTraining[mot].keys())
        possible_values = list(resultTraining[mot].values())
        return np.random.choice(possible_Chars, p=possible_values)


print('Premiers mots : ')
resultText = input()+' '
frac = resultText.split(' ')
lastword = frac[-1]
doStop = False
while(doStop != True):
    newWord = getNextWord(lastword)
    resultText = resultText + newWord + ' '
    doStop = functionStopCheck(newWord)

print(resultText)
