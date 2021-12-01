import sys
sys.path.insert(1, './')
import json
import os
import numpy as np
from constants import *

# Get word following [mot].
# Require a list [allWords] and a json [resultTraining]


def __getNextWord(mot, allWords, resultTraining):
    mot = mot.lower()
    if mot not in allWords:
        print(mot, ': NOK')
        randomWord = np.random.choice(allWords)
        possible_words = list(resultTraining[randomWord].keys())
        return np.random.choice(possible_words)
    else:
        print(mot, ': OK')
        possible_words = list(resultTraining[mot].keys())
        possible_probabilities = list(resultTraining[mot].values())
        return np.random.choice(possible_words, p=possible_probabilities)


# Generate the phrase and print it.
def generatePhraseWithCouple():
    # Checks if the files exist
    isResultFileExists = os.path.isfile('./couple-training-result-prob.json')

    # Open or create the training result file
    if(isResultFileExists):
        with open('./couple-training-result-prob.json') as json_file:
            resultTraining = json.load(json_file)
    else:
        raise ValueError(
            'Training result file does not exist. This program cannot be launch.')
    allWords = list(resultTraining)

    # Get the first word from an user input
    print('Premiers mots : ')
    resultText = input()+' '
    doStop = False
    # Loop to create the phrase
    while(doStop != True):
        resultList = resultText.split()
        resultLen = len(resultList)
        lastword = resultList[resultLen-2] + ' ' + resultList[resultLen-1]

        newWord = __getNextWord(lastword, allWords, resultTraining)
        resultText = resultText + newWord + ' '
        doStop = functionStopCheck(newWord)

    print(resultText)


# Test
generatePhraseWithCouple()
