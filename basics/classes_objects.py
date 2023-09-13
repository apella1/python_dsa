class Dog:
    """_summary_
    """
    pass


pepper = Dog()

print(pepper)


class ClassSchedule:
    """_summary_
    """
    # constructor
    def __init__(self, course, instructor, no_of_students, funded):
        self.course = course
        self.instructor = instructor
        # protected access modifier using the _ symbol
        self._no_of_students = no_of_students
        # private modifiers
        self.__funded = funded
    # destructor
    def __del__(self):
        print(f"You successfully deleted {self.course}.")

    def display_course(self):
        """_summary_
        """
        print(f"Course: {self.course}, Instructor: {self.instructor}")

    def is_course_funded(self):
        """_summary_
        """
        if self.__funded:
            print(f"{self.course} is funded")
        else:
            print(f"{self.course} is not funded")


chemistry = ClassSchedule("Chemistry", "Mr. Feynman", 8, False)

print(chemistry.display_course())
print(chemistry.course)
# print(chemistry.__funded) - private members cannot be accessed
print(chemistry.is_course_funded())
del chemistry
