import re, string

# takes in list of words from file 'text2.txt' and sets up dictionary to count word frequency
# TODO: turn above comment into triple quote docstring
def histogram(words_from_text):
    dict = {}
    for word in words_from_text:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict

# takes in histogram and returns a count of unique words_from_text
def unique_words(histogram):
    return len(histogram)

# takes in a word and returns the word count from histogram
def frequency(word, histogram):
    if word in histogram:
        return histogram[word]
    else:
        return "Given word is not an element of the histogram."

#       Hist list of tuples implementation
def hist_list_of_tuples(words_from_text):
    list_of_tuples = []
    inner_tuple = ()
    for word in words_from_text:
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
    # print(list_of_tuples)
    return(list_of_tuples)

#   hist list of lists implementation

def hist_list_of_lists(words_from_text):
    list_of_lists = []
    inner_list = []
    for word in words_from_text:
        found = False
        for inner_list in list_of_lists:
            if word == inner_list[0]:
                found = True
                inner_list[1]+=1
                break
        if not found:
            list_of_lists.append([word, 1])
    # print(list_of_lists)
    return(list_of_lists)

if __name__ == '__main__':
    word_file = 'text2.txt'
    text =  open(word_file).read()
    # TODO: open with with instead of open()

    # removes punctuation from text and sets all ensures all characters are lower case
    translator = str.maketrans('', '', string.punctuation)
    text = text.lower()
    words_from_text = (text.translate(translator)).split()

    # sorts words alphabetically
    words_from_text = sorted(words_from_text)
    # hist = histogram(words_from_text)

    hist = hist_list_of_lists(words_from_text)
    # hist = hist_list_of_tuples(words_from_text)
    print(hist)
