# protecting data..Encapsulation means wrapping data and methods together and restricting direct access to data.

class Student:

    def __init__(self):

        self.__cgpa = 9.0   #double underscore makes it private and cannot be accessed outside the class.
                            #Hide data: double underscore is used to hide data from outside the class. It is a way to implement encapsulation in Python.

s1 = Student()

print(s1.__cgpa)   #attribute error: 'Student' object has no attribute '__cgpa'

#To protect data from direct access and allow controlled, secure access through methods.