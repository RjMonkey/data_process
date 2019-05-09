import os
import io
from nltk.tokenize import word_tokenize

data = []
file_list = os.listdir("./2wdata")
for file in file_list:

    f = io.open('./2wdata/' + file, "r", encoding="utf8")
    text = f.read()
    tokens = word_tokenize(text)
    if "collectwhen" in tokens:
        num = tokens.index("collectwhen")
        print num
        print file

    words = [word for word in tokens if word.isalpha()]
    text = ' '.join(words)
    data.append(text)

text = ' '.join(data)
f = io.open('./data/test.txt', 'w', encoding="utf8")

f.write(' '.join(text))