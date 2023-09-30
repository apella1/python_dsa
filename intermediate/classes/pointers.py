"""Pointer behaviors with different data types
"""

# integers are immutable
NUM1 = 3
NUM2 = NUM1
print(f"The value of num1 is {NUM1}")
print(f"The value of num2 is {NUM2}")

print(f"\nNum2 points to {id(NUM2)}")
print(f"Num1 points to {id(NUM1)}")

NUM2 = 22

print(f"The value of num2 is {NUM2}")
print(f"The value of num1 is {NUM1}")


print(f"\nNum2 points to {id(NUM2)}")
print(f"Num1 points to {id(NUM1)}")

# Dictionaries
# Dictionaries are mutable

dict1 = {"value": 11}
dict2 = dict1


print("Before value is updated:\n")
print(f"Dict1 is {dict1}")
print(f"Dict2 is {dict2}")
print(f"Dict 1 points to {id(dict1)}")
print(f"Dict 2 points to {id(dict2)}")


dict2["value"] = 22
print("After value is updated:\n")
print(f"Dict1 is {dict1}")
print(f"Dict2 is {dict2}")
print(f"Dict 1 points to {id(dict1)}")
print(f"Dict 2 points to {id(dict2)}")


# set1 = {"hello", "hi"}
# tuple1 = ("hello", "hello", "hello")

# Garbage collection - Removing values that no longer have pointers
# dict1 and dict2 are now pointing to the value of dict3
# therefore the initial dict {"value": 22} is garbage collected
dict3 = {"value": 32}
dict1 = dict3
dict2 = dict3

print(dict1, dict2, dict3)
