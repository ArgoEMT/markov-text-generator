import json
import os


def doubleTraining():
    # Checks if the files exist
    isResultFileExists = os.path.isfile(
        './generated/couple-training-result-freq.json')
    isTrainingFileExist = os.path.isfile('./training-data.txt')

    # Open training set or throw exception if it does not exist
    if(isTrainingFileExist != True):
        raise ValueError(
            'Training file does not exist. This program cannot be launch.')
    else:
        trainingDataFile = open('./training-data.txt', 'r')
        trainingData = trainingDataFile.read()
        trainingDataFile.close()
        trainingData = trainingData.split()

    # Open or create the training result file
    if(isResultFileExists):
        with open('./generated/couple-training-result-freq.json') as json_file:
            resultTrainingFreq = json.load(json_file)
    else:
        resultTrainingFreq = {}

    listlenght = len(trainingData)

    # Calculate the number of time that a word come after another
    # and keep track of the total number of word that came after this specific word.
    for i in range(0, listlenght - 1):
        print('Couple training: ', (i+1), '/', listlenght-1)
        if(i != listlenght - 2):
            firstWord = trainingData[i] + ' ' + trainingData[i+1]
            isWordPresent = firstWord in resultTrainingFreq
            if(isWordPresent):
                isSecondWordPresent = trainingData[i +
                                                   2] in (resultTrainingFreq[firstWord])
                if(isSecondWordPresent):
                    resultTrainingFreq[firstWord][trainingData[i+2]
                                                  ] = resultTrainingFreq[firstWord][trainingData[i+2]] + 1
                    resultTrainingFreq[firstWord]['counter'] = resultTrainingFreq[firstWord]['counter'] + 1
                else:
                    resultTrainingFreq[firstWord][trainingData[i+2]] = 1
                    resultTrainingFreq[firstWord]['counter'] = resultTrainingFreq[firstWord]['counter'] + 1
            else:
                resultTrainingFreq[firstWord] = {
                    trainingData[i+2]: 1, 'counter': 1}

    # Create a new json that store probabilities instead of frequencies
    resultTrainingProb = {}
    for word in resultTrainingFreq:
        resultTrainingProb[word] = {}
        for subWord in resultTrainingFreq[word]:
            if(subWord != 'counter'):
                resultTrainingProb[word][subWord] = resultTrainingFreq[word][subWord] / \
                    resultTrainingFreq[word]['counter']

    # Save the changes for frequencies and create a new file for probabilites
    with open('./generated/couple-training-result-freq.json', 'w') as outfile:
        json.dump(resultTrainingFreq, outfile)

    with open('./generated/couple-training-result-prob.json', 'w') as outfile:
        json.dump(resultTrainingProb, outfile)


doubleTraining()
