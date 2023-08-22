# classes should use pascal case

class MyDog:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("My dog's name is: ", self.name)


favorite_dog = MyDog("Pepper")

# function and variable names should use snake casing


def calculate_force(mass, acc):
    force = mass * acc
    return force


def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)


print(calculate_factorial(8))

# the main function is used as an entry point to the program
