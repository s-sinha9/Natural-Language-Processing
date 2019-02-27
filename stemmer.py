from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

f=open("sample.txt")
text=f.read()

lst = word_tokenize(text)
for w in lst:
    print(w,end=' ')

print("\nPorter Stemmer Algorithm")
ps=PorterStemmer()

for w in lst:
    print(ps.stem(w),end=' ')


