""""A Quick Refresher on Python Basics"""
# pylint: disable=C0103
# - [C0103] is a warning for naming constants with UPPER_CASE convention.
#   When checking names, Pylint differentiates between constants, variables,
#   classes etc. Any name that is NOT inside a function/class will be
#   considered a constant, anything else is a variable.

class Student:
    """ A student class we created to practice inheritance with. """
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        """ Returns the students average marks. """
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args):
        """ Return a new Student called 'friend_name' in the same school as self. """
        return cls(friend_name, origin.school, *args)

    @classmethod
    def kwfriend(cls, origin, friend_name, **kwargs):
        """ Return a new Student called 'friend_name' in the same school as self. """
        return cls(friend_name, origin.school, **kwargs)

class WorkingStudent(Student):
    """ A working student class we created to practice inheritance with. """
    def __init__(self, name, school, salary, job):
        super().__init__(name, school)
        self.salary = salary
        self.job = job

anna = WorkingStudent("Anna", "Oxford", 20.00, "Artist")
friend = WorkingStudent.friend(anna, "Greg", 22.50, "IT")
friend = WorkingStudent.kwfriend(anna, "Jeff", salary=17.50, job="IT")
classmate = Student.friend(anna, "Jane")
print(anna.name, anna.school, anna.salary, anna.job)
print(friend.name, friend.school, friend.salary, friend.job)
print(classmate.name, classmate.school)
