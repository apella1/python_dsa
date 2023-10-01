"""Using optional arguments in named tuples"""
# * rename, defaults, module

from collections import namedtuple

# rename - set to True if you have no control of the field names

# defaults
Developer = namedtuple("Developer", "name level language",
                       defaults=["Junior", "Python"])

print(Developer("John"))


Game = namedtuple("Game", "name no_of_players creator",
                  defaults=["Football", 11, "English"])

print(Game("Basketball", 5, "American"))
