import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
#nltk.download('punkt')

f=open("sample.txt")
text=f.read()

#print(text)

#print(sent_tokenize(text))

lst = word_tokenize(text)
print(lst)

lst2=[]
for word in lst:
    if(word.isalnum()):
        lst2.append(word)

print(len(lst2))


