import string

def unique_words():
    uniqueWordSet = set(wordsFromText)
    print(len(uniqueWordSet))
    return (uniqueWordSet)

def frequency(selectWord):
    frequency = 0
    for word in wordsFromText:
        if word == selectWord:
            frequency += 1
    # print(frequency)
    return frequency

# def hist_list_of_lists(uniqueWordSet):
#     histListOfLists = []
#     for word in uniqueWordSet:
#         wordFrequency = frequency(word)
#         histEntry = [word, wordFrequency]
#         histListOfLists.append(histEntry)
#     print(histListOfLists)

def hist_list_of_lists(wordsFromText):
    listsOfLists = []
    for word in wordsFromText:
        for innerList in listsOfLists:
            if listsOfLists == []:
                innerList.append([word, 1])
            print(word)
            print(innerList)
            if word == innerList[0]:
                innerList[1]+=1
            else:
                listsOfLists.append([word, 1])
    print(listsOfLists)


def hist_list_of_tuples(uniqueWordSet):
    histListOfTuples = []
    wordFrequencyList = []
    for word in uniqueWordSet:
        wordFrequency = frequency(word)
        wordFrequencyList.append(wordFrequency)
    histListOfTuples = list(zip(uniqueWordSet, wordFrequencyList))
    # for a, *b in histListOfTuples:
    #   print(a, ' '.join(map(str, b)))
    print(histListOfTuples)

# for innerTuple in list
#     if word == innerTuple[0]:
#         count = innerTuple[1] + 1
#         list.remove(innerTuple)
#         list.append((word,count))
#         break
#     if not found:
#         list.append((word,1))

def hist_dictionary(uniqueWordSet):
    dict = {}
    wordFrequencyList = []
    for word in uniqueWordSet:
        wordFrequency = frequency(word)
        wordFrequencyList.append(wordFrequency)
    for key, value in zip(uniqueWordSet, wordFrequencyList):
        dict[key] = value
    print(dict)


if __name__ == '__main__':
    word_file = 'text2.txt'
    text =  open(word_file).read()

    # removes punctuation from text and sets all ensures all characters are lower case
    translator = str.maketrans('', '', string.punctuation)
    text = text.lower()
    wordsFromText = (text.translate(translator)).split()
    uniqueWordSet = sorted(unique_words())
    # frequency('the')
    hist_list_of_lists(wordsFromText)
    # hist_list_of_tuples(uniqueWordSet)
    # hist_dictionary(uniqueWordSet)
