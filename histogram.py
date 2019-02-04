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

if __name__ == '__main__':
    word_file = 'text2.txt'
    text =  open(word_file).read()

    # removes punctuation from text and sets all ensures all characters are lower case
    translator = str.maketrans('', '', string.punctuation)
    text = text.lower()
    wordsFromText = (text.translate(translator)).split()
    uniqueWordSet = sorted(wordsFromText)
    hist = histogram(uniqueWordSet)
    print(hist)
