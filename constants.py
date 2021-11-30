STOPPING_VALUES = [".", "?", "!", "..."]

def functionStopCheck(wordToTest):
    for char in STOPPING_VALUES:
        if(char in wordToTest):
            return True
    return False