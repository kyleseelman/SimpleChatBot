import nltk
import numpy as np
import random
import string

file = open('corpus.txt','r',errors = 'ignore')
raw_file = file.read()
raw_file = raw_file.lower()

nltk.download('punkt')
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw_file)
word_tokens = nltk.word_tokenize(raw_file)

print(sent_tokens[:-2])
