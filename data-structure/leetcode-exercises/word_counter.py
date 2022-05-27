# poem.txt Contains famous poem "Road not taken" by poet Robert Frost.
# You have to read this file in python and print every word and
# its count as show below. Think about the best data structure
# that you can use to solve this problem and figure out why you
# selected that specific data structure.
import re

word_database = {}

def preprocess(line):
    pattern = r'\w+'
    res = re.findall(pattern, line)
    return res

with open('poem.txt', 'r') as f:
    for line in f:
        words = preprocess(line.splitlines()[0])
        for word in words:
            word = word.lower()
            if word not in word_database:
                word_database[word] = 1
            else:
                word_database[word] += 1

print(word_database)
