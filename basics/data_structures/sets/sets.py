"""Built in sets"""

# sets are unordered collections with no duplicate elements
# best suited for membership testing and eliminating duplicate entries

# creating sets
my_empty_set = set()
# ! a = {} creates an empty dictionary not an empty set
my_empty_dictionary = {}

names_set = {"Michael", "James", "Peter", "John", "Bob", "Alice"}

print(names_set)

names_list = ["Peter", "John", "Dave", "Alice", "Bob", "John", "Kate", "Peter"]

unique_ordered_names_list = list(set(names_list))

print("Unique Ordered Names List:")
print(unique_ordered_names_list)

print("Sorted Unique Ordered Names List:")
unique_ordered_names_list.sort()

print(unique_ordered_names_list)

print("John" in unique_ordered_names_list)

# set operations on unique letters from two words

first_letters_set = set("omnipresent")
print(first_letters_set)

second_letters_set = set("necessary")
print(second_letters_set)

print("Letters in Second Word but not First Word:")
print(second_letters_set - first_letters_set)

# either or both
print("First Letters Set or Second Letters Set:")
print(first_letters_set | second_letters_set)
# both
print("First Letters Set and Second Letters Set:")
print(first_letters_set & second_letters_set)
# exclusive or
print("First Letters Set xor Second Letters Set:")
print(first_letters_set ^ second_letters_set)

# * set comprehensions
print("Set Comprehensions:")
a = {x for x in "abracadabra" if x not in "abc"}
b = {c for c in "obnoxious" if c in "xylophone"}

print("Set a")
print(a)

print("Set b")
print(b)
