# 1. Large power

def large_power(base, exponent):
    return True if base ** exponent > 5000 else False


# 2. Over Budget
def is_over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    over_budget = None
    total = food_bill + electricity_bill + internet_bill + rent
    if total > budget:
        over_budget = True
    else:
        over_budget = False

    return over_budget

# 3. Twice as Large


def twice_as_large(num1, num2):
    return True if num1 > num2 * 2 else False

# 4. Divisible by 10


def divisible_by_ten(num):
    return True if num % 10 == 0 else False


# Not sum to 10
def does_not_sum_to_ten(num1, num2):
    return True if num1 + num2 != 10 else False


# Advanced Challenges

# 1. In Range
def in_range(num, lower, upper):
    return True if (num >= lower and num <= upper) else False


#  2. Same Name
def same_name(your_name, my_name):
    if your_name == my_name:
        return True
    return False


# 3. Always False - Including a contradiction
def always_false(num):
    return True if num > 1 and num < 1 else False


# 4. Movie Review
def movie_review(rating):
    if rating <= 5:
        return "Avoid at all costs!"
    elif rating < 9:
        return "This was fun."
    else:
        return "Outstanding!"


# 5. Max Num
def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "It's a tie"
