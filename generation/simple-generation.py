import sys
sys.path.insert(1, './')
from constants import *
import numpy as np
import os
import json


# Get word following [mot].
# Require a list [allWords] and a json [resultTraining]
def __getNextWord(mot, allWords, resultTraining):
    mot = mot.lower()
    if mot not in allWords:
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
    isResultFileExists = os.path.isfile('./generated/simple-training-result-prob.json')

    # Open or create the training result file
    if(isResultFileExists):
        with open('./generated/simple-training-result-prob.json') as json_file:
            resultTraining = json.load(json_file)
    else:
        raise ValueError(
            'Training result file does not exist. Make sure to run the training before trying to run this methode.')
    allWords = list(resultTraining)

    # Get the first word from an user input
    print('Premiers mots : ')
    resultText = input()+' '
    doStop = False
    
    # Loop to create the phrase
    while(doStop != True):
        frac = resultText.split()
        fraclen = len(frac)
        lastword = frac[fraclen-1]
        
        newWord = __getNextWord(lastword, allWords, resultTraining)
        resultText = resultText + newWord + ' '
        doStop = functionStopCheck(newWord)

    print(resultText)


# Test
generatePhrase()
