


#  /$$$$$$  /$$$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$ /$$      /$$       /$$                                               /$$                                           /$$     /$$                    
# /$$__  $$| $$_____/| $$$ | $$ /$$__  $$|_  $$_/| $$$    /$$$      |__/                                              | $$                                          | $$    |__/                    
#| $$  \__/| $$      | $$$$| $$| $$  \__/  | $$  | $$$$  /$$$$       /$$ /$$$$$$/$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$          /$$$$$$$  /$$$$$$   /$$$$$$$ /$$$$$$   /$$  /$$$$$$  /$$$$$$$ 
#| $$ /$$$$| $$$$$   | $$ $$ $$|  $$$$$$   | $$  | $$ $$/$$ $$      | $$| $$_  $$_  $$ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/         /$$_____/ /$$__  $$ /$$_____/|_  $$_/  | $$ /$$__  $$| $$__  $$
#| $$|_  $$| $$__/   | $$  $$$$ \____  $$  | $$  | $$  $$$| $$      | $$| $$ \ $$ \ $$| $$  \ $$| $$  \ $$| $$  \__/  | $$          |  $$$$$$ | $$$$$$$$| $$        | $$    | $$| $$  \ $$| $$  \ $$
#| $$  \ $$| $$      | $$\  $$$ /$$  \ $$  | $$  | $$\  $ | $$      | $$| $$ | $$ | $$| $$  | $$| $$  | $$| $$        | $$ /$$       \____  $$| $$_____/| $$        | $$ /$$| $$| $$  | $$| $$  | $$
#|  $$$$$$/| $$$$$$$$| $$ \  $$|  $$$$$$/ /$$$$$$| $$ \/  | $$      | $$| $$ | $$ | $$| $$$$$$$/|  $$$$$$/| $$        |  $$$$/       /$$$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$
# \______/ |________/|__/  \__/ \______/ |______/|__/     |__/      |__/|__/ |__/ |__/| $$____/  \______/ |__/         \___/        |_______/  \_______/ \_______/   \___/  |__/ \______/ |__/  |__/
#                                                                                     | $$                                                                                                          
#                                                                                     | $$                                                                                                          
#                                                                                     |__/                                                                                                          

            
from gensim import corpora
import pickle
import gensim
from scrapy.utils.project import get_project_settings
from datetime import date
import pymongo

ldamodel = None
today = date.today()
topics = []

def create_lda_model(text_data):
    dictionary = corpora.Dictionary(text_data)
    corpus = [dictionary.doc2bow(text) for text in text_data]

    pickle.dump(corpus, open('corpus.pkl', 'wb'))
    dictionary.save('dictionary.gensim')

    NUM_TOPICS = 5
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
    ldamodel.save('model5.gensim')
    
    for elem in ldamodel.print_topics(num_topics=-1, num_words=20):
        topics.append(elem)
