"""This module covers the built in enumerate function"""
fruits = ["bananas", "oranges", "apples", "strawberry"]

for index, element in enumerate(fruits):
    print(f"Index: {index}, Element: {element}")


even_numbers = [2, 4, 6, 8]
prime_numbers = [2, 3, 5, 7]


def same_values(lst1, lst2):
    """_summary_

    Args:
        lst1 (_type_): _description_
        lst2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    new_list: list[int] = []
    for index, value in enumerate(lst1):
        if value == lst2[index]:
            new_list.append(index)
    return new_list


print(same_values(even_numbers, prime_numbers))


def enumerate_implementation(iterable, start=0):
    """Basic implementation of the python built-in enumerate function

    Args:
        iterable (_type_): _description_
        start (int, optional): _description_. Defaults to 0.

    Yields:
        _type_: _description_
    """
    n = start
    for elem in iterable:
        yield n, elem
        n += 1


for a, b in enumerate_implementation(even_numbers):
    print(f"Index: {a}, Element: {b}")
