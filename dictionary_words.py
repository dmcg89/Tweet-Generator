import random
import sys

# Open dictionary
word_file = "/usr/share/dict/words"
words = open(word_file).read().splitlines()

# Generate random integers to serve as the indices for the random words selected from dict
def randomIntegersList():
    listOfNumbers = []
    fileWordCount = len(words)
    for x in range (0, sentenceWordCount):
        listOfNumbers.append(random.randint(0, fileWordCount - 1))
    return listOfNumbers

#Use random integers to select random words from dict
def findRandomWord(listOfNumbers):
    sentence = []
    for num in listOfNumbers:
        newRandomWord = words[num]
        sentence.append(newRandomWord)
    return sentence

#Print random words in a sentence
def printSentence(sentence):
    print(*sentence,'.')

if __name__ == '__main__':
    sentenceWordCount = int(sys.argv[1])
    listOfNumbers = randomIntegersList()
    sentence = findRandomWord(listOfNumbers)
    printSentence(sentence)
