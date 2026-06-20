#A Data Structure is a way of organizing and storing data efficiently.
# Lists are used to store multiple related values in one variable.
#A List is an ordered collection of multiple items.

# Creating a List
fruits = ["Apple", "Mango", "Orange"]

print("Original List:")
print(fruits)

# Accessing Elements
print("\nFirst Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

# Updating Element
fruits[1] = "Banana"
print("\nAfter Updating:")
print(fruits)

# append()
fruits.append("Grapes")
print("\nAfter Append:")
print(fruits)

# insert()
fruits.insert(1, "Pineapple")
print("\nAfter Insert:")
print(fruits)

# extend()
fruits.extend(["Kiwi", "Papaya"])
print("\nAfter Extend:")
print(fruits)

# remove()
fruits.remove("Orange")
print("\nAfter Remove:")
print(fruits)

# pop()
fruits.pop()
print("\nAfter Pop:")
print(fruits)

# pop(index)
fruits.pop(1)
print("\nAfter Pop Index:")
print(fruits)

# index()
print("\nIndex of Banana:")
print(fruits.index("Banana"))

# count()
numbers = [10, 20, 10, 30, 10]
print("\nCount of 10:")
print(numbers.count(10))

# sort()
numbers.sort()
print("\nSorted Numbers:")
print(numbers)

# reverse()
numbers.reverse()
print("\nReversed Numbers:")
print(numbers)

# copy()
new_list = numbers.copy()
print("\nCopied List:")
print(new_list)

# len()
print("\nLength:")
print(len(fruits))

# membership
print("\nCheck Item:")
print("Apple" in fruits)

# Looping
print("\nLooping Through List:")
for fruit in fruits:
    print(fruit)

# clear()
temp = [1, 2, 3]
temp.clear()
print("\nAfter Clear:")
print(temp)
