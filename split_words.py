import os
import nltk
import io
import string
from nltk.corpus import stopwords
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
import sys
import re



reload(sys)
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding()
# nltk.download('stopwords')
file = io.open('data/data.txt', 'r', encoding="utf8")
text = file.read()

tokens = word_tokenize(text)

words = [word for word in tokens if word.isalpha()]


#stop_words = set(stopwords.words('english'))
#words = ' '.join([w for w in words if not w in stop_words])


f = io.open('data_word_embedding.txt', 'w', encoding="utf8")

f.write(' '.join(words))

# model = fasttext.cbow(sentences, 'model')
# print model.words
pass