from abc import abstractmethod


class Animal:
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def speak(self) -> str:
        pass
        # default implementation
        # return f"{self.name} makes a sound!"


class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return f"{self.name} says Meow!"


# Creating instances of the Dog and Cat class

dog = Dog("Buddy")
cat = Cat("Cindy")


print(dog.speak())
print(cat.speak())
