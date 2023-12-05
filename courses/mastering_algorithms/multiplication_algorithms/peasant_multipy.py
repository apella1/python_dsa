def peasant_multiply(x: int, y: int) -> int:
    prod = 0
    while x > 0:
        if x % 2 == 1:
            prod += y
        x = x // 2
        y = y + y
    return prod


print(peasant_multiply(7, 9))

# The algorithm is fundamentally recursive


def recursive_peasant_multiply(a: int, b: int) -> int:
    if a == 0:
        return 0
    a_hat = a // 2
    b_hat = b + b
    prod = recursive_peasant_multiply(a_hat, b_hat)
    if a % 2 == 1:
        prod = prod + b
    return prod


print(recursive_peasant_multiply(4, 5))
