#Inheritance allows one class to acquire properties and methods from another class.

''' Parent Class
class Person:

    def __init__(self,name):

        self.name = name

Person is Parent.

Child Class
class Student(Person):
    pass

Student is Child.'''


class Person:

    def __init__(self,name):

        self.name = name

class Student(Person):

    pass

s1 = Student("madhuri")

print(s1.name)