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
    inner_list = []
    for word in wordsFromText:
        found = False
        for innerList in listsOfLists:
            if word == innerList[0]:
                found = True
                innerList[1]+=1
                break
        if not found:
            listsOfLists.append([word, 1])
    # print(listsOfLists)


# def hist_list_of_tuples(uniqueWordSet):
#     histListOfTuples = []
#     wordFrequencyList = []
#     for word in uniqueWordSet:
#         wordFrequency = frequency(word)
#         wordFrequencyList.append(wordFrequency)
#     histListOfTuples = list(zip(uniqueWordSet, wordFrequencyList))
#     # for a, *b in histListOfTuples:
#     #   print(a, ' '.join(map(str, b)))
#     print(histListOfTuples)

def hist_list_of_tuples(wordsFromText):
    list_of_tuples = []
    inner_tuple = ()
    for word in wordsFromText:
        found = False
        for inner_tuple in list_of_tuples:
            if word == inner_tuple[0]:
                count = inner_tuple[1] + 1
                list_of_tuples.remove(inner_tuple)
                list_of_tuples.append((word, count))
                found = True
                break
        if not found:
            list_of_tuples.append((word, 1))
    print(list_of_tuples)

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
    # hist_list_of_lists(wordsFromText)
    hist_list_of_tuples(wordsFromText)
    # hist_dictionary(uniqueWordSet)
