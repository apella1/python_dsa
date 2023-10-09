"""UserDict"""
from collections import UserDict
from pprint import pprint


# Doesn't work when a dictionary is passed into the class constructor
# or using the .update() method meaning more methods would need
# to be overridden such as init and update
# ! only the dictionary assignment works i.e my_dict["A"] = 1
# ! works as expected when UserDict is extended instead of dict
class LowerDict(UserDict):
    """Overriding setitem from the dict class"""

    def __setitem__(self, key, value) -> None:
        key = key.lower()
        return super().__setitem__(key, value)


ordinals = LowerDict({"FIRST": 1, "SECOND": 2})
ordinals["THIRD"] = 3
ordinals.update({"FOURTH": 4})
pprint(ordinals)
# ! not instance of dict when UserDict is extended
# UserDict stores a regular dict in an instance attribute called .data
pprint(isinstance(ordinals, dict))
