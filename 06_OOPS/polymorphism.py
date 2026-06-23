'''  Poly = Many
Morphism = Forms
''' #same method different behavior

#Method Overriding:Child class method replaces parent class method.
class Animal:

    def sound(self):

        print("Animal Sound")


class Dog(Animal):

    def sound(self):

        print("Bark")
dog = Dog()
dog.sound()


#Method Overloading:Same method name with different parameters.
#py dont work with true overloading, it uses args* for implementation.

class Calculator:

    def add(self, *numbers):

        total = 0

        for num in numbers:
            total += num

        return total

calc = Calculator()
print(calc.add(10, 20))
print(calc.add(10, 20, 30))