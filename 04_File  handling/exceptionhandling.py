#Unexpected Error

'''try
Means:
Try this code.

except
Means:If error occurs,
execute this block.

finally
Means:Run no matter what.'''



try:

    file = open("student.txt")

except:

    print("Error")

finally:

    print("Finished")

