import numpy as np

def get_word_count(filePath):
    with open(filePath) as f:
        words = (f.read()).split()
        return len(words)

def get_character_count(filePath):
    with open(filePath) as f:
        text = f.read()
    text = text.lower()
    dict = {}
    temp = ""

    for i in range(0, len(text)):
        temp = text[i]
        if(temp in dict):
            dict[temp] += 1
        else:
            dict[temp] = 1

    keys = list(dict.keys())
    values = list(dict.values())
    sortedOrder = np.argsort(values)[::-1]
    dictSorted = {keys[i]: values[i] for i in sortedOrder}

    return dictSorted