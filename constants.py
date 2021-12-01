STOPPING_VALUES = [".", "?", "!", "..."]

# Check if a word contains one of the stopping characters declared in [STOPPING_VALUES]
def functionStopCheck(wordToTest):
    for char in STOPPING_VALUES:
        if(char in wordToTest):
            return True
    return False