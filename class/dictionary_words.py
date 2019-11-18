import random
import sys

# Open dictionary
word_file = "/usr/share/dict/words"
# words = open(word_file).read().splitlines()
#file.readline() one line at a time (for loop)
#file.readlines() best practice for this case?
words = ['katie', 'robin', 'trout', 'drew', 'ben']

# Generate random integers to serve as the indices for the random words selected from dict
def random_integers_list():
    listOfNumbers = []
    fileWordCount = len(words)
    for x in range (0, sentenceWordCount):
        listOfNumbers.append(random.randint(0, fileWordCount - 1))
        print(listOfNumbers)
    return listOfNumbers

#Use random integers to select random words from dict
def find_random_word(listOfNumbers):
    sentence = []
    for num in listOfNumbers:
        newRandomWord = words[num]
        sentence.append(newRandomWord)
    return sentence

#Print random words in a sentence
def print_sentence(sentence):
    print(*sentence,'.')

if __name__ == '__main__':
    sentenceWordCount = int(sys.argv[1])
    listOfNumbers = random_integers_list()
    sentence = find_random_word(listOfNumbers)
    print_sentence(sentence)
