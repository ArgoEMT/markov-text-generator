import json
import os
import numpy as np
from constants import *

# Check if a word contains one of the stopping characters declared in [STOPPING_VALUES]
def __functionStopCheck(wordToTest):
    for char in STOPPING_VALUES:
        if(char in wordToTest):
            return True
    return False


# Get word following [mot].
# Require a list [allWords] and a json [resultTraining]
def __getNextWord(mot, allWords, resultTraining):
    mot = mot.lower()
    if mot not in resultTraining:
        randomWord = np.random.choice(allWords)
        possible_words = list(resultTraining[randomWord].keys())
        return np.random.choice(possible_words)
    else:
        possible_words = list(resultTraining[mot].keys())
        possible_probabilities = list(resultTraining[mot].values())
        return np.random.choice(possible_words, p=possible_probabilities)


# Generate the phrase and print it.
def generatePhrase():
    # Checks if the files exist
    isResultFileExists = os.path.isfile('./training-result-prob.json')

    # Open or create the training result file
    if(isResultFileExists):
        with open('./training-result-prob.json') as json_file:
            resultTraining = json.load(json_file)
    else:
        raise ValueError(
            'Training result file does not exist. This program cannot be launch.')
    allWords = list(resultTraining)

    # Get the first word from an user input
    print('Premiers mots : ')
    resultText = input()+' '
    lastword = (resultText.split(' '))[0]
    doStop = False

    # Loop to create the phrase
    while(doStop != True):
        newWord = __getNextWord(lastword, allWords, resultTraining)
        resultText = resultText + newWord + ' '
        doStop = __functionStopCheck(newWord)

    print(resultText)

# Test
generatePhrase()
