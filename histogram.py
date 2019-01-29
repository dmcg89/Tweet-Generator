import string


word_file = 'text1.txt'

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

def hist_list_of_lists(uniqueWordSet):
    histListOfLists = []
    for word in uniqueWordSet:
        wordFrequency = frequency(word)
        histEntry = [word, wordFrequency]
        histListOfLists.append(histEntry)
    print(histListOfLists)

def hist_list_of_tuples(uniqueWordSet):
    histListOfTuples = []
    wordFrequencyList = []
    for word in uniqueWordSet:
        wordFrequency = frequency(word)
        wordFrequencyList.append(wordFrequency)
    histListOfTuples = zip(uniqueWordSet, wordFrequencyList)
    for a, *b in histListOfTuples:
      print(a, ' '.join(map(str, b)))




if __name__ == '__main__':
    text =  open(word_file).read()

    # removes punctuation from text and sets all ensures all characters are lower case
    translator = str.maketrans('', '', string.punctuation)
    text = text.lower()
    wordsFromText = (text.translate(translator)).split()
    uniqueWordSet = unique_words()
    # hist_list_of_lists(uniqueWordSet)
    hist_list_of_tuples(uniqueWordSet)
