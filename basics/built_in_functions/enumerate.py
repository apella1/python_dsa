fruits = ["bananas", "oranges", "apples", "strawberry"]

for index, element in enumerate(fruits):
    print(f"Index: {index}, Element: {element}")


even_numbers = [2, 4, 6, 8]
prime_numbers = [2, 3, 5, 7]


def same_values(lst1, lst2):
    new_list = []
    for index, value in enumerate(lst1):
        if value == lst2[index]:
            new_list.append(index)
    return new_list


print(same_values(even_numbers, prime_numbers))


def enumerate_implementation(iterable, start=0):
    n = start
    for elem in iterable:
        yield n, elem
        n += 1


for a, b in enumerate_implementation(even_numbers):
    print(f"Index: {a}, Element: {b}")
