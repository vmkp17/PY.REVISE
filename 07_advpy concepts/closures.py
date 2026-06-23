# it remembers variables even after the outer function has finished.

def outer():

    name = "madhuri"

    def inner():

        print(name)

    return inner


my_function = outer()

my_function()