import nltk
from nltk import WordNetLemmatizer
import re
import sys, codecs

def clean(word):
    word = re.sub("(\@[A-Za-z0-9]*)|(www\.[A-Za-z0-9]*)|([\.\-\/!\?%$\:;#,&]+)|(\/\/t\.co[A-Za-z0-9]*)|([.\(\)][A-Za-z0-9]*)|(http[s]?:\/\/[A-Za-z0-9]*)|([A-Za-z]*[0-9][A-Za-z]*)|(\.,\'\"\(\))", '', word)
    word = nltk.stem.WordNetLemmatizer().lemmatize(word.lower())
    return word

with open('anstlskwts.txt', 'r', encoding='utf-8') as f:
    raw = f.read().split(' ')
with open('file1.txt', 'a') as f:
    for word in raw:
        f.write(str(clean(word)+' '))

