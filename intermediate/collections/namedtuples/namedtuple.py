"""Factory function for tuples with named fields"""
from collections import namedtuple

# creating a 2-D point as a tuple (immutable)
point = (2, 4)

# Accessing the coordinates
print(point[0], point[1])

# ! point[0] = 5
# ! tuples do not support item assignment

# * A namedtuple factory class is used to avoid the ambiguity
# * of accessing tuple values using indices
Point = namedtuple("Point", "x y")
print(issubclass(Point, tuple))

# Instantiating the new type
point = Point(5, 7)
print(point.x, point.y)

# named tuples are also immutable so there's no item assignment
# e.g point.x = 79
# indices can still be used to access the value of each coordinate
# in a named tuple

Sport = namedtuple("Sport", "name players_number")
Person = namedtuple("Person", "name children")
Subject = namedtuple("Subject", "category has_prerequisites")

football = Sport("Football", 11)
john = Person("John", ["Pete", "Owen", "Parker"])
maths = Subject("Mathematics", False)

print(john.children)
john.children.append("Tammy")
print(john.children)
print(football)
print(id(john.name))

# named tuples objects can be mutable,
# however the tuple itself has the same reference in memory

# tuples with mutable values can't be hashed
# football is hashable since all its objects are immutable
print(hash(football))
# john isn't hashable since it has a mutable list object
# ! traceback: unhashable type 'list'
# print(hash(john))
print(hash(maths))


Project = namedtuple("Project", "name number_of_people inception_year",
                     defaults=["Long Ropes In Flower Gardens", 19, 2021])

default_project = Project()
print(default_project)


print(divmod(4, 2))


def custom_divmod(x, y):
    """Specifying the remainder and quotient"""
    DivMod = namedtuple("Divmod", "quotient remainder")
    return DivMod(*divmod(x, y))


result = custom_divmod(12, 6)

print(result.quotient)
print(result.remainder)
