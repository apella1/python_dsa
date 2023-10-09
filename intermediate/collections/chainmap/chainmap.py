"""Chaining dictionaries together"""

# taking multiple mappings and making them logically appear as one
# chainmap objects are updatable views
# - change in mappings affects the whole object


from collections import ChainMap
from pprint import pprint


cmd_proxy = {}
local_proxy = {"proxy": "proxy.local.com"}
global_proxy = {"proxy": "proxy.global.com"}

proxy_config = ChainMap(cmd_proxy, local_proxy, global_proxy)

pprint(proxy_config)
# key lookup searches cmd_proxy, local_proxy then finally global_proxy
# (provided order) -> returning first instance of the key at hand
pprint(proxy_config["proxy"])


numbers = {"one": 1, "two": 2}
letters = {"a": "A", "b": "B"}

alpha_nums = ChainMap(numbers, letters)
pprint(alpha_nums)
pprint(alpha_nums.maps)


dad = {"name": "Peter", "age": 33}
mum = {"name": "Wendy", "age": 30}
son = {"name": "John", "age": 10}
daughter = {"name": "Winnie", "age": 3}

family = ChainMap(dad, mum)
pprint(family.maps)
pprint(family)

family = family.new_child(son)
family = family.new_child(daughter)

pprint(family.maps)
pprint(family.parents)

for person in family.maps:
    pprint(person)

# mutating operations on the internal list of mappings act on the first mapping
# ! using the alpha_nums ChainMap

alpha_nums["c"] = "C"
pprint(alpha_nums)
alpha_nums.pop("one")
pprint(alpha_nums)

# * alpha_nums.pop("one") -> KeyError as the key isn't in the first mapping
alpha_nums.clear()
pprint(alpha_nums)

# Teams
united = {"name": "Manchester United", "trophies": 13}
liverpool = {"name": "Liverpool FC", "trophies": 3}
city = {"name": "Manchester City", "trophies": 7}

epl = ChainMap(city, liverpool, united)
pprint(epl.parents)
pprint(epl.maps)
wolves = {"name": "Wolverhampton Wanderers", "trophies": 0}
epl = epl.new_child(wolves)
pprint(epl)
pprint(epl.parents)
