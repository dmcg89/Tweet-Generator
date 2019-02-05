import random

text = 'one fish two fish red fish blue fish'
wordsFromText = text.split()
print(wordsFromText)

def histogram(wordsFromText):
    dict = {}
    for word in wordsFromText:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict

wordCounts = histogram(wordsFromText)
print(wordCounts)

def weighted_random_select(dict, wordsFromText):
    randomChoice = random.randrange(1, len(wordsFromText)+1)
    weightsSum = 1
    # print(randomChoice)
    for key in dict:
        weightsSum += dict[key]
        # print(weightsSum)
        if randomChoice < weightsSum:
            # print(key)
            return key
            exit

def frequency_test(wordCounts, wordsFromText):
    tempWordList = []
    for i in range(10000):
        selectWord = weighted_random_select(wordCounts, wordsFromText)
        tempWordList.append(selectWord)
    frequencyList = histogram(tempWordList)
    for key in frequencyList:
        frequencyList[key] = frequencyList[key]/len(tempWordList)
    print(frequencyList)



frequency_test(wordCounts, wordsFromText)

# weighted_random_select(wordCounts, wordsFromText)
