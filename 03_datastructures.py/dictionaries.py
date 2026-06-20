# A Dictionary stores data in Key-Value pairs.
''' Example: student = {
    "name": "FIFA",
    "age": 20
}'''

# DICTIONARY OPERATIONS

student = {
    "name": "FIFA",
    "age": 20,
    "cgpa": 9.0
}

print("Original Dictionary:") 
print(student)

# Access
print("\nName:")
print(student["name"])

# get()
print("\nUsing get():")
print(student.get("age"))

# Add
student["city"] = "Vijayawada"
print("\nAfter Adding:")
print(student)

# Update
student["age"] = 21
print("\nAfter Update:")
print(student)

# keys()
print("\nKeys:")
print(student.keys())

# values()
print("\nValues:")
print(student.values())

# items()
print("\nItems:")
print(student.items())

# pop()
student.pop("city")
print("\nAfter pop():")
print(student)

# copy()
new_dict = student.copy()
print("\nCopied Dictionary:")
print(new_dict)

# clear()
temp = {"a":1,"b":2}
temp.clear()
print("\nAfter clear():")
print(temp)