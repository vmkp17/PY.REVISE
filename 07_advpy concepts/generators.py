# A generator produces values one at a time instead of storing everything in memory
#YIELD: Give value and pause function

'''def count():

    for i in range(1,6):

        yield i
gen = count()
for num in gen:
    print(num)'''


# DIFFERENCE LIST AND GEN
#list:Creates all values now.
squares = [x*x for x in range(5)]  #OP: [0,1,4,9,16]

#Generator:Creates value when requested.
squares = (x*x for x in range(5))  
print(next(squares))
print(next(squares))
print(next(squares))               #OP: 0,1,4

