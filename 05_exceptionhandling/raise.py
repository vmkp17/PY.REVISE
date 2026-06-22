#Creates your own exception.

age = int(input())

if age < 18:
    raise ValueError("Age must be 18 or above")