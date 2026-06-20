#A concise way to create a list using a single line of code.
#eg: 
'''squares = [i * i for i in range(1, 6)]
print(squares)'''   #output: [1, 4, 9, 16, 25]

#IMP  PATTERN : [new_value for item in collection]
#IMP  PATTERN : [new_value for item in iterable if condition]

#EG2
''' even = [i for i in range(1,11) if i % 2 == 0]
print(even)'''  #output: [2, 4, 6, 8, 10]