#A function calling itself.

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)
print("Countdown:")
countdown(5)