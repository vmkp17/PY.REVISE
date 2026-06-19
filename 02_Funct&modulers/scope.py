#Scope determines where a variable can be accessed.

# Local Scope :x exists only inside functi
def test():
    x = 10

# Global Scope :y exists outside the function and can be accessed anywhere in the program
x = 20
def test():
    print(x)  # Accessing the global variable x