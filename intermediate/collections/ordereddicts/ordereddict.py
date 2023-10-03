"""Keeping dictionaries ordered"""
from collections import OrderedDict

life_stages = OrderedDict()
life_stages["childhood"] = "0-9"
life_stages["adolescence"] = "9-18"
life_stages["adulthood"] = "18-65"
life_stages["old"] = "+65"

for stage, years in life_stages.items():
    print(stage, "->", years)

# regular dicts also maintain an order
# * however using an ordereddict communicates intent
# * and provides additional features e.g equality test, backward compatibility
# * and control over the order of items

letters = OrderedDict(b=2, d=4, a=1, c=3)
print(letters)

# move b to the right end
letters.move_to_end("b")
print(letters)

# move b to the right end
letters.move_to_end("b", last=False)
print(letters)


# sort letters by key
for key in sorted(letters):
    letters.move_to_end(key)

print(letters)


# comparison
letters_0 = dict(a=1, b=2, c=3, d=4)
letters_1 = dict(b=2, a=1, d=4, c=3)
print(letters_0 == letters_1)


# orderddict compares by content and order
letters_2 = OrderedDict(a=1, b=2, c=3, d=4)
letters_3 = OrderedDict(b=2, a=1, d=4, c=3)
print(letters_2 == letters_3)
