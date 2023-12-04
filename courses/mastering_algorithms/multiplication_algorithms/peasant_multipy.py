def peasant_multiply(x, y):
    prod = 0
    while x > 0:
        if x % 2 == 1:
            prod += y
        x = x // 2
        y = y + y
    return prod


print(peasant_multiply(7, 9))

# The algorithm is fundamentally recursive
