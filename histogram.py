import re, string

# takes in list of words from file 'text2.txt' and sets up dictionary to count word frequency
def histogram(wordsFromText):
    dict = {}
    for word in wordsFromText:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict

# takes in histogram and returns a count of unique wordsFromText
def unique_words(histogram):
    return len(histogram)

# takes in a word and returns the word count from histogram
def frequency(word, histogram):
    if word in histogram:
        return histogram[word]
    else:
        return "Given word is not an element of the histogram."

#       Hist list of tuples implementation
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

#   hist list of lists implementation

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

if __name__ == '__main__':
    word_file = 'text2.txt'
    text =  open(word_file).read()

    # removes punctuation from text and sets all ensures all characters are lower case
    translator = str.maketrans('', '', string.punctuation)
    text = text.lower()
    wordsFromText = (text.translate(translator)).split()

    # sorts words alphabetically
    wordsFromText = sorted(wordsFromText)
    hist = histogram(wordsFromText)
    
    # hist = hist_list_of_lists(wordsFromText)
    # hist = hist_list_of_tuples(wordsFromText)
    print(hist)
