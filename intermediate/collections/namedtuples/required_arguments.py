"""namedtuple() is a factory function rather than a typical data structure"""
from collections import namedtuple

# different ways of providing field_names
# * 1. As an iterable of strings
# sequenced iterables should be used. Sets would provide unreliable access
# ! e.g Point = namedtuple("Point", {"x", "y"})
Point = namedtuple("Point", ["x", "y"])
print(Point)
print(Point(12, 4))

# * 2. Using comma separated field names
Language = namedtuple("ProgrammingLanguage", "name, purpose, age, creator")

java = Language("Java", "Large computing", 13, "James Gosling")
print(java)

# * 3. Using a generator expression for the field names

LocalPoint = namedtuple("LocalPoint", (field for field in "abc"))
print(LocalPoint(1, 2, 3))

# All valid python identifiers can be used for field names
# except for names starting with an underscore
# and Python keywords
