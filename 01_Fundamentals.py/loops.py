#loop : A loop is used to execute a block of code repeatedly.

#FOR LOOP ,range(start, stop)
for i in range(1, 6):
    print(i)
#output: 1 2 3 4 5

#range(start, stop, step)
for i in range(1, 11, 2):
    print(i)    
#output: 1 3 5 7 9

#Reverse Loop
for i in range(10, 0, -1):
    print(i)
#output: 10 9 8 7 6 5 4 3 2 1

#EG: SUM OF NOS
total = 0
for i in range(1, 6):
    total += i
print(total)


#WHILE LOOP
#Used when we don't know exactly how many times to repeat.
print("while loop")

count = 1
while count <= 5:
    print(count)
    count += 1
#output: 1 2 3 4 5