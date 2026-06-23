#User doesn't need to know how something works internally.
#Abstraction means showing only essential features and hiding implementation details.


from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):

        print("Bark")


class Cat(Animal):

    def sound(self):

        print("Meow")

dog = Dog()
cat = Cat()
dog.sound()
cat.sound()

'''  Encapsulation=Hide WHAT data is stored

Abstraction=Hide HOW things work
'''