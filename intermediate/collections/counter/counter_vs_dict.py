"""Differences between Counter and dict"""
# Counter is a subclass of dict with some subtle differences

# 1. Counter doesn't implement .fromkeys()
# 2. .update() doesn't replace the count value of the object key
# but instead adds to the existing value

from collections import Counter
from pprint import pprint


letters = Counter("Addis Ababa")
pprint(letters)
letters.update(d=2, a=3)
pprint(letters)

# updating with another counter
letters.update(Counter("monrovia"))
pprint(letters)

# Add a new count pair
letters.update({"a": 10})

pprint(letters)

# * .update() accepts mappings, keyword arguments, iterables, other Counters

# 3. Accessing a missing key for Counters returns a 0 instead of a KeyError
decoupled_letters = Counter("modular")
pprint(decoupled_letters["x"])
