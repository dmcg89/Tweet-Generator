import random

text = 'one fish two fish red fish blue fish'
word_list = text.split()
# print(word_list)

# builds histogram to be used as input
def histogram(word_list):
    """Builds histogram from text input"""
    dict = {}
    for word in word_list:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict

hist = histogram(word_list)
# print(hist)

def weighted_random_select(dict, word_list):
    """Takes in a histogram and generates a random word with weighted probability"""
    randomChoice = random.randint(1, len(word_list))
    weights_sum = 0
    # print(randomChoice)

    for key in dict:
        weights_sum += dict[key]

        if randomChoice <= weights_sum:
            # print(randomChoice)
            # print(weights_sum)
            # print(key)
            return key
            exit

def frequency_test(hist, word_list):
    """Takes in the histogram, runs the weighted random selection function on it to generate a list of relative probabilities associated with each word"""
    temp_word_list = []
    for i in range(100000):
        selectWord = weighted_random_select(hist, word_list)
        temp_word_list.append(selectWord)
    frequencyList = histogram(temp_word_list)
    for key in frequencyList:
        frequencyList[key] = frequencyList[key]/len(temp_word_list)
        # frequencyList[key] = frequencyList[key]

    print(frequencyList)



frequency_test(hist, word_list)

# weighted_random_select(hist, word_list)
