#A decorator adds extra functionality to a function without modifying the original function.

def stars(func):
    def wrapper():
        print("*" * 20)
        func()
        print("*" * 20)
    return wrapper
@stars
def message():
    print("Welcome MADHURI")
message()