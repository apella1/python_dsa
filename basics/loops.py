"""_summary_

    Returns:
        _type_: _description_
    """
# for loops
nums = [1, 2, 3, 4, 5, 6, 7]

for num in nums:
    if num % 3 == 0:
        print(num)

# for loops with range
for i in range(3, 9):
    print(i)

# nested for loops
teams = [["Elly", "Chris"], ["John", "Matt"],
         ["Scott", "Wes"], ["Huberman", "Lex"]]


for team in teams:
    for name in team:
        if name.startswith("J"):
            print(name)


for i in range(3):
    print(teams)

# while loop

number = 8

while number < 18:
    print("Nice!")
    number += 1


# loops exercises
# counting numbers divisible by 10
def divisible_by_ten(numbers):
    """ Returns the number of elements in an array divisible by 10

    Args:
        numbers (list[int]): A list of integer arrays

    Returns:
        int : the number of occurrences of elements divisible by 10
    """
    count = 0
    for n in numbers:
        if n % 10 == 0:
            count += 1
            print(number, count)
    return count


print(divisible_by_ten(nums))


# appending greetings to names
def add_greetings(names):
    """ Prepends greeting to each name in the provided list of names
        and returns the new list

    Args:
        names (list[str]): A string list of names

    Returns:
        list[str] : list of the names with greeting prepended
    """
    greetings = []
    for name in names:
        greetings.append(f"Hello, {name}")
    return greetings

# deleting starting even numbers


def delete_starting_evens(my_list):
    """ Deletes all starting even elements in a list of ints

    Args:
        my_list (list[int]): list of ints

    Returns:
        list[int] : a new list without the preceding even elements
    """
    for item in my_list:
        if item % 2 == 0:
            my_list.remove(item)
    # if len(my_list) > 0:
    #     for j in range(len(my_list)):
    #         if my_list[j] % 2 == 0:
    #             my_list.pop(j)
    return my_list


def delete_starting_evens2(my_list):
    """ Deletes all starting even elements in a list of ints

    Args:
        my_list (list[int]): list of ints

    Returns:
        list[int] : a new list without the preceding even elements
    """
    while (len(my_list) > 0 and my_list[0] % 2 == 0):
        my_list = my_list[1:]
    return my_list


print(delete_starting_evens2([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens2([4, 8, 10]))


def delete_starting_odds(numbers):
    """ Deletes all starting odd elements in a list of ints

    Args:
        my_list (list[int]): list of ints

    Returns:
        list[int] : a new list without the preceding odd elements
    """

    while (len(numbers) > 0 and numbers[0] % 2 == 1):
        numbers = numbers[1:]
    return numbers


print(delete_starting_odds([3, 17, 13, 4, 5, 12, 6, 78]))
print(delete_starting_odds([3, 17, 13]))
