# -*- coding: utf-8 -*-
"""HAMLET.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hq0vUyI2CtFe2E91zat70dCeI8c0JZfb
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.corpus import stopwords
import string
from nltk.text import Text
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.corpus import stopwords
from nltk.sentiment import vader

nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('gutenberg')
nltk.download('punkt')
nltk.corpus.gutenberg.fileids()

hamlet_text = nltk.corpus.gutenberg.raw('shakespeare-hamlet.txt')
#len(moby_dick)
type(hamlet_text)
#dir(moby_dick)
#help(moby_dick)

my_string_two = hamlet_text
tokens_two = word_tokenize(my_string_two)
tokens_two = [word.lower() for word in tokens_two]
tokens_two[:5]

print(my_string_two[0:1000])

#create n-grams


generated_4grams = []

ngram_list = nltk.ngrams(tokens_two,2)
ngram_fd = nltk.probability.FreqDist(ngram_list)
t_fd = nltk.probability.FreqDist(tokens_two)
top_ngrams = ngram_fd.most_common(50)

vsent = vader.SentimentIntensityAnalyzer()

for line in top_ngrams:
    ngram, num = line
    print (ngram)
    
print(vsent.polarity_scores(my_string_two))

#remove punctuation
""" remove stopwords """
stop_words = set (stopwords.words('english'))

result_str =  ' '.join([word.lower() for word in my_string_two.split() if word not in stop_words])
result_str2 = ''.join([word for word in result_str if word not in string.punctuation])

#remove punctuation

word_tokens = word_tokenize(result_str2)
#word_tokens = word_tokenize(text_in)
text1 = nltk.Text(word_tokens)

ngram_list = nltk.ngrams(word_tokens,2)
ngram_fd = nltk.probability.FreqDist(ngram_list)
t_fd = nltk.probability.FreqDist(word_tokens)

top_ngrams = ngram_fd.most_common(100)
sorted_ngrams = sorted(top_ngrams)

for line in top_ngrams:
    ngram, num = line
    print (ngram)

text1.concordance("hamlet")

#most frequent words
t_fd = nltk.probability.FreqDist(word_tokens)
#help(t_fd)
t_fd.most_common(25)

#part of speech tagging
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize, pos_tag
print(pos_tag(word_tokens[0:10]))
help(pos_tag)
#https://stackoverflow.com/questions/15388831/what-are-all-possible-pos-tags-of-nltk

#create a list of every verb in moby dick
lst = []
pos_tagged = pos_tag(word_tokens)
for word in pos_tagged:
    txt,pos = word
    if pos == "NN":
        lst.append(txt)

print(lst)

