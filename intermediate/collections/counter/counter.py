"""Counting objects in one go"""
from collections import Counter, defaultdict
from pprint import pprint

# counting using a regular dictionary and for loop

SENTENCE = "The quick brown fox jumped over the brown lazy dog"

letter_counter = dict()

for letter in SENTENCE:
    # ! checking if there is  a key i.e letter before incrementing
    # ! to avoid KeyError
    if letter not in letter_counter:
        letter_counter[letter] = 0
    letter_counter[letter] += 1

pprint(letter_counter)

# * defaultdicts are convenient as there is no need
# * to check if a key already exists

WORD = "perpetuity"

# initializing the default dict using the int() factory function
letter_count = defaultdict(int)

for letter in WORD:
    letter_count[letter] += 1

pprint(letter_count)


# the object argument to the Counter() function should be hashable
characters = Counter("mississippi")
pprint(characters)

pprint(hash(45))
pprint(hash("Hello"))
pprint(hash((2, 3, 5)))

# mutable objects are unhashable
# pprint(hash([2, 3, 5]))

# counter is a sub class of dict therefore no restrictions
# on the keys and values of the objects
pprint(issubclass(Counter, dict))
pprint(Counter("atmosphere"))

# ! Differences between Counter and dict
