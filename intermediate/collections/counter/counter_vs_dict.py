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


# In Python, Counter is also useful to emulate a multiset or a bag
# Multisests are similar to sets but allow multiple instances
# of a given element
# ! multiplicity - the number of instances of an element

multiset = Counter([1, 1, 2, 2, 2, 3, 3, 4])
pprint(multiset)

# The keys are equivalent to a set
# -> the values hold multiplicity of each element
print(multiset.keys())


# Local pet shelter analogy
inventory = Counter(snakes=8, dogs=12, cats=7, rabbits=22)
adopted = Counter(snakes=2, dogs=6, cats=7, rabbits=0)
inventory.subtract(adopted)
pprint(inventory)
pprint(inventory.keys())
pprint(inventory.values())

new_pets = {"cats": 19, "dogs": 10}
inventory.update(new_pets)
pprint(inventory)

inventory = inventory - Counter(cats=12, dogs=4, rabbits=20)
pprint(inventory)
inventory += {"cats": 2, "dogs": 3, "rabbits": 5}
pprint(inventory)

# .subtract() and .update() can be used to update the records of the counter
# addition, subtraction and their respective assignment operators can be used
# i.e  -= and +=
