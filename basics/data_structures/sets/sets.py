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
print(unique_ordered_names_list)
unique_ordered_names_list.sort()
print(unique_ordered_names_list)
print("John" in unique_ordered_names_list)

# set operations on unique letters fro two words

first_letters_set = set("omnipresent")
print(first_letters_set)
second_letters_set = set("necessary")
print(second_letters_set)
print(second_letters_set - first_letters_set)
# either or both
print(first_letters_set | second_letters_set)
# both
print(first_letters_set & second_letters_set)
# exclusive or
print(first_letters_set ^ second_letters_set)

# * set comprehensions
a = {x for x in "abracadabra" if x not in "abc"}
b = {c for c in "obnoxious" if c in "xylophone"}
print(a)
print(b)
