import re
import pprint
from collections import Counter

ihaveadream = open('ihaveadream.txt', 'r')

read_dream = ihaveadream.read()

split = read_dream.split()

just_words = [re.sub('[^a-zA-Z]+','',i) for i in split]

just_long_words = []

for word in just_words:
    word = word.lower()
    if len(word) > 3:
        just_long_words.append(word)

freqs = [just_words.count(i) for i in just_long_words]

word_freq = zip(just_long_words, freqs)
repeat = []

for word in word_freq:
    if word not in repeat:
        repeat.append(word)

sorted_wfreq = sorted(repeat, key = lambda x: x[1], reverse = True)

for word in sorted_wfreq:
    print word[0] + ':' + str(word[1]+1)

        