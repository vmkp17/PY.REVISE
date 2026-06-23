#An iterator is an object that returns data one element at a time.

numbers=[10,20,30,40]
for i in numbers:
    print(i)      #Returns values one by one



    #eg2

    colors = ["Red","Blue","Green"]
it = iter(colors)
for item in it:
    print(item)