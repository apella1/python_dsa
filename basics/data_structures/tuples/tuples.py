"""Built in python tuple object"""
# immutable sequences typically used to store collection of heterogenous data
# e.g 2-tuples produced by enumerate
# ! It's the comma that makes the tuple, not the parentheses
# ! The parentheses are optional except for an empty tuple

characters = ["a", "b", "c", "d"]

for index, character in enumerate(characters):
    print((index, character))

# Constructing tuples
my_empty_tuple = ()
my_singleton = ("a",)
comma_separated_tuple = "a", "b", "c"
comma_separated_tuple_with_brackets = (2, 4, 6)
# Constructor creates a new empty tuple when no args are given
tuple_from_builtin = tuple()

print(tuple("abcd"))
print(tuple("1234"))
print(tuple(["a", "b", "c", "d"]))

# To avoid ambiguity
# f(a, b,c ) -> function call with 3 arguments
# f((a, b,c)) -> function call with the tuple (a, b, c) as the sole argument

# * For heterogenous collections of data where access by name is clearer
# * than access by index, then collections.namedtuple()
# * may be a more appropriate choice than a simple tuple object
