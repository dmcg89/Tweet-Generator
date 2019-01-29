import string


word_file = 'text1.txt'
text =  open(word_file).read()
print(text)

# removes punctuation from text and sets all ensures all characters are lower case
translator = str.maketrans('', '', string.punctuation)
text = text.lower()
wordsFromText = (text.translate(translator)).split()

def unique_words():
    uniqueWordSet = set(wordsFromText)
    print(len(uniqueWordSet))
    return len(uniqueWordSet)

def frequency(selectWord):
    frequency = 0
    for word in wordsFromText:
        if word == selectWord:
            frequency += 1
    print(frequency)
    return frequency

# unique_words()
# frequency('mystery')
# frequency('one')

if __name__ == '__main__':
    pass
