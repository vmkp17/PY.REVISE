#A Tuple is an ordered and immutable collection of items.
# Creating a Tuple
#person = ("Alice", 30, "Engineer")
# TUPLE OPERATIONS DEMO

student = ("MADHURI", 20, "AIML", 20)

print("Original Tuple:")
print(student)

# Accessing Elements
print("\nFirst Element:")
print(student[0])

print("\nLast Element:")
print(student[-1])

# Length
print("\nLength of Tuple:")
print(len(student))

# count()
print("\nCount of 20:")
print(student.count(20))

# index()
print("\nIndex of AIML:")
print(student.index("AIML"))

# Membership Operator
print("\nCheck FIFA Exists:")
print("FIFA" in student)

# Looping
print("\nLooping Through Tuple:")
for item in student:
    print(item)

# Tuple Slicing
print("\nSlicing [0:3]:")
print(student[0:3])

# Tuple Unpacking
print("\nTuple Unpacking:")
name, age, dept, marks = student

print(name)
print(age)
print(dept)
print(marks)

# Tuple Concatenation
print("\nConcatenation:")
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)
# Tuple Repetition
print(t1 * 3)