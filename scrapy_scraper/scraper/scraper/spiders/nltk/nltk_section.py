


# /$$   /$$ /$$    /$$$$$$$$ /$$   /$$       /$$                                               /$$                                           /$$     /$$                    
#| $$$ | $$| $$   |__  $$__/| $$  /$$/      |__/                                              | $$                                          | $$    |__/                    
#| $$$$| $$| $$      | $$   | $$ /$$/        /$$ /$$$$$$/$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$          /$$$$$$$  /$$$$$$   /$$$$$$$ /$$$$$$   /$$  /$$$$$$  /$$$$$$$ 
#| $$ $$ $$| $$      | $$   | $$$$$/        | $$| $$_  $$_  $$ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/         /$$_____/ /$$__  $$ /$$_____/|_  $$_/  | $$ /$$__  $$| $$__  $$
#| $$  $$$$| $$      | $$   | $$  $$        | $$| $$ \ $$ \ $$| $$  \ $$| $$  \ $$| $$  \__/  | $$          |  $$$$$$ | $$$$$$$$| $$        | $$    | $$| $$  \ $$| $$  \ $$
#| $$\  $$$| $$      | $$   | $$\  $$       | $$| $$ | $$ | $$| $$  | $$| $$  | $$| $$        | $$ /$$       \____  $$| $$_____/| $$        | $$ /$$| $$| $$  | $$| $$  | $$
#| $$ \  $$| $$$$$$$$| $$   | $$ \  $$      | $$| $$ | $$ | $$| $$$$$$$/|  $$$$$$/| $$        |  $$$$/       /$$$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$
#|__/  \__/|________/|__/   |__/  \__/      |__/|__/ |__/ |__/| $$____/  \______/ |__/         \___/        |_______/  \_______/ \_______/   \___/  |__/ \______/ |__/  |__/
#                                                             | $$                                                                                                          
#                                                             | $$                                                                                                          
#                                                             |__/                                                                                                          


#word lemmatize and stopwords removing with NLTK
import nltk
from .spacy_section import *
from .gensim_section import *
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

def get_lemma(word):
    lemma = wn.morphy(word)
    if lemma is None:
        return word
    else:
        return lemma
    
from nltk.stem.wordnet import WordNetLemmatizer
def get_lemma2(word):
    return WordNetLemmatizer().lemmatize(word)

nltk.download('stopwords')
it_stop = set(nltk.corpus.stopwords.words('italian'))

def prepare_text_for_lda(text):
    tokens = tokenize(text)
    tokens = [token for token in tokens if len(token) > 4]
    tokens = [token for token in tokens if token not in it_stop]
    tokens = [get_lemma(token) for token in tokens]
    return tokens

#generate LDA-Model with GENSIM
import random
text_data = []
def prepare_text(input):
    for elem in range(len(input)):
        tokens = prepare_text_for_lda(input[elem])
        for elem in range(len(tokens)):
            text_data.append(tokens)
    create_lda_model(text_data)
    