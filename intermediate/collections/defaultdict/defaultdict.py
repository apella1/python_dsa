"""Handling missing keys"""
# defaultdict can be used as you would use a normal dict
from collections import defaultdict

favorites = {"pet": "dog", "color": "purple", "language": "Python"}
print(favorites["color"])
# setdefault() checks if the key exists if not returns the default
print(favorites.setdefault("ide", "Neovim"))
print(favorites)
# returns dog since the key pet already exists
print(favorites.setdefault("pet", "cat"))
# get() returns the default value to the key if missing
# otherwise returns the default value, doesn't persist the entry
print(favorites.get("voice_actor", "Nick Kroll"))
print(favorites)

# the constructor of defaultdict takes in a function object as a first argument
counter = defaultdict(int)
print(counter)
print(counter["dog"])
counter["dog"] += 1
counter["dog"] += 1
counter["dog"] += 1
counter["cat"] += 1
counter["cat"] += 1
counter["python"] += 9
counter["python"] += 9
print(counter)

# grouping things
programs = [
    ("language", "Python"),
    ("language", "Java"),
    ("language", "Python"),
    ("language", "C"),
    ("language", "Rust"),
    ("ide", "VSCode"),
    ("ide", "Neovim"),
    ("ide", "PyCharm"),
    ("ide", "webstorm"),
    ("data_structure", "list"),
    ("data_structure", "linked_list")
]

print(programs)

group_programs = defaultdict(list)

for program, program_type in programs:
    group_programs[program].append(program_type)

print(group_programs)

for program, program_type in group_programs.items():
    print(program, "->", program_type)


print(issubclass(defaultdict, dict))
