# definition, parameters, arguments, return statement, recursion, base case

def factorial(num):
    call_stack = []
    if num == 1:
        print("Base case reached. Num is 1")
        return 1
    else:
        call_stack.append({'input': num})
        print('call stack: ', call_stack)
        return num * factorial(num - 1)


print(factorial(3))
