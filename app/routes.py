from app import app
from histogram import histogram
from stochastic_sample import weighted_random_select
import re, string

@app.route('/')
@app.route('/index')
def index():
    word_file = 'text2.txt'
    text =  open(word_file).read()
    translator = str.maketrans('', '', string.punctuation)
    text = text.lower()
    words_from_text = (text.translate(translator)).split()
    # sorts words alphabetically
    words_from_text = sorted(words_from_text)
    hist = histogram(words_from_text)
    sentence = []
    for i in range(10):
        select_word = weighted_random_select(hist, words_from_text)
        sentence.append(select_word)
    print(sentence)
    new_sentence = " ".join(sentence)
    print(new_sentence)



    return new_sentence
