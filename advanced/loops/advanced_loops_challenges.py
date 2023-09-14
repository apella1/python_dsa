"""This module covers advanced loop challenges"""

# 1 Larger sum


def larger_sum(lst1, lst2):
    """Returning list whose sum of elements is larger

    Args:
        lst1 (_type_): _description_
        lst2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    lst1_sum = 0
    lst2_sum = 0
    # computing the sum of elements in lst1
    for elem in lst1:
        lst1_sum += elem

    # computing the sum of elements in lst1
    for elem in lst2:
        lst2_sum += elem

    if lst2_sum > lst1_sum:
        return lst2
    else:
        return lst1


# using in-built sum function
def larger_sum2(lst1, lst2):
    """ Using in-built sum function for the implementation

    Args:
        lst1 (list[int]): _description_
        lst2 (list[int]): _description_

    Returns:
        list[int]: list with greater sum of elements
    """
    return lst1 if sum(lst1) > sum(lst2) else lst2

# 2 Over 9000


def over_nine_thousand(lst):
    """_summary_

    Args:
        lst (_type_): _description_

    Returns:
        _type_: _description_
    """
    MAX_SUM = 9000
    power_sum = 0
    for elem in lst:
        power_sum += elem
        if power_sum > MAX_SUM:
            break
    return power_sum


print(sum([]))


# 3 Max Number
def max_num(nums):
    max_number = nums[0]
    for num in nums:
        if num > max_number:
            max_number = num
    return max_number


# 4 Same values
def same_values(lst1, lst2):
    new_list = []
    for index in range(len(lst1)):
        if lst1[index] == lst2(index):
            new_list.append(index)
    return new_list


# 5 Reversed List
def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if lst1[index] != lst2[len(lst2) - 1 - index]:
            return False
    return True


# using enumerate instead of using range and len
def reversed_list2(lst1, lst2):
    for index, value in enumerate(lst1):
        if value != lst2[(len(lst2) - 1 - index)]:
            return False
    return True
