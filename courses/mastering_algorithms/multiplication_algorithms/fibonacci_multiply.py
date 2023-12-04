def fibonacci_multipy(X, Y):
    m = len(X)
    n = len(Y)
    Z = [0] * (m + n)
    hold = 0
    for k in range(n + m - 1):
        for i in range(m):
            j = k - i
            if j >= 0 and j < n and i + j == k:
                hold += X[i] * Y[j]
            Z[k] = hold % 10
            hold //= 10
    Z[m + n - 1] = hold
    while len(Z) > 1 and Z[-1] == 0:
        Z.pop()
    Z.reverse()
    return Z


X = [1, 2, 3]
Y = [4, 5]

Z = fibonacci_multipy(X, Y)
print("The product of two input vector is : ", end="")
for i in range(len(Z)):
    print(Z[i], end="")
print()
