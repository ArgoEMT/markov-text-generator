import json
import os

# Checks if the files exist
isResultFileExists = os.path.isfile('./training-result.json')
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
    with open('./training-result.json') as json_file:
        resultTraining = json.load(json_file)
else:
    resultTraining = {}

listlenght = len(trainingData)

# Calculate the number of time that a word come after another
# and keep track of the total number of word that came after this specific word.
for i in range(0, listlenght):
    print((i+1), '/', listlenght)
    if(i != listlenght - 1):
        isWordPresent = trainingData[i] in resultTraining
        if(isWordPresent):
            isSecondWordPresent = trainingData[i +1] in (resultTraining[trainingData[i]])
            if(isSecondWordPresent):
                resultTraining[trainingData[i]][trainingData[i+1]] = resultTraining[trainingData[i]][trainingData[i+1]] + 1
                resultTraining[trainingData[i]]['counter'] = resultTraining[trainingData[i]]['counter'] + 1
            else:
                resultTraining[trainingData[i]][trainingData[i+1]] = 1
                resultTraining[trainingData[i]]['counter'] = resultTraining[trainingData[i]]['counter'] + 1
        else:
            resultTraining[trainingData[i]] = {trainingData[i+1]: 1, 'counter': 1}

# Transform the number in probabilities
for word in resultTraining:
    for subWord in resultTraining[word]:
        if(subWord != 'counter'):
            resultTraining[word][subWord] = resultTraining[word][subWord] / resultTraining[word]['counter']
    (resultTraining[word]).pop('counter')
    
# Save the changes
with open('training-result.json', 'w') as outfile:
    json.dump(resultTraining, outfile)
