import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps=PorterStemmer()

words=['reached','reaching','reacher']

for w in words:
    print(ps.stem(w))


