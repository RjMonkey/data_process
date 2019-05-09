import fasttext
import os
import nltk
import io

from nltk import sent_tokenize
import sys

reload(sys)
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding()
file = io.open('data.txt', 'r', encoding="utf8")
text = file.read()

sentences = sent_tokenize(text)
f = io.open('data_sentence.txt', 'w', encoding="utf8")

f.write(sentences)
# model = fasttext.cbow(sentences, 'model')
# print model.words
pass