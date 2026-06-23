'''LEGB Rule: Local, Enclosing, Global, Built-in'''


#Namespace is a container that stores variable names and their values. It is a mapping between names and objects. In Python, namespaces are implemented as dictionaries that map names to objects. There are four types of namespaces in Python:
#1. Built-in namespace: Contains names of built-in functions and exceptions. It is created when the Python interpreter starts.
#example: print(), len(), Exception, etc.

#2. Global namespace: Contains names defined at the top level of a module or script. It is created when the module is imported or the script is executed.
#example: variables, functions, and classes defined in a module.

name = "MADHURI"  #wrks everywhere in the module

def test():

    print(name)

test()           #OP: MADHURI 


#3. Local namespace: Contains names defined within a function. It is created when the function is called and destroyed when the function returns.
#example: variables defined within a function.

def test():
    name = "Ali"

    print(name)

test()          #OP: Ali


#4. Enclosing namespace: Contains names defined in the enclosing function. It is created when an inner function is defined and destroyed when the outer function returns.
#example: variables defined in an outer function that are accessed by an inner function.

def outer():

    name = "KRISHNA"

    def inner():

        print(name)

    inner()

outer()              #OP: KRISHNA