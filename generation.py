import json
import os
import numpy as np

# Checks if the files exist
isResultFileExists = os.path.isfile('./training-result.json')


# Open or create the training result file
if(isResultFileExists):
    with open('./training-result.json') as json_file:
        resultTraining = json.load(json_file)
else:
    raise ValueError(
        'Training result file does not exist. This program cannot be launch.')


def sample_next(mot):

    possible_Chars = list(resultTraining[mot].keys())
    possible_values = list(resultTraining[mot].values())

    return np.random.choice(possible_Chars, p=possible_values)


doContinue = True
resultText = 'Dumbledore'
lastword ='dumbledore'
while(doContinue):
    resultText = resultText + ' '
    newWord = sample_next(lastword)
    lastword = newWord
    resultText = resultText + newWord
    if(newWord == '.' or '.' in newWord):
        doContinue = False

print(resultText)