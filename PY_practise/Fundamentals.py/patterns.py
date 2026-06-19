#Pattern 1: Rectangle
for row in range(3):
    for col in range(5):
        print("*", end="")
    print()

#pattern 2: square
for i in range(4):   #rows
    for j in range(4):   #columns
        print("*", end="")
    print()

#pattern 3: right angled triangle
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

#pattern 4: inverted right angled triangle
for i  in range(5,0,-1):
    for j in range(i):
        print("*", end="")
    print()

#number triangle
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()

#pyramid
for i in range(1, 6):
    #print spaces
    for j in range(5-i):
        print(" ", end="")
    #print stars
    for k in range(2*i-1):
        print("*", end="")
    print()